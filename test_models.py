from unittest import TestCase
from models import Produto, Estoque

class ProdutoTests(TestCase):
    def test_criar_produto_com_sucesso(self):
        nome = "Arroz"
        peso = 4.0
        preco = 5.0
        tipo = "Alimento"
        data_de_compra = "12/12/2024"
        validade_original = "14/06/2027"
        validade_armazenado = "14/06/2030"
        produto = Produto(nome, peso, preco, tipo, data_de_compra, validade_original, validade_armazenado)
        self.assertEqual(produto.nome, nome)
        self.assertEqual(produto.peso, peso)
        self.assertEqual(produto.preco, preco)
        self.assertEqual(produto.tipo, tipo)
        self.assertEqual(produto.data_de_compra, data_de_compra)
        self.assertEqual(produto.validade_original, validade_original)
        self.assertEqual(produto.validade_armazenado, validade_armazenado)

    def test_criar_produto_com_peso_invalido(self):
        nome = "Arroz"
        peso = "TEST"
        preco = 5.0
        tipo = "Alimento"
        data_de_compra = "12/12/2024"
        validade_original = "14/06/2027"
        validade_armazenado = "14/06/2030"
        
        with self.assertRaises(ValueError) as error:
            Produto(nome, peso, preco, tipo, data_de_compra, validade_original, validade_armazenado)
        self.assertEqual(str(error.exception), "Peso tem que ser em float.")

    def test_criar_produto_com_preco_invalido(self):
        nome = "Arroz"
        peso = 4.0
        preco = "TEST"
        tipo = "Alimento"
        data_de_compra = "12/12/2024"
        validade_original = "14/06/2027"
        validade_armazenado = "14/06/2030"
        
        with self.assertRaises(ValueError) as error:
            Produto(nome, peso, preco, tipo, data_de_compra, validade_original, validade_armazenado)
        self.assertEqual(str(error.exception), "Preço tem que ser em float.")


class EstoqueTests(TestCase):
    def test_adicionar_produto_com_sucesso(self):
        produto = Produto("Arroz", 4.0, 5.0, "Alimento", "12/12/2024", "12/12/2024", "12/12/2024")
        estoque = Estoque()
        estoque.adicionar_produto(produto)
        
        self.assertEqual(len(estoque.listar_produtos()), 1)
        self.assertEqual(estoque.listar_produtos()[0], produto)

    def test_adicionar_produto_invalido(self):
        estoque = Estoque()
        
        with self.assertRaises(ValueError) as error:
            estoque.adicionar_produto("Test")
        self.assertEqual(str(error.exception), "Produto deve ser do tipo Produto.")

    def test_calcular_peso_com_sucesso(self):
        produto_1 = Produto("Arroz", 4.0, 5.0, "Alimento", "12/12/2024", "12/12/2024", "12/12/2024")
        produto_2 = Produto("Arroz", 10.0, 5.0, "Alimento", "12/12/2024", "12/12/2024", "12/12/2024")

        estoque = Estoque()
        estoque.adicionar_produto(produto_1)
        estoque.adicionar_produto(produto_2)
        self.assertEqual(estoque.calcular_peso("Arroz"), 14.0)
    
    def test_calcular_peso_com_nome_invalido(self):
        produto_1 = Produto("Arroz", 4.0, 5.0, "Alimento", "12/12/2024", "12/12/2024", "12/12/2024")
        produto_2 = Produto("Arroz", 10.0, 5.0, "Alimento", "12/12/2024", "12/12/2024", "12/12/2024")

        estoque = Estoque()
        estoque.adicionar_produto(produto_1)
        estoque.adicionar_produto(produto_2)
        
        with self.assertRaises(ValueError) as error:
            estoque.calcular_peso(12)
        self.assertEqual(str(error.exception), "Nome produto tem que ser uma string.")

    def test_listar_produtos_com_sucesso(self):
        produto_1 = Produto("Arroz", 4.0, 5.0, "Alimento", "12/12/2024", "12/12/2024", "12/12/2024")
        produto_2 = Produto("Arroz", 10.0, 5.0, "Alimento", "12/12/2024", "12/12/2024", "12/12/2024")

        estoque = Estoque()
        self.assertEqual(len(estoque.listar_produtos()), 0)
        estoque.adicionar_produto(produto_1)
        estoque.adicionar_produto(produto_2)
        self.assertEqual(len(estoque.listar_produtos()), 2)
    
    def test_listar_produtos_nome_invalido(self):
        produto_1 = Produto("Arroz", 4.0, 5.0, "Alimento", "12/12/2024", "12/12/2024", "12/12/2024")
        produto_2 = Produto("Arroz", 10.0, 5.0, "Alimento", "12/12/2024", "12/12/2024", "12/12/2024")

        estoque = Estoque()
        estoque.adicionar_produto(produto_1)
        estoque.adicionar_produto(produto_2)
        
        with self.assertRaises(ValueError) as error:
            estoque.listar_produtos(1)
        self.assertEqual(str(error.exception), "Nome produto tem que ser uma string.")

