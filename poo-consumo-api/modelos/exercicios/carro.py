from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, porta:int):
        super().__init__(marca, modelo)
        self._porta = porta

    def __str__(self):
        return f'{super().__str__()}\nNúmero de portas: {self._porta}\n------------------------------------'