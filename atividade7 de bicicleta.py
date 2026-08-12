import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

class Bicicleta:

    def __init__(self, modelo: str, velocidade: int = 0):

        self.modelo = modelo
        self.velocidade = velocidade
    
    def pedalar(self):
        if self.velocidade < 60:
            self.velocidade += 5
        
        if self.velocidade > 60:
            print("Essa é a velocidade limite!")
        else:    
            print(f"Uma Bike Viking acelerou!\nVelocidade: {self.velocidade}km")

    def frear(self):
        if self.velocidade > 60:
            self.velocidade -= 5
            print("Freando...")
        elif self.velocidade == 0:
            print("A bike está totalmente parada")
        else:
            print("Pedalando...")

    def radar_de_velocidade(self):
        if self.velocidade > 60:
            print(f"A bike {self.modelo} está a {self.velocidade} km/h, está muito alto!")
        else:    
            print(f"A bike {self.modelo} está a {self.velocidade} km/h, está tudo certo")

    def main(self):
        self.pedalar()
        self.frear()
        self.radar_de_velocidade()


viking = Bicicleta("Viking", 0)

viking.main()