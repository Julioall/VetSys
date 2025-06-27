from models.pet import Pet
from utils.persistencia import guardar_banco, carregar_banco

class PetRepository:
    def __init__(self):
        self.arquivo = 'database/pets.json'
        self.pets = carregar_banco(self.arquivo, Pet)

    def adicionar(self, pet):
        self.pets.append(pet)
        guardar_banco(self.pets, self.arquivo)

    def listar_todos(self):
        return self.pets

    def buscar_por_id(self, id):
        for pet in self.pets:
            if pet.id == id:
                return pet
        return None

    def atualizar(self, id, novo_pet):
        for i, pet in enumerate(self.pets):
            if pet.id == id:
                self.pets[i] = novo_pet
                guardar_banco(self.pets, self.arquivo)
                return True
        return False

    def remover(self, id):
        for pet in self.pets:
            if pet.id == id:
                self.pets.remove(pet)
                guardar_banco(self.pets, self.arquivo)
                return True
        return False
