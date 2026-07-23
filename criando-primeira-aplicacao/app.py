import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Danke', 'categoria': 'Alemã', 'ativo': True},
    {'nome': 'Manggiare', 'categoria': 'Italiana', 'ativo': True}
]

def exibir_nome_app():
    print("*********************************")
    print("Sabor Express")
    print("*********************************")

def exibir_opcoes():
    print('[1] Cadastrar Restaurante')
    print('[2] Listar Restaurantes')
    print('[3] Alternar status do Restaurante')
    print('[4] Sair')
    print("*********************************")

def finalizar_app():
    exibir_subtitulo('Finalizando app!')

def opcao_invalida():
    print('Opcão invalida!\n')
    voltar_menu_principal()

def cadastrar_restaurante():
    '''
    Essa função é responsável por cadastrar um novo restaurante.
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes.
    '''
    exibir_subtitulo('Cadastro de Restaurante')
    nome_restaurante = input('Informe o nome do restaurante: ')
    categoria = input(f'Informe o categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'{nome_restaurante} cadastrado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurantes():
    '''
    Essa função é responsável por listar os restaurantes cadastrados.
    :return:
    '''
    exibir_subtitulo('Lista de Restaurantes')
    print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} ')

    voltar_menu_principal()

def alternar_status():
    '''
    Essa função é responsável por alterar o status do restaurante selecionado.
    :return:
    '''
    exibir_subtitulo('Alternar Status')
    nome_restaurante = input('Informe o nome do restaurante: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltar_menu_principal()

def voltar_menu_principal():
    '''
    Essa função é responsável por levar o usuário de volta ao menu principal.
    :return:
    '''
    input('Pressione uma ENTER para voltar ao menu ')
    main()

def exibir_subtitulo(texto):
    '''
    Essa função é responsável por exibir o subtitulo da opção escolhida.
    :param texto:
    :return:
    '''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcao():
    '''
    Essa função permite ao usuário escolher qual opção ele deseja usar do app.
    :return:
    '''
    try:
        opcao_escolhida = int(input("Escolha a sua opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status()
        elif opcao_escolhida == 4:
            finalizar_app()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()