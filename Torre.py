class Torre:
    def __init__(self, nome):
        self.nome = nome
        self.discos = []

    def empilhar(self, disco):
        if not self.discos or self.discos[-1].id > disco.id:
            self.discos.append(disco)
            return True
        return False

    def desempilhar(self):
        if self.discos:
            return self.discos.pop()

    def __str__(self):
        return str([str(disco) for disco in self.discos])
