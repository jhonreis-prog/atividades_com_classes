import os

if os.name == 'nt':
    os.system('cls')  
else:
    os.system('clear')


class Carro:
    def __init__(self, modelo : str, marca : str):
        self.modelo = modelo
        self.marca = marca
        self.combustivel = 100
        self.quilometragem = 0
    
    def fazer_barulho(self):
        if self.combustivel - 2 >= 0:
            self.combustivel -= 2
            print(f"{self.modelo} está fazendo barulho! \nCombustível: {self.combustivel}")
        else:
            print("Sem combustível para isso!")
    
    def acelerar(self):
        if self.combustivel - 10 >= 0:
            self.combustivel -= 10
            self.quilometragem += 15
            print(f"{self.modelo} acelerou! \nCombustível: {self.combustivel} e andou {self.quilometragem} km")
        else:
            print("Sem combustível para isso!")

    def abastecer(self, quantidade):
        quantidade = float(input("Quanto deseja abastecer? "))
        
        if (self.combustivel + quantidade <= 100):
            self.combustivel += quantidade
        
            print(f"Combustível: {self.combustivel}")
        else:
            print("O tanque não pode passar de 100!")

    def painel(self):
        print(f"Seu carro da {self.modelo} da marca {self.marca}")
        print(f"está com {self.combustivel} de combustivel")
        print(f"e ele andou {self.quilometragem} km")


def main():
    onyx = Carro("Onyx", "Chevrolet")
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()
    onyx.abastecer(0)
    print("\n")
    onyx.painel()
    

if __name__ == "__main__":
    main()