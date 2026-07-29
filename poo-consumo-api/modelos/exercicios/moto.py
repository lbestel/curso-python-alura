from veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, tipo: tuple = ('esportiva', 'casual')):
        super().__init__(marca, modelo)
        self._tipo = tipo


    def __str__(self):
        return (f'{super().__str__()}\nTipo: {self._tipo}\n------------------------------------')