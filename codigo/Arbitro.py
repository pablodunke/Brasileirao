# @project Brasileirao
# @description Classe que representa os arbitros das partidas
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

class Arbitro:
    def __init__(self, pid, pnome, pcredencial, pestado):
        self.id = pid
        self.nome = pnome
        self.credencial = pcredencial
        self.estado = pestado

def adicionaArbitro(arbitros, pnome, pcredencial, pestado):
    for arbitro in arbitros:
        if arbitro.nome == pnome:
            return arbitro.id

    arbitros.append(Arbitro(len(arbitros), pnome, pcredencial, pestado))
    return len(arbitros) - 1

def imprimeArbitros(arbitros):
    for arbitro in arbitros:
        print('O arbitro ' + arbitro.nome + ' teve ' + str(arbitro.jogos) + ' jogos')