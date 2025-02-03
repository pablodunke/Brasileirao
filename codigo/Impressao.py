# @project Brasileirao
# @description Classe que imprime em CSV
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/29

import os
import csv

def imprimeCSV(pasta, nome, objetos):

    with open("output/" + pasta + "/" + nome + ".csv", mode="w", newline="", encoding="utf-8") as arquivo_csv:
        colunas = vars(objetos[0]).keys()
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
        escritor.writeheader()
        for objeto in objetos:
            escritor.writerow(vars(objeto))

def imprimeDado(pasta, nome, string):

    caminho_arquivo = f"{pasta}/{nome}.txt"
    diretorio = os.path.dirname(caminho_arquivo)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(string + '\n')