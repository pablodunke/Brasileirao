# -*- coding: utf-8 -*-
# @project Brasileirao
# @description Classe que baixa os PDFs
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/30

import os
import requests
from io import BytesIO
from PyPDF2 import PdfReader
from selenium import webdriver
from selenium.webdriver.common.by       import      By
from selenium.webdriver.chrome.service  import      Service
from selenium.webdriver.support.ui      import      Select
from selenium.webdriver.support.ui      import      WebDriverWait
from selenium.webdriver.support         import      expected_conditions as EC
from time import sleep

from codigo.Extrator                    import      extrai1Valor, extrai2Valores, extrai3Valores

def baixaPDFs(pAno, pCampeonato, pRodada):

    pCampeonato = pCampeonato.replace("_", " ")

    chrome_options = webdriver.ChromeOptions()

    # Caminho para o chromedriver no cache
    driver_path = r"C:\Users\Pablo\.cache\selenium\chromedriver\win64\131.0.6778.85\chromedriver.exe"

    # Configurando o serviço com o caminho do chromedriver
    service = Service(driver_path)

    # Iniciando o WebDriver com o serviço configurado
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = 'https://portaldegovernanca.cbf.com.br/documentos-da-partida'
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    # Seleciona o ano
    select1 = wait.until(EC.presence_of_element_located((By.ID, 'ano')))
    Select(select1).select_by_visible_text(pAno)
    sleep(1)

    # Seleciona o campeonato
    select2 = wait.until(EC.presence_of_element_located((By.ID, 'campeonato')))
    Select(select2).select_by_visible_text(pCampeonato)
    sleep(1)

    # Seleciona a rodada
    select3 = wait.until(EC.presence_of_element_located((By.ID, 'rodada')))
    Select(select3).select_by_visible_text(pRodada)
    sleep(1)

    # Pega o link
    #links = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Súmula')))
    links = driver.find_elements(By.LINK_TEXT, 'Súmula')
    sleep(1)

    for link in links:

        pdf_url = link.get_attribute("href")
        print(pdf_url)

        if(pdf_url != None):

            response = requests.get(pdf_url)
            pdf_data = BytesIO(response.content)

            pdf_reader = PdfReader(pdf_data)

            first_page = pdf_reader.pages[0]
            first_page_text = first_page.extract_text()
            linhas = first_page_text.split('\n')

            start = 0
            while linhas[start][0:5] != "Jogo:":
                start = start + 1

            jogo = linhas[start].split(' CBF')[0].split('Jogo: ')[1]
            srodada = "{:03}".format(int(jogo))

            times = extrai1Valor(linhas[start + 3], 'Jogo')

            nome_arquivo = pCampeonato + ' ' + pAno + ' ' + srodada + ' - ' + times.replace(' / ', ' ')

            with open(f"download/{nome_arquivo}.pdf", "wb") as file:
                file.write(response.content)

    # driver.quit()