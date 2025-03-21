#Calcular as quantidades de produtos em estoque
#Calcular tempo medio de duracao de estoque
#Chackliste de produtos em estoque

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_peso(self, nome_produto):
        produtos_filtrados = list(filter(lambda produto: produto.nome == nome_produto, self.produtos))
        soma = 0
        for produto in produtos_filtrados:
            soma += produto.peso
        return soma
        

class Produto:
    def __init__(self, nome, peso, preco, tipo, data_de_compra, validade_original, validade_armazenado):
        if not isinstance(peso, float):
            raise ValueError("Peso tem que ser em float.")
        if not isinstance(preco, float):
            raise ValueError("Preço tem que ser em float.")
        self.nome = nome
        self.peso = peso
        self.preco = preco
        self.tipo = tipo
        self.data_de_compra = data_de_compra
        self.validade_original = validade_original
        self.validade_armazenado = validade_armazenado

        

        
