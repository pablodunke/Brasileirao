# -*- coding: utf-8 -*-
# @project Brasileirao
# @description Classe principal do projeto
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

import os
import PyPDF2

from codigo.Arbitro             import Arbitro,             adicionaArbitro, imprimeArbitros
from codigo.Campeonato          import Campeonato,          adicionaCampeonato
from codigo.Gol                 import Gol,                 adicionaGol, imprimeGols
from codigo.Jogador             import Jogador,             adicionaJogador, imprimeJogadores
from codigo.Partida             import Partida,             adicionaPartida, imprimePartidas
from codigo.Time                import Time,                adicionaTime

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

            if(pagina_num == 0):
                
                cbf = extrai1Valor(linhas[1], 'Jogo')
                camp, rodada = extrai2Valores(linhas[3], 'Campeonato', 'Rodada')
                data, horario, estadio = extrai3Valores(linhas[5], 'Data', 'Horário', 'Estádio')

                arbi = extrai1Valor(linhas[7], 'Arbitro')
                arbitroId = adicionaArbitro(Arbitros, arbi)

                cid = adicionaCampeonato(Campeonatos, camp)

                jogo = extrai1Valor(linhas[4], 'Jogo')
                pid = adicionaPartida(Partidas, jogo, rodada)

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
            for l in range(num_linhas):
                if(linhas[l] == 'Gols'):
                    if(linhas[l + 1] != 'NÃO HOUVE MARCADORES'):
                        current = l + 2
                        while(linhas[current] != 'NR = Normal | PN = Pênalti | CT = Contra | FT = Falta'):
                            #print(linhas[current])
                            adicionaGol(Gols, linhas[current], 0)
                            current += 1




#imprimeArbitros(Arbitros)
imprimeGols(Gols)
#imprimePartidas(Partidas, Arbitros)

