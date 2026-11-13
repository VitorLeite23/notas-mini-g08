import unittest
from notas.situacao import situacao

class TestSituacao(unittest.TestCase):
    def test_media_alta_e_frequencia_boa(self):
        self.assertEqual(situacao(8.0, 90), "aprovado")
    def test_limite_aprovado(self):
        self.assertEqual(situacao(6.0, 75), "aprovado")
    def test_exame_media_5_9(self):
        self.assertEqual(situacao(5.9, 100), "exame")
    def test_exame_media_4(self):
        self.assertEqual(situacao(4.0, 80), "exame")
    def test_media_baixa_reprova(self):
        self.assertEqual(situacao(3.9, 80), "reprovado")
    def test_frequencia_baixa_reprova(self):
        self.assertEqual(situacao(9.0, 74), "reprovado")
