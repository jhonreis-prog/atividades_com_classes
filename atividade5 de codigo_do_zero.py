class Produto:

    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def reduzir_estoque(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            print("Estoque insuficiente!")
            return False


class CarrinhoDeCompras:

    def __init__(self):
        self.produtos = []

    def adicionar_ao_carrinho(self, produto, quantidade):
        if produto.reduzir_estoque(quantidade):
            self.produtos.append((produto, quantidade))

    def mostrar_carrinho(self):
        for produto, quantidade in self.produtos:
            print(f"{produto.nome} - Quantidade: {quantidade}")

    def finalizar_compra(self):
        total = 0

        for produto, quantidade in self.produtos:
            total += produto.preco * quantidade

        print(f"Total da compra: R$ {total:.2f}")
        print("Compra finalizada!")


mouse = Produto("Mouse", 50.0, 10)
teclado = Produto("Teclado", 65.0, 8)

carrinho = CarrinhoDeCompras()

carrinho.adicionar_ao_carrinho(mouse, 2)
carrinho.adicionar_ao_carrinho(teclado, 1)

carrinho.mostrar_carrinho()

while True:

    print("\n=== LOJA ===")
    print("1 - Comprar")
    print("2 - Ver carrinho")
    print("3 - Finalizar compra")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:

        case "1":
            print("\n=== PRODUTOS ===")
            print("1 - Mouse - R$ 50,00")
            print("2 - Teclado - R$ 65,00")

            produto_escolhido = input("Qual produto deseja comprar? ")

            if produto_escolhido == "1":
                produto = mouse
            elif produto_escolhido == "2":
                produto = teclado
            else:
                print("Produto inválido!")
                continue

            quantidade = int(input("Quantas unidades deseja comprar? "))

            carrinho.adicionar_ao_carrinho(produto, quantidade)

        case "2":
            carrinho.mostrar_carrinho()

        case "3":
            carrinho.finalizar_compra()
            break

        case "4":
            print("Obrigado por visitar a loja!")
            break

        case _:
            print("Opção inválida!")