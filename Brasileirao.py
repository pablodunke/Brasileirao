# -*- coding: utf-8 -*-
# @project Brasileirao
# @description Classe principal do projeto
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

from codigo.ConverteCSV         import              converteCSVs
from codigo.Graficos            import              exibeGraficos
from codigo.Selenium            import              baixaPDFs

from analise.Basico             import              basicoDescribe

#for rodada in range(1, 39):
    #baixaPDFs('2021', 'Campeonato Brasileiro - Série A', str(rodada))

#converteCSVs()
#exibeGraficos()
basicoDescribe()