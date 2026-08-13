import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

class OrdemDeServico:
    total_os_criadas = 0
    os_abertas = 0
    
    id = 0
    def __init__(self, cliente, descricao):
        self.cliente = cliente
        self.descricao = descricao

        OrdemDeServico.total_os_criadas += 1
        OrdemDeServico.os_abertas += 1

        self.id_os = OrdemDeServico.total_os_criadas
        self.status = "Aberta"

    def finalizar_os(self):
        if self.status == "Aberta":
            self.status = "Concluida"
            OrdemDeServico.os_abertas -= 1

    def verificar_os(self):
        print(OrdemDeServico.os_abertas)

os1 = OrdemDeServico("João", "Troca de óleo")
os2 = OrdemDeServico("Maria", "Revisão")
os3 = OrdemDeServico("Carlos", "Alinhamento")

os2.finalizar_os()
os2.verificar_os()