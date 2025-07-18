# @project Brasileirao
# @description Classe que representa os cartoes vermelhos nas partidas
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/29

class Vermelho:
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

def adicionaVermelho(vermelhos, pCampeonatoId, pRodada, pPartidaId, pTimeId, pJogadorId, pTempo, pMinuto):
    vermelhos.append(Vermelho(len(vermelhos), pCampeonatoId, pRodada, pPartidaId, pTimeId, pJogadorId, pTempo, pMinuto))
    return len(vermelhos) - 1

def imprimeVermelhos(vermelhos, jogadores):
    for vermelho in vermelhos:
        print('Vermelho do jogador ' + jogadores[vermelho.jogadorId].nome + ".")
