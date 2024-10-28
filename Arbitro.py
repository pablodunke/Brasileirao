



class Arbitro:
    def __init__(self, nome):
        self.nome = nome
        self.valores = []

    def adicionar_valor(self, valor):
        self.valores.append(valor)

    def mostrar_valores(self):
        return self.valores