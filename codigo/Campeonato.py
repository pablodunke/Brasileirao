# @project Brasileirao
# @description Classe que representa o campeonato
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

class Campeonato:
    def __init__(self, pid, pnome):
        self.id = pid
        self.nome = pnome
        self.jogos = 1

def adicionaCampeonato(campeonatos, nome):
    for campeonato in campeonatos:
        if campeonato.nome == nome:
            campeonato.jogos += 1
            return campeonato.id

    campeonatos.append(Campeonato(len(campeonatos), nome))
    return len(campeonatos) - 1