# -*- coding: utf-8 -*-
import PyPDF2

# Abre o arquivo PDF em modo de leitura bin�ria
with open("211 - Internacional x Athletico.pdf", "rb") as pdf_file:
    # Cria um objeto PDF Reader
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Verifica o n�mero de p�ginas
    num_paginas = len(pdf_reader.pages)
    print(f"Total de paginas: {num_paginas}")
    
    # Extrai texto de cada p�gina
    for pagina_num in range(num_paginas):
        pagina = pdf_reader.pages[pagina_num]
        texto = pagina.extract_text()
        print({texto})