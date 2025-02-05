# @project Brasileirao
# @description Classe que representa os cartoes amarelos nas partidas
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/29

class Amarelo:
    def __init__(self, pId, pCampeonatoId, pRodada, pPartidaId, pTimeId, pJogadorId, pTempo, pMinuto):
        self.id = pId
        self.campeonatoId = pCampeonatoId
        self.rodada = pRodada.strip()
        self.partidaId = pPartidaId
        self.timeId = pTimeId
        self.jogadorId = pJogadorId
        self.tempo = pTempo
        self.minuto = pMinuto

        minuto = pMinuto[:2]
        if pMinuto[1:2] == ":":
            minuto = pMinuto[:1]

        self.minutoGeral = int(minuto) + ((pTempo - 1) * 45)

def adicionaAmarelo(amarelos, pCampeonatoId, pRodada, pPartidaId, pTimeId, pJogadorId, pTempo, pMinuto):
    amarelos.append(Amarelo(len(amarelos), pCampeonatoId, pRodada, pPartidaId, pTimeId, pJogadorId, pTempo, pMinuto))
    return len(amarelos) - 1

def imprimeAmarelos(amarelos, jogadores):
    for amarelo in amarelos:
        print('Amarelo do jogador ' + jogadores[amarelo.jogadorId].nome + ".")
