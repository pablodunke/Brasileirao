# @project Brasileirao
# @description Classe que representa as partidas
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

class Partida:
    def __init__(self, pid, pnome):
        self.id = pid
        self.nome = pnome
        self.arbitroId = -1

def adicionarPartida(partidas, nome):
    partidas.append(Partida(len(partidas), nome))
    return len(partidas) - 1

