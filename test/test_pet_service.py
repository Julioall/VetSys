import unittest
from repositories.pet_repository import PetRepository
from services.pet_servico import PetService

class TestPetService(unittest.TestCase):
    def setUp(self):
        self.repo = PetRepository()
        self.service = PetService(self.repo)

    def test_cadastrar_pet(self):
        self.service.cadastrar_pet(1, "Rex", "Cachorro", "Labrador", 5, 25.0, 101)
        pet = self.service.buscar_pet(1)
        self.assertIsNotNone(pet)
        self.assertEqual(pet.nome, "Rex")

    def test_listar_pets(self):
        self.service.cadastrar_pet(1, "Mimi", "Gato", "Persa", 3, 4.5, 102)
        self.service.cadastrar_pet(2, "Luna", "Cachorro", "Poodle", 2, 6.0, 103)
        pets = self.service.listar_pets()
        self.assertEqual(len(pets), 2)

    def test_atualizar_pet(self):
        self.service.cadastrar_pet(3, "Bidu", "Cachorro", "Beagle", 4, 12.0, 104)
        atualizado = self.service.atualizar_pet(3, "Bidu", "Cachorro", "Beagle", 5, 13.0, 104)
        self.assertTrue(atualizado)
        pet = self.service.buscar_pet(3)
        self.assertEqual(pet.idade, 5)

    def test_remover_pet_existente(self):
        self.service.cadastrar_pet(4, "Frajola", "Gato", "Siamês", 6, 5.0, 105)
        removido = self.service.remover_pet(4)
        self.assertTrue(removido)
        self.assertIsNone(self.service.buscar_pet(4))

    def test_remover_pet_inexistente(self):
        removido = self.service.remover_pet(999)
        self.assertFalse(removido)

if __name__ == '__main__':
    unittest.main()
