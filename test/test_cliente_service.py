import unittest
from repositories.cliente_repository import ClienteRepository
from services.cliente_servico import ClienteService

class TestClienteService(unittest.TestCase):
    def setUp(self):
        self.repo = ClienteRepository()
        self.service = ClienteService(self.repo)

    def test_cadastrar_cliente(self):
        self.service.cadastrar_cliente(1, "João", "62-99999-1234", "joao@email.com")
        cliente = self.service.buscar_cliente(1)
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.nome, "João")

    def test_listar_clientes(self):
        self.service.cadastrar_cliente(1, "Maria", "62-12345-6789", "maria@email.com")
        self.service.cadastrar_cliente(2, "Lucas", "62-98765-4321", "lucas@email.com")
        clientes = self.service.listar_clientes()
        self.assertEqual(len(clientes), 2)

    def test_buscar_cliente_existente(self):
        self.service.cadastrar_cliente(3, "Carlos", "62-00000-0000", "carlos@email.com")
        cliente = self.service.buscar_cliente(3)
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.email, "carlos@email.com")

    def test_buscar_cliente_inexistente(self):
        cliente = self.service.buscar_cliente(999)
        self.assertIsNone(cliente)

    def test_atualizar_cliente(self):
        self.service.cadastrar_cliente(4, "Paula", "62-11111-1111", "paula@email.com")
        atualizado = self.service.atualizar_cliente(4, "Paula Souza", "62-22222-2222", "paula.souza@email.com")
        self.assertTrue(atualizado)
        cliente = self.service.buscar_cliente(4)
        self.assertEqual(cliente.nome, "Paula Souza")

    def test_remover_cliente_existente(self):
        self.service.cadastrar_cliente(5, "Ricardo", "62-33333-3333", "ricardo@email.com")
        removido = self.service.remover_cliente(5)
        self.assertTrue(removido)
        self.assertIsNone(self.service.buscar_cliente(5))

    def test_remover_cliente_inexistente(self):
        removido = self.service.remover_cliente(999)
        self.assertFalse(removido)

if __name__ == '__main__':
    unittest.main()

#Execute o comando abaixo para rodar os testes
# python -m unittest discover -s test