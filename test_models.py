from unittest import TestCase
from models import Produto

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

        
    
