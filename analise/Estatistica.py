# @project Brasileirao
# @description Classe que faz a analise basica
# @createdBy Pablo Giovani Dunke
# @createdDate 2025/01/31

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from scipy.stats import kruskal
from scipy.stats import f_oneway
from scipy.stats import permutation_test
from scipy.stats import shapiro

import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.power import FTestAnovaPower

def basicaNormalidade(pasta, coluna):

    df = pd.read_csv("output/" + pasta + "/partidas.csv")

    stat, p = shapiro(df[coluna])
    print(f'Teste de Shapiro-Wilk: p={p}')

    if p > 0.05:
        print("Os dados parecem seguir uma distribuicao normal.")
    else:
        print("Os dados nao seguem uma distribuicao normal.")

def basicaAnova(pasta, coluna):
    
    df = pd.read_csv("output/" + pasta + "/partidas.csv")
    """
    manha = df[df['periodo'] == 'Manha'][coluna]
    tarde = df[df['periodo'] == 'Tarde'][coluna]
    noite = df[df['periodo'] == 'Noite'][coluna]

    stat, p = f_oneway(manha, tarde, noite)
    print(f'Teste ANOVA: p={p}')

    if p < 0.05:
        print("Diferenca significativa entre os periodos.")
    else:
        print("Nenhuma diferenca significativa entre os periodos."

    """

    # Filtrar os dados para os horários específicos
    horarios = [11, 15, 16, 17, 18, 19, 20, 21]
    grupos = [df[df['horas'] == h][coluna] for h in horarios]

    # Teste ANOVA
    stat, p = f_oneway(*grupos)
    print(f'Teste ANOVA: p={p}')

    if p < 0.05:
        print("Há diferenças significativas entre os horários.")
    else:
        print("Nenhuma diferença significativa entre os horários.")

def basicaKruskal(pasta, coluna):
       
    df = pd.read_csv("output/" + pasta + "/partidas.csv")

    horarios = [11, 15, 16, 17, 18, 19, 20, 21]
    grupos = [df[df['horas'] == h][coluna] for h in horarios]

    stat, p = kruskal(*grupos)

    print(f'Teste Kruskal-Wallis: p={p}')

    if p < 0.05:
        print("Ha diferencas significativas entre os periodos.")
    else:
        print("Nenhuma diferenca significativa entre os periodos.")

def basicaPermutacao(pasta, coluna):

    df = pd.read_csv("output/" + pasta + "/partidas.csv")

    # Criar os grupos de cartões amarelos por hora
    grupos = [df[df["horas"] == h]["numAmarelos"].values for h in df["horas"].unique()]

    # Definir a estatística F manualmente
    def stat_func(*args):
        return f_oneway(*args).statistic  # Retorna apenas o valor F

    # Teste de permutação
    result = permutation_test(grupos, statistic=stat_func, permutation_type="independent")

    # Acessando os valores corretamente
    print(f"Estatística F: {result.statistic}")
    print(f"p-valor: {result.pvalue}")

    if result.pvalue < 0.05:
        print("Diferença significativa entre os horários!")
    else:
        print("Nenhuma diferença estatística entre os horários.")

def basicaRegressao(pasta, coluna):

    df = pd.read_csv("output/" + pasta + "/partidas.csv")

    # Regressão de Poisson (útil para contagens)
    modelo = smf.glm(coluna + " ~ C(horas)", data=df, family=sm.families.Poisson()).fit()
    print(modelo.summary())

def basicaPoisson(pasta, coluna):

    df = pd.read_csv("output/" + pasta + "/partidas.csv")

    # Criar o modelo usando 'numAmarelos' como variável dependente e 'horas' como explicativa
    modelo = smf.glm(coluna + " ~ C(horas)", data=df, family=sm.families.Poisson()).fit()

    # Exibir os resultados do modelo
    print('Resultado: ')
    print(modelo.summary())

    print('Média:')
    print(df[coluna].mean())
    print('Variança:')
    print(df[coluna].var())

def powerAnalysis(pasta, coluna):
       
    df = pd.read_csv("output/" + pasta + "/partidas.csv")

    horarios = [11, 15, 16, 17, 18, 19, 20, 21]
    grupos = [df[df['horas'] == h][coluna] for h in horarios]

    # Coletar o número de observações em cada grupo
    n_grupos = len(grupos)  # Você tem 6 horários diferentes
    n_amostras = np.mean([len(g) for g in grupos])  # Média de jogos por grupo
    effect_size = 0.25  # Tamanho de efeito moderado

    # Calcular poder do teste
    power_analysis = FTestAnovaPower()
    power = power_analysis.power(effect_size=effect_size, nobs=n_grupos * n_amostras, alpha=0.05)
    print(f"Poder do teste: {power:.2f}")

    if power < 0.8:
        print("A amostra pode ser pequena demais para detectar diferenças.")
    else:
        print("A amostra é suficiente para detectar diferenças, se existirem.")