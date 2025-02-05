# -*- coding: utf-8 -*-
# @project Brasileirao
# @description Classe que converte os PDFs em CSVs
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

import os
import re
import PyPDF2

from codigo.Amarelo             import Amarelo,             adicionaAmarelo, imprimeAmarelos
from codigo.Vermelho            import Vermelho,            adicionaVermelho, imprimeVermelhos
from codigo.Arbitro             import Arbitro,             adicionaArbitro, imprimeArbitros
from codigo.Campeonato          import Campeonato,          adicionaCampeonato
from codigo.Gol                 import Gol,                 adicionaGol, imprimeGols
from codigo.Jogador             import Jogador,             adicionaJogador, imprimeJogadores
from codigo.Partida             import Partida,             adicionaPartida, imprimePartidas, imprimeHorarioPartidas
from codigo.Time                import Time,                adicionaTime, imprimeTimes, buscaTime

from codigo.Impressao           import                      imprimeCSV
from codigo.Extrator            import                      extrai1Valor, extrai2Valores, extrai3Valores

from analise.Basica             import                      basicaDescribe, basicaHistograma, basicaRelacionamento, basicaPorPeriodo
from analise.Estatistica        import                      basicaNormalidade, basicaAnova, basicaKruskal, powerAnalysis

Amarelos = []
Vermelhos = []

Arbitros = []
Campeonatos = []
Gols = []
Jogadores = []
Partidas = []
Times = []

