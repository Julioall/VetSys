from models.cliente import Cliente
from utils.persistencia import guardar_banco, carregar_banco

class ClienteRepository:
    def __init__(self):
        self.arquivo = 'database/clientes.json'
        self.clientes = carregar_banco(self.arquivo, Cliente)

    def adicionar(self, cliente):
        self.clientes.append(cliente)
        guardar_banco(self.clientes, self.arquivo)

    def listar_todos(self):
        return self.clientes

    def buscar_por_id(self, id):
        return next((c for c in self.clientes if c.id == id), None)

    def atualizar(self, id, novo_cliente):
        for i, c in enumerate(self.clientes):
            if c.id == id:
                self.clientes[i] = novo_cliente
                guardar_banco(self.clientes, self.arquivo)
                return True
        return False

    def remover(self, id):
        for c in self.clientes:
            if c.id == id:
                self.clientes.remove(c)
                guardar_banco(self.clientes, self.arquivo)
                return True
        return False
