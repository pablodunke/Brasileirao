# @project Brasileirao
# @description Classe que representa os gols nas partidas
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

class Gol:
    def __init__(self, pid, pnome, prodada):
        self.id = pid
        self.nome = pnome
        #self.rodada = prodada
        #self.arbitroId = -1

def adicionaGol(gols, pnome, prodada):
    gols.append(Gol(len(gols), pnome, prodada))
    return len(gols) - 1

def imprimeGols(gols):
    for gol in gols:
        print('Gol ' + gol.nome + ".")
