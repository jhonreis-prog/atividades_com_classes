import os

if os.name == 'nt':
    os.system('cls')  
else:
    os.system('clear')


class Animal:
    def __init__(self, nome : str, barulho : str, idade : int = 0):
        self.nome = nome
        self.barulho = barulho
        self.idade = idade
    
    def fazer_barulho(self):
        
        print(f"{self.nome} fez {self.barulho}")

    def aniversario(self):
        
        self.idade += 1
        
        print(f"O {self.nome} fez {self.idade} anos!!")

def main():
    cachorro = Animal("Pastor Alemão", "AU AU!", 5)
    vaca = Animal("Vaca", "MUUUU!")
    hamster = Animal("Hamster", "Ssshhh")


    cachorro.fazer_barulho()
    vaca.fazer_barulho()
    
    hamster.fazer_barulho()
    hamster.aniversario()
    hamster.aniversario()
    hamster.aniversario()

if __name__ == "__main__":
    main()