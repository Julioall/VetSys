from models.cliente import Cliente

class ClienteService:
    def __init__(self, cliente_repository):
        self.cliente_repository = cliente_repository

    def cadastrar_cliente(self, id, nome, telefone, email):
        cliente = Cliente(id, nome, telefone, email)
        self.cliente_repository.adicionar(cliente)

    def listar_clientes(self):
        return self.cliente_repository.listar_todos()

    def buscar_cliente(self, id):
        return self.cliente_repository.buscar_por_id(id)

    def atualizar_cliente(self, id, nome, telefone, email):
        cliente = Cliente(id, nome, telefone, email)
        return self.cliente_repository.atualizar(id, cliente)

    def remover_cliente(self, id):
        return self.cliente_repository.remover(id)
