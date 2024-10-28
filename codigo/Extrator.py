# -*- coding: utf-8 -*-
# @project Brasileirao
# @description Classe extratora de valores
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

def extrai1Valor(linha, chave1):

    item1 = linha.split(chave1 + ': ', 1)

    return item1[1]

def extrai2Valores(linha, chave1, chave2):

    item2 = linha.split(' ' + chave2 + ': ', 1)
    item1 = item2[0].split(chave1 + ': ', 1)

    return item1[1], item2[1]

def extrai3Valores(linha, chave1, chave2, chave3):

    item3 = linha.split(' ' + chave3 + ': ', 1)
    item2 = item3[0].split(' ' + chave2 + ': ', 1)
    item1 = item2[0].split(chave1 + ': ', 1)

    return item1[1], item2[1], item3[1]