def converteCSVs(campeonato):

    if campeonato == "":
        campeonato = "dados"

    pasta = "pdfs/" + campeonato + "/";

    arquivos = os.listdir(pasta)
    for pdf in [arquivo for arquivo in arquivos if arquivo.endswith('.pdf')]:

        caminho_pdf = os.path.join(pasta, pdf)
        print("Lendo arquivo " + caminho_pdf)

        with open(caminho_pdf, 'rb') as pdf_file:

            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_paginas = len(pdf_reader.pages)

            partidaId = -1
            for pagina_num in range(num_paginas):

                pagina = pdf_reader.pages[pagina_num]
                texto = pagina.extract_text()
                linhas = texto.split('\n')

                if pagina_num == 0:

                    start = 0
                    while linhas[start][0:5] != "Jogo:":
                        start = start + 1

                    # Extrai as informacoes iniciais
                    cbf = extrai1Valor(linhas[start], 'Jogo')
                    camp, rodada = extrai2Valores(linhas[start + 2], 'Campeonato', 'Rodada')
                    data, horario, estadio = extrai3Valores(linhas[start + 4], 'Data', 'Horário', 'Estádio')

                    # Extrai e cria o arbitro
                    arbitroString = extrai1Valor(linhas[start + 6], 'Arbitro')
                    arbitroGrupo = re.match(r"(.+?)\s\((.+?)\s\/\s([A-Z]{2})\)", arbitroString)
                    arbitroNome = arbitroGrupo.group(1)
                    arbitroCredencial = arbitroGrupo.group(2)
                    arbitroEstado = arbitroGrupo.group(3)
                    arbitroId = adicionaArbitro(Arbitros, arbitroNome, arbitroCredencial, arbitroEstado)

                    # Cria o campeonato
                    campeonatoId = adicionaCampeonato(Campeonatos, camp)

                    # Cria e preenche a partida
                    jogo = extrai1Valor(linhas[start], 'Jogo')
                    partidaId = adicionaPartida(Partidas, jogo)
                    Partidas[partidaId].campeonatoId = campeonatoId
                    Partidas[partidaId].arbitroId = arbitroId
                    Partidas[partidaId].rodada = rodada.strip(' ')
                    Partidas[partidaId].data = data
                    Partidas[partidaId].horario = horario
                    Partidas[partidaId].estadio = estadio

                    # Define o horario em minutos desde a meia noite
                    horas, minutos = horario.split(':')
                    Partidas[partidaId].horarioInt = int(horas) * 60 + int(minutos)

                    Partidas[partidaId].horas = horas

                    ihoras = int(horas)
                    if ihoras >= 0 and ihoras < 6:
                        Partidas[partidaId].periodo = 'Madrugada'
                    elif ihoras >= 6 and ihoras < 12:
                        Partidas[partidaId].periodo = 'Manha'
                    elif ihoras >= 12 and ihoras < 18:
                        Partidas[partidaId].periodo = 'Tarde'
                    elif ihoras >= 18:
                        Partidas[partidaId].periodo = 'Noite'

                    # Extrai os times
                    times = extrai1Valor(linhas[start + 3], 'Jogo')
                    time1, time2 = times.split(' X ')

                    nome1, estado1 = time1.split(' / ')
                    casaId = adicionaTime(Times, nome1, estado1)
                
                    nome2, estado2 = time2.split(' / ')
                    visitanteId = adicionaTime(Times, nome2, estado2)

                    # Complementa a tabela de partidas
                    Partidas[partidaId].casa = casaId
                    Partidas[partidaId].visitante = visitanteId

                if pagina_num == 1:

                    num_linhas = len(linhas)

                    # Extrai cartoes amarelos
                    current = 0
                    while current < num_linhas and linhas[current] != 'Cartões Amarelos':
                        current += 1

                    if current < num_linhas and linhas[current] == 'Cartões Amarelos':
                        current += 1

                        minuto = ''
                        tempo = 0
                        jogadorId = -1
                        timeId = -1

                        # Enquanto nao se encontra na secao de cartoes vermelhos
                        while current < num_linhas and linhas[current] != 'Cartões Vermelhos':

                            # Busca o time
                            timeId = buscaTime(linhas[current], Times)

                            if(timeId != None):

                                # Remove o nome do time da linha e entao extrai o resto
                                linhaSemTime = linhas[current].replace(" " + Times[timeId].nome + "/" + Times[timeId].estado, "")

                                match = re.search(r"1T|2T|INT", linhaSemTime)
                                if match:
                                    minuto = linhaSemTime[0:match.start() - 1]
                                    tempo = linhaSemTime[match.start():match.end()]

                                    resto = linhaSemTime[match.end():len(linhaSemTime)]

                                    if resto[0:2] == "AT" or resto[0:2] == "TC":
                                        numero = resto[0:2]
                                        nome = resto[2:len(resto)]
                                    else:
                                        numero = "".join([c for c in resto if c.isdigit()])
                                        nome = resto[len(numero):]

                                    if minuto[0:1] == "+":
                                        acrescimo = 45 + int(minuto[1:3])
                                        minuto = str(acrescimo) + ":00"

                                    itempo = 0
                                    if tempo == "1T":
                                        itempo = 1
                                    elif tempo == "INT":
                                        itempo = 1
                                        minuto = "45:00"
                                    elif tempo == "2T":
                                        itempo = 2
                                    
                                    # Cria o jogador e o cartao amarelo
                                    jogadorId = adicionaJogador(Jogadores, nome, numero)
                                    amareloId = adicionaAmarelo(Amarelos, campeonatoId, rodada, partidaId, timeId, jogadorId, itempo, minuto)

                                    # Complementa tabela de amarelos
                                    Amarelos[amareloId].jogador = Jogadores[jogadorId].nome
                                    Amarelos[amareloId].time = Times[timeId].nome

                                    sMinutos, sSegundos = minuto.split(':')
                                    Amarelos[amareloId].horarioInt = Partidas[partidaId].horarioInt + (int(sMinutos)) + ((itempo - 1) * 60)
                                    Amarelos[amareloId].horarioString = f"{Amarelos[amareloId].horarioInt // 60:02}:{Amarelos[amareloId].horarioInt % 60:02}"

                                    Partidas[partidaId].numAmarelos = Partidas[partidaId].numAmarelos + 1

                            current += 1

                        if current < num_linhas and linhas[current] == 'Cartões Vermelhos':

                            current = current + 1

                            if current < num_linhas and linhas[current] == 'NÃO HOUVE EXPULSÕES':
                                pula = 1
                            elif current == num_linhas:
                                print("Terminou")
                            else:

                                while current < num_linhas:

                                    current = current + 1
                                    if current < num_linhas:

                                        # Busca o time
                                        timeId = buscaTime(linhas[current], Times)

                                        if timeId != None:

                                            # Remove o nome do time da linha e entao extrai o resto
                                            linhaSemTime = linhas[current].replace(" " + Times[timeId].nome + "/" + Times[timeId].estado, "")

                                            match = re.search(r"1T|2T|INT", linhaSemTime)
                                            if match:

                                                minuto = linhaSemTime[0:match.start() - 1]
                                                #print('minuto')
                                                #print(minuto)

                                                tempo = linhaSemTime[match.start():match.end()]

                                                resto = linhaSemTime[match.end():len(linhaSemTime)]

                                                if resto[0:2] == "AT" or resto[0:2] == "TC":
                                                    numero = resto[0:2]
                                                    nome = resto[2:len(resto)]
                                                else:
                                                    numero = "".join([c for c in resto if c.isdigit()])
                                                    nome = resto[len(numero):]

                                                if minuto[0:1] == "+":
                                                    if minuto[3:4] == ":":
                                                        acrescimo = 45 + int(minuto[1:3])
                                                        minuto = str(acrescimo) + ":00"
                                                    elif minuto [2:3] == ":":
                                                        acrescimo = 45 + int(minuto[1:2])
                                                        minuto = str(acrescimo) + ":00"

                                                itempo = 0

                                                if tempo == "1T":
                                                    itempo = 1
                                                elif tempo == "INT":
                                                    itempo = 1
                                                    minuto = "45:00"
                                                elif tempo == "2T":
                                                    itempo = 2
                                    
                                                # Cria o jogador e o cartao vermelho
                                                jogadorId = adicionaJogador(Jogadores, nome, numero)
                                                vermelhoId = adicionaVermelho(Vermelhos, campeonatoId, rodada, partidaId, timeId, jogadorId, itempo, minuto)

                                                # Complementa tabela de vermelhos
                                                Vermelhos[vermelhoId].jogador = Jogadores[jogadorId].nome
                                                Vermelhos[vermelhoId].time = Times[timeId].nome

                                                sMinutos, sSegundos = minuto.split(':')
                                                Vermelhos[vermelhoId].horarioInt = Partidas[partidaId].horarioInt + (int(sMinutos)) + ((itempo - 1) * 60)
                                                Vermelhos[vermelhoId].horarioString = f"{Vermelhos[vermelhoId].horarioInt // 60:02}:{Vermelhos[vermelhoId].horarioInt % 60:02}"

                                                Partidas[partidaId].numVermelhos = Partidas[partidaId].numVermelhos + 1



                        

                """
                for l in range(num_linhas):
                    if(linhas[l] == 'Gols'):
                        if(linhas[l + 1] != 'NÃO HOUVE MARCADORES'):
                            current = l + 2
                            while(linhas[current] != 'NR = Normal | PN = Pênalti | CT = Contra | FT = Falta'):
                                #print(linhas[current])
                                adicionaGol(Gols, 0, 0, 0)
                                current += 1
                """

    imprimeCSV(campeonato, "amarelos", Amarelos)

    if len(Vermelhos) > 0:
        imprimeCSV(campeonato, "vermelhos", Vermelhos)

    imprimeCSV(campeonato, "arbitros", Arbitros)
    #imprimeCSV(campeonato, "gols", Gols)
    imprimeCSV(campeonato, "jogadores", Jogadores)
    imprimeCSV(campeonato, "partidas", Partidas)
    imprimeCSV(campeonato, "times", Times)
    imprimeCSV(campeonato, "campeonatos", Campeonatos)

    basicaDescribe(campeonato, "numAmarelos")
    print("...")
    basicaDescribe(campeonato, "numVermelhos")