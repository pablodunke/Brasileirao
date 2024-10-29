# -*- coding: utf-8 -*-
# @project Brasileirao
# @description Classe principal do projeto
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

import os
import re
import PyPDF2

from codigo.Arbitro             import Arbitro,             adicionaArbitro, imprimeArbitros
from codigo.Campeonato          import Campeonato,          adicionaCampeonato
from codigo.Gol                 import Gol,                 adicionaGol, imprimeGols
from codigo.Jogador             import Jogador,             adicionaJogador, imprimeJogadores
from codigo.Partida             import Partida,             adicionaPartida, imprimePartidas, imprimeHorarioPartidas
from codigo.Time                import Time,                adicionaTime, imprimeTimes

from codigo.CSV                 import                      imprimeCSV
from codigo.Extrator            import                      extrai1Valor, extrai2Valores, extrai3Valores

Arbitros = []
Campeonatos = []
Gols = []
Jogadores = []
Partidas = []
Times = []

pasta = 'dados'
arquivos = os.listdir(pasta)
for pdf in [arquivo for arquivo in arquivos if arquivo.endswith('.pdf')]:

    caminho_pdf = os.path.join(pasta, pdf)
    with open(caminho_pdf, 'rb') as pdf_file:

        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_paginas = len(pdf_reader.pages)

        for pagina_num in range(num_paginas):

            pagina = pdf_reader.pages[pagina_num]
            texto = pagina.extract_text()
            linhas = texto.split('\n')
            
            #for linha in linhas:
                #print(linha)

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

                Partidas[partidaId].casa = casaId
                Partidas[partidaId].visitante = visitanteId

                #jid = adicionaJogador(Jogadores, 'Jorgi', '13')

                # Acessar chave e valor
                #key = key_value[0]
                #value = key_value[1] if len(key_value) > 1 else None

                #if(key == 'Jogo' and nomeado == False):
                
                   # nomeado = True
                #elif(key == 'Jogo'):
                    #h = 0
                #elif(key == 'Arbitro'):
                   # aid = adicionarArbitro(Arbitros, value)
                    #Partidas[pid].arbitroId = aid

            num_linhas = len(linhas)
            """
            for j in range(num_linhas):
                if(linhas[j] == 'Relação de Jogadores'):
                    current = j + 3
                    while(current < num_linhas and linhas[current] != 'T = Titular | R = Reserva | P = Profissional | A = Amador | (g) = Goleiro '):
                        if(linhas[current] != 'NºApelido Nome Completo T/RP/A CBF'):
                            name = linhas[current]
                            name = name.replace('ã', 'a')
                            name = name.replace('á', 'a')
                            name = name.replace('ç', 'c')
                            name = name.replace('é', 'e')
                            name = name.replace('ê', 'e')
                            name = name.replace('É', 'E')
                            name = name.replace('í', 'e')
                            name = name.replace('ñ', 'n')
                            name = name.replace('ó', 'o')
                            name = name.replace('ô', 'o')
                            name = name.replace('õ', 'o')
                            name = name.replace('ú', 'u')

                            partes = re.match(r"(\d+)([A-Za-z\s\.\(\)]+?)\s+[A-Za-z]*([A-Za-z\(\)]*P\d+)", name)
                            if(partes != None):
                                numero = partes.group(1)  # '79'
                                nome = partes.group(2).strip()  # 'Ronie Ronie Edmundo Carril'
                                codigo = partes.group(3)  # 'TP870027'
                                idj = adicionaJogador(Jogadores, nome, codigo)
                            else:
                                print('Falhou: ' + linhas[current])
                        current += 1

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

imprimeCSV("arbitros", Arbitros)
#imprimeCSV("gols", Gols)
#imprimeCSV("jogadores", Jogadores)
imprimeCSV("partidas", Partidas)
imprimeCSV("times", Times)

