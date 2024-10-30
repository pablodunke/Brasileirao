# -*- coding: utf-8 -*-
# @project Brasileirao
# @description Classe que exibe os graficos
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/30

import pandas as pd
import matplotlib.pyplot as plt

def exibeGraficos():



    """
    df = pd.read_csv('../csv/amarelos.csv', encoding='utf-8')
    # Passo 2: Contar as ocorrências por horarioInt
    # Contando as ocorrências de cada minuto
    ocorrencias_por_horario = df['horarioString'].value_counts().sort_index()

    # Passo 3: Garantir que todos os minutos de 0 a 1439 estejam presentes no gráfico
    # Cria um índice completo de 0 a 1439 e reindexa as ocorrências
    ocorrencias_por_horario = ocorrencias_por_horario.reindex(range(1440), fill_value=0)

    # Passo 4: Criar o gráfico
    plt.figure(figsize=(15, 6))
    ocorrencias_por_horario.plot(kind='bar', color='lightgreen')
    plt.title('Quantidade de Ocorrências por Horário (minutos)')
    plt.xlabel('Minuto do Jogo')
    plt.ylabel('Quantidade de Ocorrências')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    # Exibir o gráfico
    plt.tight_layout()
    plt.show()
    """

    """
    df = pd.read_csv('../csv/amarelos.csv', encoding='utf-8')

    # Agrupar os dados pela coluna 'tempo' e contar a quantidade de cartões
    cartoes_por_tempo = df.groupby('minutoGeral').size()

    # Plotar o gráfico
    plt.figure(figsize=(10, 6))
    cartoes_por_tempo.plot(kind='bar', color='skyblue')
    plt.title('Quantidade de Cartões por Tempo')
    plt.xlabel('Tempo')
    plt.ylabel('Quantidade de Cartões')
    plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x para melhor legibilidade
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Mostrar o gráfico
    plt.tight_layout()  # Ajusta o layout para evitar sobreposição
    plt.show()
    """


    """
    cartoes_por_time = df['time'].value_counts()

    # Passo 3: Criar o gráfico
    plt.figure(figsize=(10, 6))
    cartoes_por_time.plot(kind='bar', color='skyblue')
    plt.title('Quantidade de Cartões por Time')
    plt.xlabel('Time')
    plt.ylabel('Quantidade de Cartões')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    # Exibir o gráfico
    plt.tight_layout()
    plt.show()
    """


    # Passo 1: Ler o arquivo CSV
    df = pd.read_csv('../csv/amarelos.csv', encoding='utf-8')

    # Passo 2: Contar as ocorrências por horarioInt
    # Contando as ocorrências de cada minuto
    ocorrencias_por_horario = df['horarioInt'].value_counts().sort_index()

    # Passo 3: Garantir que todos os minutos de 0 a 1439 estejam presentes no gráfico
    # Cria um índice completo de 0 a 1439 e reindexa as ocorrências
    ocorrencias_por_horario = ocorrencias_por_horario.reindex(range(1440), fill_value=0)

    # Passo 4: Criar o gráfico
    plt.figure(figsize=(15, 6))
    ocorrencias_por_horario.plot(kind='bar', color='lightgreen')
    plt.title('Quantidade de Ocorrências por Horário (minutos)')
    plt.xlabel('Minuto do Jogo')
    plt.ylabel('Quantidade de Ocorrências')

    # Formatar o eixo x para mostrar HH:MM
    plt.xticks(ticks=range(0, 1440, 5), 
               labels=[f"{i//60:02}:{i%60:02}" for i in range(0, 1440, 5)], 
               rotation=45)

    plt.grid(axis='y')

    # Exibir o gráfico
    plt.tight_layout()
    plt.show()