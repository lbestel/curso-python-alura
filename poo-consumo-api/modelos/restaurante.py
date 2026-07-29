from modelos.avaliacao import Avaliacao
from modelos.cardapio.ItemCardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.status}')

    @property
    def status(self):
        return '✅' if self._status else '❌'

    def alternar_status(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliação'

        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media_avaliacao = round((soma_das_notas / quantidade_notas), 1)
        return media_avaliacao

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do Restaurante: {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f'[{i}] Nome: {item._nome} | Preço: R${item._preco:.2f} | Descricao: {item._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'[{i}] Nome: {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)