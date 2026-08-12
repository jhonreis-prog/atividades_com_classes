# 1: Em Aplicativo - Guarde o nome e o consumo de bateria no próprio objeto aplicativo;  
#                   ✅✅✅


# 2: Em Celular - Verifique se o celular está ligado (self.ligado) E se a bateria é maior 
# ou igual ao consumo do objeto 'app' passado por parâmetro;
#                   ✅✅✅


# 3: Em executar_app - Subtraia o consumo do aplicativo da bateria atual do celular,
# não deve ser possivel executar um app com o celular desligado,
# deve se mostrado na tela o nome do aplicativo que foi usado.
#                   ✅✅✅


# 4: Crie dois objetos Aplicativo com consumos de bateria diferentes;
# 5: Crie um objeto Celular, ligue o aparelho e execute cada um dos aplicativos criados.
#                   ✅✅✅


import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

class Aplicativo:
    def __init__(self, nome, consumo_bateria):
        
        self.nome = nome
        self.consumo_bateria = consumo_bateria


class Celular:
    def __init__(self, marca, modelo, bateria = 100):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = True

    def ligar(self):
        self.ligado = True
        print(f"O {self.marca} {self.modelo} foi ligado.")

    def executar_app(self, app):
        if self.ligado and self.bateria > app.consumo_bateria:
            print(f"O {self.modelo} tem bateria o suficiente para entrar no app: {self.bateria}%")
            print("Entrando no Youtumbe...\napp iniciado")
            self.bateria -= app.consumo_bateria
            print(f"Bateria atual do seu {self.modelo} é de {self.bateria}%")
        else:
            print("Não tem bateria seu jumento, bota o celular pra carregar 👌")



iphone = Celular("Apple", "iPhone 17", 99)
Youtumbe = Aplicativo("Youtumbe", 14)

samsung = Celular("Samsung", "Galaxy A07", 100)
whatsapp = Aplicativo("Whats", 10)

iphone.ligar()
iphone.executar_app(Youtumbe)
print("\n")
samsung.ligar()
samsung.executar_app(whatsapp)