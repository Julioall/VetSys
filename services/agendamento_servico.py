from models.agendamento import Agendamento

class AgendamentoService:
    def __init__(self, agendamento_repository):
        self.agendamento_repository = agendamento_repository

    def cadastrar_agendamento(self, id, cliente_id, pet_id, doutor_id, data_hora):
        agendamento = Agendamento(id, cliente_id, pet_id, doutor_id, data_hora)
        self.agendamento_repository.adicionar(agendamento)

    def listar_agendamentos(self):
        return self.agendamento_repository.listar_todos()

    def buscar_agendamento(self, id):
        return self.agendamento_repository.buscar_por_id(id)

    def atualizar_agendamento(self, id, cliente_id, pet_id, doutor_id, data_hora):
        agendamento = Agendamento(id, cliente_id, pet_id, doutor_id, data_hora)
        return self.agendamento_repository.atualizar(id, agendamento)

    def remover_agendamento(self, id):
        return self.agendamento_repository.remover(id)
