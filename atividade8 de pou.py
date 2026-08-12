import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

class Bixin:

    def __init__(self, name: str):
        
        self.name = name
        self.fome = 5
        self.felicidade = 5

    def alimentar(self):
        print(f"Você VAI alimentar {self.name}!!!")
        self.fome += 2
        
    def brincar(self):
        self.felicidade += 2
        self.fome -= 1