# @project Brasileirao
# @description Classe que representa os arbitros das partidas
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

class Arbitro:
    def __init__(self, pid, pnome):
        self.id = pid
        self.nome = pnome
        self.jogos = 1

def adicionaArbitro(arbitros, nome):
    for arbitro in arbitros:
        if arbitro.nome == nome:
            arbitro.jogos += 1
            return arbitro.id

    arbitros.append(Arbitro(len(arbitros), nome))
    return len(arbitros) - 1

def imprimeArbitros(arbitros):
    for arbitro in arbitros:
        print('O arbitro ' + arbitro.nome + ' teve ' + str(arbitro.jogos) + ' jogos')