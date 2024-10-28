# -*- coding: utf-8 -*-
# @project Brasileirao
# @description Classe principal do projeto
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

import os
import PyPDF2

from codigo.Arbitro             import Arbitro,             adicionarArbitro
from codigo.Campeonato          import Campeonato,          adicionarCampeonato
from codigo.Partida             import Partida,             adicionarPartida
from codigo.Time                import Time,                adicionarTime

from codigo.Extrator            import                      extrai1Valor, extrai2Valores, extrai3Valores

Arbitros = []
Campeonatos = []
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

            if(pagina_num == 0):
                pagina = pdf_reader.pages[pagina_num]
                texto = pagina.extract_text()

                linhas = texto.split('\n')
            
                #print(linhas[5])

                jogo = extrai1Valor(linhas[1], 'Jogo')
                camp, rodada = extrai2Valores(linhas[3], 'Campeonato', 'Rodada')
                data, horario, estadio = extrai3Valores(linhas[5], 'Data', 'Horário', 'Estádio')

                arbi = extrai1Valor(linhas[7], 'Arbitro')
                aid = adicionarArbitro(Arbitros, arbi)

                cid = adicionarCampeonato(Campeonatos, camp)
                pid = adicionarPartida(Partidas, jogo, rodada)

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


for arbitro in Arbitros:
    print(arbitro.nome + ' teve ' + str(arbitro.jogos) + ' jogos')

##for partida in Partidas:
  ##  print("A partida " + partida.nome + " teve como arbitro o(a) " + Arbitros[partida.arbitroId].nome + ".")

