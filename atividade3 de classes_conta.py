from datetime import datetime, timedelta

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')


class ContaBancaria:
    def __init__(self, titular : str):
        self.titular = titular
        self.saldo = 0
        self.extrato = []

    def transferir(self, valor, quem_recebe):
        self.saldo -= valor
        quem_recebe.plus_dinh(valor)
        return self.saldo
    
    def plus_dinh(self, valor):
        self.saldo += valor
        return self.saldo

    def mostrar_informações(self): 
        print(f"{self.titular}\nSaldo Atual: {self.saldo}")
    
    def mostrar_extrato(self):
        for i in self.extrato:
            print(f"{i["data"]} > {i["movimento"]}")
        print("\n")

    def atualizar_extrato(self, transacao : float):
        self.extrato.append({"data": datetime.now(),"movimento": transacao})  # noqa: DTZ005
    
    def adicionar_saldo(self, valor):
        self.saldo += valor
        self.atualizar_extrato(valor)
    
    def fazer_pix(self, valor):
        if self.saldo - valor < -500:
            print("Transação bloqueada!")
        else:
            self.saldo -= valor
            self.atualizar_extrato(-valor)

gabriel = ContaBancaria("Gabriel")
gabriel.adicionar_saldo(1000)
gabriel.mostrar_extrato()
gabriel.fazer_pix(600)
gabriel.mostrar_extrato()
gabriel.mostrar_informações()

joao = ContaBancaria("João")
joao.adicionar_saldo(200)
joao.mostrar_extrato()
joao.mostrar_informações()
joao.mostrar_extrato()

gabriel.transferir(200, joao)
print(joao.saldo)
joao.mostrar_extrato()




# class pessoa:
#     def __init__(self, saldo):
#         self.saldo = saldo
#
#     def transferir(self, valor, quem_recebe):
#        self.saldo -= valor
#         quem_recebe.adicionar_dinheiro(valor)
#         return self.saldo
#
#     def adicionar_dinheiro(self, valor):
#         self.saldo += valor
#         return self.saldo
#
# gabriel = pessoa(1000)
# aline = pessoa (200)
#
# gabriel.transferir(200, aline)
# print(aline.saldo)