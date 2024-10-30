# -*- coding: utf-8 -*-
# @project Brasileirao
# @description Classe que baixa os PDFs
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/30

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def baixaPDFs():

    download_dir = "../download"

    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }

    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)

    url = 'https://portaldegovernanca.cbf.com.br/documentos-da-partida'
    driver.get(url)

    # Espera e seleciona a primeira opção
    wait = WebDriverWait(driver, 10)
    select1 = wait.until(EC.presence_of_element_located((By.ID, 'ano')))
    Select(select1).select_by_visible_text('2024')
    sleep(2)

    # Espera e seleciona a segunda opção
    select2 = wait.until(EC.presence_of_element_located((By.ID, 'campeonato')))
    Select(select2).select_by_visible_text('Campeonato Brasileiro - Série A')
    sleep(2)

    # Espera e seleciona a terceira opção
    select3 = wait.until(EC.presence_of_element_located((By.ID, 'rodada')))
    Select(select3).select_by_visible_text('22')
    sleep(2)

    # Clica no link para iniciar o download
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Súmula')))
    print(link)
    sleep(2)
    link.click()

    # driver.quit()