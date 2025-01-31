# @project Brasileirao
# @description Classe que faz a analise basica
# @createdBy Pablo Giovani Dunke
# @createdDate 2025/01/31

import pandas as pd

def basicoDescribe():
    df = pd.read_csv("csv/partidas.csv")
    print(df['numAmarelos'].describe())