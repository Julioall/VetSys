from models.pet import Pet

class PetService:
    def __init__(self, pet_repository):
        self.pet_repository = pet_repository

    def cadastrar_pet(self, id, nome, especie, raca, idade, peso, cliente_id):
        pet = Pet(id, nome, especie, raca, idade, peso, cliente_id)
        self.pet_repository.adicionar(pet)

    def listar_pets(self):
        return self.pet_repository.listar_todos()

    def buscar_pet(self, id):
        return self.pet_repository.buscar_por_id(id)

    def atualizar_pet(self, id, nome, especie, raca, idade, peso, cliente_id):
        pet = Pet(id, nome, especie, raca, idade, peso, cliente_id)
        return self.pet_repository.atualizar(id, pet)

    def remover_pet(self, id):
        return self.pet_repository.remover(id)
