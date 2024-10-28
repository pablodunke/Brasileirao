# @project Brasileirao
# @description Classe que representa os arbitros das partidas
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

class Arbitro:
    def __init__(self, pid, pnome):
        self.id = pid
        self.nome = pnome
        self.jogos = 1

def adicionarArbitro(arbitros, nome):
    for arbitro in arbitros:
        if arbitro.nome == nome:
            arbitro.jogos += 1
            return arbitro.id

    arbitros.append(Arbitro(len(arbitros), nome))
    return len(arbitros) - 1