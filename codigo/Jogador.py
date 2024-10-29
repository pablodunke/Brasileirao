# @project Brasileirao
# @description Classe que representa os jogadores dos times
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

class Jogador:
    def __init__(self, pid, pnome, pcbf):
        self.id = pid
        self.nome = pnome
        self.cbf = pcbf
        #self.timeId = ptime

def adicionaJogador(jogadores, pnome, pcbf):
    jogadores.append(Jogador(len(jogadores), pnome, pcbf))
    return len(jogadores) - 1

def imprimeJogadores(jogadores):
    for jogador in jogadores:
        print('O jogador ' + jogador.nome + " .")
