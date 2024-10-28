# -*- coding: utf-8 -*-
# @project Brasileirao
# @description Classe principal do projeto
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

import os
import PyPDF2

from banco.Arbitro import Arbitro, adicionarArbitro
from banco.Partida import Partida, adicionarPartida

pasta = "dados"
arquivos = os.listdir(pasta)

pdfs = [arquivo for arquivo in arquivos if arquivo.endswith('.pdf')]

#print("Brasileirao")

#arbitro = Arbitro("Maria")

#print(arbitro.nome)

Arbitros = []
Partidas = []

for pdf in pdfs:

    caminho_pdf = os.path.join(pasta, pdf)
    with open(caminho_pdf, "rb") as pdf_file:

        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_paginas = len(pdf_reader.pages)

        for pagina_num in range(num_paginas):

            pagina = pdf_reader.pages[pagina_num]
            texto = pagina.extract_text()

            linhas = texto.split('\n')

            for linha in linhas:
                #print({linha})

                s_cleaned = linha.strip("{}'")

                key_value = s_cleaned.split(": ", 1)

                # Acessar chave e valor
                key = key_value[0]
                if(len(key_value) > 1):
                    value = key_value[1]

                if(key == 'Jogo'):
                    pid = adicionarPartida(Partidas, value)
                elif(key == 'Arbitro'):
                    aid = adicionarArbitro(Arbitros, value)
                    Partidas[pid].arbitroId = aid


##for arbitro in arbitros:
##    print(arbitro.nome + " teve " + str(arbitro.jogos) + " jogos")

for partida in Partidas:
    print("A partida " + partida.nome + " teve como arbitro o(a) " + Arbitros[partida.arbitroId].nome + ".")