# 1) Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo.
# A classe deve ter um atributo protegido _ligado inicializado como False por padrão.

class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'Dados do Veículo:\nMarca: {self._marca}\nModelo: {self._modelo}\nLigado: {self._ligado}'