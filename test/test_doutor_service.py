import unittest
from repositories.doutor_repository import DoutorRepository
from services.doutor_servico import DoutorService

class TestDoutorService(unittest.TestCase):
    def setUp(self):
        self.repo = DoutorRepository()
        self.service = DoutorService(self.repo)

    def test_cadastrar_doutor(self):
        self.service.cadastrar_doutor(1, "Dra. Ana", "Cirurgia", "CRMV123")
        doutor = self.service.buscar_doutor(1)
        self.assertIsNotNone(doutor)
        self.assertEqual(doutor.nome, "Dra. Ana")

    def test_listar_doutores(self):
        self.service.cadastrar_doutor(1, "Dr. João", "Clínico", "CRMV456")
        self.service.cadastrar_doutor(2, "Dra. Clara", "Dermatologia", "CRMV789")
        doutores = self.service.listar_doutores()
        self.assertEqual(len(doutores), 2)

    def test_atualizar_doutor(self):
        self.service.cadastrar_doutor(3, "Dr. Pedro", "Ortopedia", "CRMV000")
        atualizado = self.service.atualizar_doutor(3, "Dr. Pedro Santos", "Neurologia", "CRMV001")
        self.assertTrue(atualizado)
        doutor = self.service.buscar_doutor(3)
        self.assertEqual(doutor.nome, "Dr. Pedro Santos")

    def test_remover_doutor_existente(self):
        self.service.cadastrar_doutor(4, "Dr. Fabio", "Oncologia", "CRMV999")
        removido = self.service.remover_doutor(4)
        self.assertTrue(removido)
        self.assertIsNone(self.service.buscar_doutor(4))

    def test_remover_doutor_inexistente(self):
        removido = self.service.remover_doutor(999)
        self.assertFalse(removido)

if __name__ == '__main__':
    unittest.main()
