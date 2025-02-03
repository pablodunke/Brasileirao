# @project Brasileirao
# @description Classe que faz a analise basica
# @createdBy Pablo Giovani Dunke
# @createdDate 2025/01/31

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from codigo.Impressao           import                      imprimeDado

def basicaDescribe(pasta, coluna):

    df = pd.read_csv("output/" + pasta + "/partidas.csv")

    imprimeDado("output/" + pasta, coluna, "Describe")
    imprimeDado("output/" + pasta, coluna, df[coluna].describe().to_string())

    imprimeDado("output/" + pasta, coluna, 'Sem elementos:')
    imprimeDado("output/" + pasta, coluna, str(df[df[coluna] == 0].shape[0]))

    media = df.groupby("horas")[coluna].mean()
    imprimeDado("output/" + pasta, coluna, 'Média:')
    imprimeDado("output/" + pasta, coluna, str(media))

    count = df.groupby("horas")[coluna].count()
    imprimeDado("output/" + pasta, coluna, 'Total:')
    imprimeDado("output/" + pasta, coluna, str(count))

def basicaHistograma(pasta):

    df = pd.read_csv("output/" + pasta + "/partidas.csv")
    #df['horas'] = pd.to_datetime(df['horas'], format='%H:%M').dt.hour

    plt.hist(df['horas'], bins=10, edgecolor='black')
    plt.xlabel('Horário de início do jogo')
    plt.ylabel('Quantidade de partidas')
    plt.title('Distribuição')
    plt.show()

def basicaRelacionamento(pasta, coluna):

    df = pd.read_csv("output/" + pasta + "/partidas.csv")

    plt.scatter(df['horas'], df[coluna], alpha=0.5)
    plt.xlabel('Horário de início do jogo')
    plt.ylabel('Quantidade de cartões')
    plt.title('Cartões por horário do jogo')
    plt.show()

def basicaPorPeriodo(pasta, coluna):

    df = pd.read_csv("output/" + pasta + "/partidas.csv")

    df['periodo'] = pd.cut(df['horarioInt'], bins=[0, 12, 18, 24], labels=['Manha', 'Tarde', 'Noite'])

    print(df.groupby('periodo')[coluna].mean())

    sns.boxplot(x=df['periodo'], y=df[coluna])
    plt.xlabel('Periodo do dia')
    plt.ylabel('Cartoes amarelos')
    plt.title('Distribuicao de cartoes por periodo do dia')
    plt.show()