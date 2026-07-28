# Respostas
# 1) Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano.
#    Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

# Instanciando um carro e atribuindo valores aos seus atributos
meu_carro = Carro(modelo='Fusca', cor='Azul', ano=1970)



# 2) Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos.
#    Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, capacidade, nota_avaliacao, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

# Instanciando um restaurante e atribuindo valores aos seus atributos
restaurante_exemplo = Restaurante(
    nome='Comida Boa',
    categoria='Gourmet',
    capacidade=50,
    nota_avaliacao=4.5,
    ativo=True
)



# 3) Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros
#    e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

# Instanciando um restaurante utilizando o construtor
novo_restaurante = Restaurante(nome='Santa Marmita', categoria='Fast Food')



# 4) Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância,
#    seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

# Exibindo uma instância do restaurante formatada
restaurante_formatado = Restaurante(nome='Bom Sabor', categoria='Tradicional')
print(restaurante_formatado)



# 5) Crie uma classe chamada Cliente e pense em 4 atributos.
#    Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')

# 6) Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.
class Pessoa:
    def __init__(self, nome = '', idade = 0, profissao = ''):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return f'Seu nome é {self._nome}, sua idade é {self._idade}  e sua profissão é {self._profissao}'

    def aniversario(self)-> int:
        self._idade += 1
        return self._idade

    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, sou {self._nome}! Trabalho como {self._profissao}.'
        else:
            return f'Olá, sou {self._nome}!'


# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)


# 1) Crie uma classe chamada `ContaBancaria` com um construtor que aceita os parâmetros titular e saldo.
# Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False  # Atributo protegido

# 2) Na classe ContaBancaria, adicione um método especial `__str__` que retorna uma mensagem formatada com o titular e o saldo da conta.
#  Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R${self.saldo}"


conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)

print(conta1)
print(conta2)


# 3) Adicione um método de classe chamado `ativar_conta` à classe `ContaBancaria` que define o atributo ativo como `True`.
#  Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

def ativar_conta(self):
    self._ativo = True


conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
conta3.ativar_conta()
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")


# 4) Refatore a classe `ContaBancaria` para utilizar a abordagem "pythonica" na criação de atributos.
# Utilize propriedades, se necessário.
class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    def ativar_conta(self):
        self._ativo = True


# 5) Crie uma instância da classe e imprima o valor da propriedade titular.
conta4 = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")


# 6) Crie uma classe chamada `ClienteBanco` com um construtor que aceita 5 atributos.
# Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao


cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")


# 7) Crie um método de classe para a conta `ClienteBanco`.
class ClienteBanco:
    # ... (outros métodos e atributos)

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta


# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")

