import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

class Aluno:
    GABARITOS = [["a", "b", "c", "d", "e"],["b", "b", "c", "e", "a"],["a", "a", "e", "b", "d"]]  # noqa: RUF012

    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.historico_notas = []

    def fazer_prova(self, numero_prova, respostas: tuple[str, ...]):
        gabarito = self.GABARITOS[numero_prova]
        nota = 0
        for resposta, correta in zip(respostas, gabarito):
            if resposta == correta:
                nota += 2
                
        self.historico_notas.append(nota)
        
    def calcular_media(self):
        if len(self.historico_notas) == 0:
            return 0

        soma = 0

        for nota in self.historico_notas:
            soma += nota

        return soma / len(self.historico_notas)



    def ver_boletim(self):
        media = self.calcular_media()

        print(f"Aluno(a): {self.nome} {self.sobrenome}")
        print(f"Notas: {self.historico_notas}")
        print(f"Média final: {media:.2f}")

        if media >= 6:
            print("Situação: Aprovado")
        else:
            print("Situação: Reprovado")

def main():
    arthur = Aluno("Arthur José", "Figueiredo", 18)
    
    arthur.fazer_prova(0, ("a", "b", "a", "d", "d"))
    arthur.fazer_prova(1, ("b", "c", "b", "e", "a"))
    arthur.fazer_prova(2, ("e", "a", "e", "b", "a"))
    
    arthur.ver_boletim()

if __name__ == "__main__":
    main()