# 1 - Imprima a frase: Python na Escola de Programação da Alura.
# print('\nExercício 1')
# print('Python na Escola de Programação da Alura')
from itertools import count

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
# print('\nExercício 2')
# nome = input("Qual o seu nome? ")
# idade = input("Qual a sua idade? ")
#
# print(f'Meu nome é {nome} e tenho {idade} anos')

# Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha
# print('Exercício 3')
# print("""A
# L
# U
# R
# A
# """)

# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa
# ser armazenado em uma variável e arredondado para apenas duas casas decimais.
# print('\nExercício 4')
# pi = 3.14159
# pi_arredondado = round(pi, 2)
#
# print(f'O valor arredondado de pi é: {pi_arredondado}')

# 5 - Solicite ao usuário que insira um número e, em seguida,
# use uma estrutura if else para determinar se o número é par ou ímpar.
# print('\nExercício 5')
# numero = int(input('Digite um numero: '))
#
# if numero % 2 == 0:
#     print(f'O número {numero} é par!')
# else:
#     print(f'O número {numero} é impar!')

# 6 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else
# para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.
# print('\nExercício 6')
# idade = int(input('Digite sua idade: '))
# if idade <= 12:
#     print('O usuário é uma CRIANÇA')
# elif idade > 12 and idade <= 18:
#     print('O usuário é um ADOLESCENTE!')
# else:
#     print('O usuário é um ADULTO!')

# 7 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a
# senha fornecidos correspondem aos valores esperados determinados por você.
# print('\nExercício 7')
# usuario = 'lucas'
# senha = '1234'
#
# login = input('Digite seu usuário: ')
# password = input('Digite sua senha: ')
#
# if login == usuario and password == senha:
#     print('Login realizado com sucesso!')
# else:
#     print('Usuário ou senha incorretos!')

# 8 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para
# determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

# print('\nExercício 8')
# x = int(input('Digite o valor de X: '))
# y = int(input('Digite o valor de Y: '))
#
# if x > 0 and y > 0:
#     print('Primeiro Quadrante')
# elif x < 0 < y:
#     print('Segundo Quadrante')
# elif x < 0 and y < 0:
#     print('Terceiro Quadrante')
# elif x > 0 > y:
#     print('Quarto Quadrante')
# else:
#     print('O ponto está localizado no eixo de origem.')

# 9 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

# print('\nExercício 9')
# numeros = []
# for i in range(1,11):
#     numeros.append(i)
# print(numeros)
#
# nomes = ['Jesus', 'Maria', 'José', 'Pedro']
# print(nomes)
#
# ano_nascimento = 1992
# ano_atual = 2026
#
# lista_anos = [ano_nascimento, ano_atual]
# print(lista_anos)

# 10 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
# print('\nExercício 10')
# print('Lista de numeros:')
# for n in numeros:
#     print(n)

# 11 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
# print('\nExercício 11')
# valor = 0
# for n in numeros:
#     if n % 2 == 1:
#         valor = valor + n
#
# print(f'A soma dos números impares entre 1 e 10 é: {valor}')

# 12 - Solicite ao usuário um número e, em seguida, utilize
# um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# numero_escolhido = int(input('Digite um número: '))
# print('\nExercício 12')
# print(f'Tabuada do {numero_escolhido}')
# for n in range(1, 11):
#     produto = numero_escolhido * n
#     print(f'{numero_escolhido} x {n} = {produto}')

# 13 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.
# Utilize um bloco try-except para lidar com possíveis exceções.
# numeros = [1, 2, 'a', 4, 5]
# soma = 0
# try:
#     for n in numeros:
#         soma = soma + n
#
#     print(soma)
# except:
#     print('Não é possivel realizar a soma!')

# 14 - Construa um código que calcule a média dos valores em uma lista.
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
numeros = [1, 2, 'a', 4, 5]

# try:
#     media = 0
#     valor = 0
#     for n in numeros:
#         valor = valor + n
#         media = valor / len(numeros)
#
#     print(media)
# except ZeroDivisionError:
#     print('A lista está vazia!, não é possível calcular a média!')
# except Exception as e:
#     print(f'Ocorreu um erro: {e}')

# 15 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoa = {'nome': 'Felipe', 'idade': 30, 'cidade': 'São Paulo'}

# 16 - Utilizando o dicionário criado no item 15:
# Atualização de Idade
pessoa['idade'] = 31

# Adicionando Profissão
pessoa['profissao'] = 'Engenheiro'

# Remoção de Elemento
del pessoa['cidade']

# 17 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

# 18 - Para verificar a existência de uma chave no dicionário, você pode utilizar a seguinte estrutura:

pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

# 19 - Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)