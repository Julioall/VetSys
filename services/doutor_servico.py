from models.doutor import Doutor

class DoutorService:
    def __init__(self, doutor_repository):
        self.doutor_repository = doutor_repository

    def cadastrar_doutor(self, id, nome, especialidade, crmv):
        doutor = Doutor(id, nome, especialidade, crmv)
        self.doutor_repository.adicionar(doutor)

    def listar_doutores(self):
        return self.doutor_repository.listar_todos()

    def buscar_doutor(self, id):
        return self.doutor_repository.buscar_por_id(id)

    def atualizar_doutor(self, id, nome, especialidade, crmv):
        doutor = Doutor(id, nome, especialidade, crmv)
        return self.doutor_repository.atualizar(id, doutor)

    def remover_doutor(self, id):
        return self.doutor_repository.remover(id)
