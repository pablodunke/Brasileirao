# @project Brasileirao
# @description Classe que representa as partidas
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

class Partida:
    def __init__(self, pid, pnome, prodada):
        self.id = pid
        self.nome = pnome
        self.rodada = prodada
        self.arbitroId = -1

def adicionarPartida(partidas, pnome, prodada):
    partidas.append(Partida(len(partidas), pnome, prodada))
    return len(partidas) - 1

