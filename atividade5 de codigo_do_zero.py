class Produto:

    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def reduzir_estoque(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
        else:
            print("Estoque insuficiente!")


class CarrinhoDeCompras:

    def __init__(self):
        self.produtos = []

    def adicionar_ao_carrinho(self, produto, quantidade):
        produto.reduzir_estoque(quantidade)
        self.produtos.append((produto, quantidade))

    def mostrar_carrinho(self):
        for produto, quantidade in self.produtos:
            print(f"{produto.nome} - Quantidade: {quantidade}")


mouse = Produto("Mouse", 50.0, 10)
teclado = Produto("Teclado", 65.0, 8)