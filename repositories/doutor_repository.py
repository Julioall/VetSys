from models.doutor import Doutor
from utils.persistencia import guardar_banco, carregar_banco

class DoutorRepository:
    def __init__(self):
        self.arquivo = 'database/doutores.json'
        self.doutores = carregar_banco(self.arquivo, Doutor)

    def adicionar(self, doutor):
        self.doutores.append(doutor)
        guardar_banco(self.doutores, self.arquivo)

    def listar_todos(self):
        return self.doutores

    def buscar_por_id(self, id):
        for doutor in self.doutores:
            if doutor.id == id:
                return doutor
        return None

    def atualizar(self, id, novo_doutor):
        for i, doutor in enumerate(self.doutores):
            if doutor.id == id:
                self.doutores[i] = novo_doutor
                guardar_banco(self.doutores, self.arquivo)
                return True
        return False

    def remover(self, id):
        for doutor in self.doutores:
            if doutor.id == id:
                self.doutores.remove(doutor)
                guardar_banco(self.doutores, self.arquivo)
                return True
        return False
