from Torre import Torre
from Disco import Disco


class Hanoi:
    def __init__(self, n_discos):
        self.n_discos = n_discos
        self.torre_a = Torre("A")
        self.torre_b = Torre("B")
        self.torre_c = Torre("C")

        for i in range(n_discos, 0, -1):
            self.torre_a.empilhar(Disco(i))

    def jogar(self):
        self.print_torres()
        while not self.verificar_vitoria():
            origem = input("Digite a torre de origem (A, B ou C): ").upper()
            destino = input("Digite a torre de destino (A, B ou C): ").upper()
            if not self.mover_disco(origem, destino):
                print("Não foi possível mover o disco. Tente novamente.")
            self.print_torres()
        print("Parabéns, você venceu!")

    def mover_disco(self, origem, destino):
        if origem == destino:
            return False

        if origem == "A":
            torre_origem = self.torre_a
        elif origem == "B":
            torre_origem = self.torre_b
        elif origem == "C":
            torre_origem = self.torre_c
        else:
            return False

        if destino == "A":
            torre_destino = self.torre_a
        elif destino == "B":
            torre_destino = self.torre_b
        elif destino == "C":
            torre_destino = self.torre_c
        else:
            return False

        disco = torre_origem.desempilhar()
        if not disco:
            return False
        if not torre_destino.empilhar(disco):
            torre_origem.empilhar(disco)
            return False
        return True

    def verificar_vitoria(self):
        return len(self.torre_c.discos) == self.n_discos

    def print_torres(self):
        print(f"Torre A: {self.torre_a}")
        print(f"Torre B: {self.torre_b}")
        print(f"Torre C: {self.torre_c}")
        print()
