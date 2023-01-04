
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome.title()
        self.__idade = idade
        self.__cpf = cpf.title()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

class Funcionario (Pessoa):
    def __init__(self, nome, idade, cpf, salario):
        super().__init__(nome, idade, cpf)
        self.salario = salario

    def descontarSalario(self, valor):
        self.salario -= valor

    def aumentarSalario(self, valor):
        self.salario += valor

    def imprimirDados(self):
        print(f'Funcionário: {self.get_nome()}')
        print(f'Idade: {self.get_idade()}')
        print(f'Cpf: {self.get_cpf()}')
        print(f'Salário atual: {self.salario}')
