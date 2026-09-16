import unittest
class Calculadora:
    def somar(self, a, b):
        return a + b
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b
class TestCalculadoraValidaEntradas(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()
    def test_divisao_valida(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
    def test_divisao_por_zero_lanca_excecao(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)
if __name__ == '__main__':
    unittest.main()