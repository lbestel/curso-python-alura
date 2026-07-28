from modelos.restaurante import Restaurante

praca = Restaurante('praça', 'gourmet')

praca.receber_avaliacao('Gui', 10)
praca.receber_avaliacao('Lais', 8)
praca.receber_avaliacao('Manoel', 4)
praca.receber_avaliacao('João', 9)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()