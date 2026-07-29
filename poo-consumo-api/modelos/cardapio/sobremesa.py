from abc import ABC

from modelos.cardapio.ItemCardapio import ItemCardapio

class Sobremesa(ItemCardapio, ABC):
    def __init__(self,nome, preco, tipo: str, descricao: str, tamanho:str) -> None:
        super().__init__(nome, preco)
        self._tipo = tipo
        self._descricao = descricao
        self._tamanho = tamanho

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)