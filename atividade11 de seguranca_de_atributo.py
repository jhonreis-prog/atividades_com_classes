class CofreDigital:

    def __init__(self, titular, senha):
        self.titular = titular
        self.__senha = senha
        self.__saldo = 0.0

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor, senha_informada):
        if senha_informada == self.__senha:
            print("Senha correta!")
        elif self.__saldo >= valor:
            print("Transação concluida!")
        else:
            print("Senha incorreta!")

cofre = CofreDigital("Jhon", "1234")

cofre.depositar(100)

cofre.sacar(30, "1234")