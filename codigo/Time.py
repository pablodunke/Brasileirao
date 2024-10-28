# @project Brasileirao
# @description Classe que representa os times das partidas
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

class Time:
    def __init__(self, pid, pnome):
        self.id = pid
        self.nome = pnome
        self.jogos = 1

def adicionarTime(times, nome):
    for time in times:
        if time.nome == nome:
            time.jogos += 1
            return time.id

    times.append(Time(len(times), nome))
    return len(times) - 1