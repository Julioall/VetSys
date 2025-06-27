import unittest
from repositories.agendamento_repository import AgendamentoRepository
from services.agendamento_servico import AgendamentoService
from datetime import datetime

class TestAgendamentoService(unittest.TestCase):
    def setUp(self):
        self.repo = AgendamentoRepository()
        self.service = AgendamentoService(self.repo)

    def test_cadastrar_agendamento(self):
        data_hora = datetime(2025, 7, 1, 10, 0)
        self.service.cadastrar_agendamento(1, 101, 201, 301, data_hora)
        agendamento = self.service.buscar_agendamento(1)
        self.assertIsNotNone(agendamento)
        self.assertEqual(agendamento.data_hora, data_hora)

    def test_listar_agendamentos(self):
        self.service.cadastrar_agendamento(1, 101, 201, 301, datetime.now())
        self.service.cadastrar_agendamento(2, 102, 202, 302, datetime.now())
        agendamentos = self.service.listar_agendamentos()
        self.assertEqual(len(agendamentos), 2)

    def test_atualizar_agendamento(self):
        data1 = datetime(2025, 7, 1, 10, 0)
        data2 = datetime(2025, 7, 2, 15, 0)
        self.service.cadastrar_agendamento(3, 103, 203, 303, data1)
        atualizado = self.service.atualizar_agendamento(3, 103, 203, 303, data2)
        self.assertTrue(atualizado)
        agendamento = self.service.buscar_agendamento(3)
        self.assertEqual(agendamento.data_hora, data2)

    def test_remover_agendamento_existente(self):
        self.service.cadastrar_agendamento(4, 104, 204, 304, datetime.now())
        removido = self.service.remover_agendamento(4)
        self.assertTrue(removido)
        self.assertIsNone(self.service.buscar_agendamento(4))

    def test_remover_agendamento_inexistente(self):
        removido = self.service.remover_agendamento(999)
        self.assertFalse(removido)

if __name__ == '__main__':
    unittest.main()
