# @project Brasileirao
# @description Classe que representa os gols nas partidas
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

class Gol:
    def __init__(self, pid, ppartidaId, ptimeId, pjogadorId):
        self.id = pid
        self.partidaId = ppartidaId
        self.timeId = ptimeId
        self.jogadorId = pjogadorId

def adicionaGol(gols, ppartidaId, ptimeId, pjogadorId):
    gols.append(Gol(len(gols), ppartidaId, ptimeId, pjogadorId))
    return len(gols) - 1

def imprimeGols(gols, partidas, times, jogadores):
    for gol in gols:
        print('Gol do jogador ' + jogadores[gol.jogadorId].nome + ".")
