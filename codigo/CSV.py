# @project Brasileirao
# @description Classe que imprime em CSV
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/29

import csv

def imprimeCSV(nome, objetos):

    with open("csv/" + nome + ".csv", mode="w", newline="") as arquivo_csv:
        colunas = vars(objetos[0]).keys()
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
        escritor.writeheader()
        for objeto in objetos:
            escritor.writerow(vars(objeto))