# -*- coding: utf-8 -*-

from Arbitro import Arbitro

import PyPDF2

#print("Brasileirao")

#arbitro = Arbitro("Maria")

#print(arbitro.nome)

arbitros = []

with open("211 - Internacional x Athletico.pdf", "rb") as pdf_file:
    # Cria um objeto PDF Reader
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Verifica o número de páginas
    num_paginas = len(pdf_reader.pages)
    print(f"Total de paginas: {num_paginas}")
    print()
    
    # Extrai texto de cada página
    for pagina_num in range(num_paginas):

        pagina = pdf_reader.pages[pagina_num]
        texto = pagina.extract_text()

        linhas = texto.split('\n')

        for linha in linhas:
            #print({linha})

            s_cleaned = linha.strip("{}'")

            key_value = s_cleaned.split(": ", 1)  # O 1 garante que apenas a primeira ocorrência seja dividida

            # Acessar chave e valor
            key = key_value[0]
            if(len(key_value) > 1):
                value = key_value[1]

            if(key == 'Arbitro'):
                arbitros.append(Arbitro(value))

for arbitro in arbitros:
    print(arbitro.nome)

            