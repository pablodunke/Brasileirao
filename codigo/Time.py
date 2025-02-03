# @project Brasileirao
# @description Classe que representa os times das partidas
# @createdBy Pablo Giovani Dunke
# @createdDate 2024/10/28

class Time:
    def __init__(self, pid, pnome, pestado):
        self.id = pid
        self.nome = pnome
        self.estado = pestado
        self.completo = pnome + "/" + pestado

def adicionaTime(times, pnome, pestado):
    for time in times:
        if time.nome == pnome:
            return time.id

    times.append(Time(len(times), pnome, pestado))
    return len(times) - 1

def imprimeTimes(times):
    for time in times:
        print('Time ' + time.nome + ' do estado de ' + time.estado + '.')

def buscaTime(linha, times):
    for time in times:
        if time.completo in linha:
            return time.id

    return None