from modelos.cardapio.ItemCardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome: str, preco: float, tamanho: int):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)