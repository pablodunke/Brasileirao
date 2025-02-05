# -*- coding: utf-8 -*-
# @project Brasileirao
# @description Classe principal do projeto
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

import sys

from codigo.ConverteCSV         import              converteCSVs
from codigo.Graficos            import              exibeGraficos, exibeCampeonatos
from codigo.Selenium            import              baixaPDFs

from analise.Basica             import              basicaDescribe, basicaHistograma, basicaRelacionamento, basicaPorPeriodo
from analise.Estatistica        import              basicaNormalidade, basicaAnova, basicaKruskal, basicaPermutacao, basicaRegressao, basicaPoisson, powerAnalysis

if len(sys.argv) < 2:
    print("Faltou o argumento!")

elif sys.argv[1] == "baixaPDF":
    if len(sys.argv) < 6:
        print("Formato é: python Brasileirao.py baixaPDF Campeonato_Brasileiro_-_Série_A 2021 1 38")
    else:
        campeonato = sys.argv[2]
        ano = sys.argv[3]
        primeira = int(sys.argv[4])
        ultima = int(sys.argv[5]) + 1

        for rodada in range(primeira, ultima):
            baixaPDFs(ano, campeonato, str(rodada))

elif sys.argv[1] == "converteCSVs":
    converteCSVs(sys.argv[2])
elif sys.argv[1] == "exibeGraficos":
    exibeGraficos()
elif sys.argv[1] == "exibeCampeonatos":
    exibeCampeonatos(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "basicaDescribe":
    basicaDescribe(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "basicaHistograma":
    basicaHistograma(sys.argv[2])
elif sys.argv[1] == "basicaRelacionamento":
    basicaRelacionamento(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "basicaPorPeriodo":
    basicaPorPeriodo(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "basicaNormalidade":
    basicaNormalidade(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "basicaAnova":
    basicaAnova(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "basicaKruskal":
    basicaKruskal(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "basicaPermutacao":
    basicaPermutacao(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "basicaRegressao":
    basicaRegressao(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "basicaPoisson":
    basicaPoisson(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "powerAnalysis":
    powerAnalysis(sys.argv[2], sys.argv[3])
else:
    print("Parâmetro não encontrado")