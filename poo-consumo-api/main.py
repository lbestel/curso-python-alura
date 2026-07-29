from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

praca = Restaurante('praça', 'gourmet')
suco = Bebida('Suco de Melancia', 5.0, 500)
suco.aplicar_desconto()

paozinho = Prato('Pãozinho', 2.0, 'O melhor pãozinho da cidade')
paozinho.aplicar_desconto()

praca.adicionar_no_cardapio(suco)
praca.adicionar_no_cardapio(paozinho)


def main():
    praca.exibir_cardapio


if __name__ == '__main__':
    main()