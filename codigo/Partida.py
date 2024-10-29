# @project Brasileirao
# @description Classe que representa as partidas
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

class Partida:
    def __init__(self, pid, pnome):
        self.id = pid
        self.nome = pnome
        self.campeonatoId = -1
        self.arbitroId = -1
        self.rodada = -1
        self.data = ''
        self.horario = ''
        self.horarioInt = -1
        self.estadio = ''
        self.casa = ''
        self.visitante = ''

def adicionaPartida(partidas, pnome):
    partidas.append(Partida(len(partidas), pnome))
    return len(partidas) - 1

def imprimePartidas(partidas, arbitros):
    for partida in partidas:
        print('A partida ' + partida.nome + " teve como arbitro o(a) " + arbitros[partida.arbitroId].nome + ".")

def imprimeHorarioPartidas(partidas):
    for partida in partidas:
        print('A partida ' + partida.nome + " comecou as " + partida.horario + " (" + str(partida.horarioInt) + ")")