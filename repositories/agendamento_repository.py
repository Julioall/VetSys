from models.agendamento import Agendamento
from utils.persistencia import guardar_banco, carregar_banco

class AgendamentoRepository:
    def __init__(self):
        self.arquivo = 'database/agendamentos.json'
        self.agendamentos = carregar_banco(self.arquivo, Agendamento)

    def adicionar(self, agendamento):
        self.agendamentos.append(agendamento)
        guardar_banco(self.agendamentos, self.arquivo)

    def listar_todos(self):
        return self.agendamentos

    def buscar_por_id(self, id):
        for agendamento in self.agendamentos:
            if agendamento.id == id:
                return agendamento
        return None

    def atualizar(self, id, novo_agendamento):
        for i, agendamento in enumerate(self.agendamentos):
            if agendamento.id == id:
                self.agendamentos[i] = novo_agendamento
                guardar_banco(self.agendamentos, self.arquivo)
                return True
        return False

    def remover(self, id):
        for agendamento in self.agendamentos:
            if agendamento.id == id:
                self.agendamentos.remove(agendamento)
                guardar_banco(self.agendamentos, self.arquivo)
                return True
        return False
