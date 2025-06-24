class ClienteRepository:
    def __init__(self):
        self.clientes = []

    def adicionar(self, cliente):
        self.clientes.append(cliente)

    def listar_todos(self):
        return self.clientes

    def buscar_por_id(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None

    def atualizar(self, id, novo_cliente):
        for i, cliente in enumerate(self.clientes):
            if cliente.id == id:
                self.clientes[i] = novo_cliente
                return True
        return False

    def remover(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                self.clientes.remove(cliente)
                return True
        return False
