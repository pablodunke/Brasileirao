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
from codigo.Time                import Time,                adicionaTime, imprimeTimes

from codigo.CSV                 import                      imprimeCSV
from codigo.Extrator            import                      extrai1Valor, extrai2Valores, extrai3Valores

Amarelos = []
Vermelhos = []

Arbitros = []
Campeonatos = []
Gols = []
Jogadores = []
Partidas = []
Times = []

def buscaTime(linha, times):

    for time in times:

        if linha.endswith(time.nome):
            return time.id

        elif re.search(r"\b" + re.escape(time.nome) + r"\b", linha):
            return time.id

    return None

def converteCSVs():
    pasta = 'dados'
    arquivos = os.listdir(pasta)
    for pdf in [arquivo for arquivo in arquivos if arquivo.endswith('.pdf')]:

        caminho_pdf = os.path.join(pasta, pdf)
        with open(caminho_pdf, 'rb') as pdf_file:

            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_paginas = len(pdf_reader.pages)

            partidaId = -1
            for pagina_num in range(num_paginas):

                pagina = pdf_reader.pages[pagina_num]
                texto = pagina.extract_text()
                linhas = texto.split('\n')

                if(pagina_num == 0):
                
                    # Extrai as informacoes iniciais
                    cbf = extrai1Valor(linhas[1], 'Jogo')
                    camp, rodada = extrai2Valores(linhas[3], 'Campeonato', 'Rodada')
                    data, horario, estadio = extrai3Valores(linhas[5], 'Data', 'Horário', 'Estádio')

                    # Extrai e cria o arbitro
                    arbitroString = extrai1Valor(linhas[7], 'Arbitro')
                    arbitroGrupo = re.match(r"(.+?)\s\((.+?)\s\/\s([A-Z]{2})\)", arbitroString)
                    arbitroNome = arbitroGrupo.group(1)
                    arbitroCredencial = arbitroGrupo.group(2)
                    arbitroEstado = arbitroGrupo.group(3)
                    arbitroId = adicionaArbitro(Arbitros, arbitroNome, arbitroCredencial, arbitroEstado)

                    # Cria o campeonato
                    campeonatoId = adicionaCampeonato(Campeonatos, camp)

                    # Cria e preenche a partida
                    jogo = extrai1Valor(linhas[1], 'Jogo')
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

                    # Extrai os times
                    times = extrai1Valor(linhas[4], 'Jogo')
                    time1, time2 = times.split(' X ')

                    nome1, estado1 = time1.split(' / ')
                    casaId = adicionaTime(Times, nome1, estado1)
                
                    nome2, estado2 = time2.split(' / ')
                    visitanteId = adicionaTime(Times, nome2, estado2)

                    # Complementa a tabela de partidas
                    Partidas[partidaId].casa = casaId
                    Partidas[partidaId].visitante = visitanteId

                if(pagina_num == 1):

                    num_linhas = len(linhas)

                    # Extrai cartoes amarelos
                    current = 0
                    while(current < num_linhas and linhas[current] != 'Cartões Amarelos'):
                        current += 1

                    if(current < num_linhas and linhas[current] == 'Cartões Amarelos'):
                        current += 1

                        minuto = ''
                        tempo = 0
                        jogadorId = -1
                        timeId = -1

                        # Enquanto nao se encontra na secao de cartoes vermelhos
                        while(current < num_linhas and linhas[current] != 'Cartões Vermelhos'):

                            # Busca o time
                            timeId = buscaTime(linhas[current], Times)
                            if(timeId != None):

                                # Remove o nome do time da linha e entao extrai o resto
                                recorte = linhas[current].replace(Times[timeId].nome, "").strip()
                                match = re.match(r"(\d{2}:\d{2})\s*(\dT)(\d+)([A-Za-z\s]+)", recorte)

                                if match:
                                    minuto = match.group(1)
                                    tempo = match.group(2)
                                    numero = match.group(3)
                                    nome = match.group(4).strip()

                                    # Cria o jogador e o cartao amarelo
                                    jogadorId = adicionaJogador(Jogadores, nome, numero)
                                    amareloId = adicionaAmarelo(Amarelos, partidaId, timeId, jogadorId, int(tempo[0]), minuto)

                                    # Define o horario em minutos desde a meia noite
                                    #horas, minutos = horario.split(':')
                                    #Amarelos[amareloId].horarioInt = int(horas) * 60 + int(minutos)

                                    # Complementa tabela de amarelos
                                    Amarelos[amareloId].jogador = Jogadores[jogadorId].nome
                                    Amarelos[amareloId].time = Times[timeId].nome

                                    sMinutos, sSegundos = minuto.split(':')
                                    Amarelos[amareloId].horarioInt = Partidas[partidaId].horarioInt + (int(sMinutos)) + ((int(tempo[0]) - 1) * 60)
                                    Amarelos[amareloId].horarioString = f"{Amarelos[amareloId].horarioInt // 60:02}:{Amarelos[amareloId].horarioInt % 60:02}"

                            current += 1
                 
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

    #imprimeArbitros(Arbitros)
    #imprimeGols(Gols, Partidas, Times, Jogadores)
    #imprimeJogadores(Jogadores)
    #imprimePartidas(Partidas, Arbitros)
    #imprimeHorarioPartidas(Partidas)
    #imprimeTimes(Times)

    imprimeCSV("amarelos", Amarelos)
    imprimeCSV("arbitros", Arbitros)
    #imprimeCSV("gols", Gols)
    imprimeCSV("jogadores", Jogadores)
    imprimeCSV("partidas", Partidas)
    imprimeCSV("times", Times)