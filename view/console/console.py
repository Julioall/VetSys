from datetime import datetime

from repositories.cliente_repository import ClienteRepository
from services.cliente_servico import ClienteService
from repositories.doutor_repository import DoutorRepository 
from services.doutor_servico import DoutorService
from repositories.pet_repository import PetRepository
from services.pet_servico import PetService
from repositories.agendamento_repository import AgendamentoRepository
from services.agendamento_servico import AgendamentoService

# Instanciando repositórios e serviços
cliente_service = ClienteService(ClienteRepository())
doutor_service = DoutorService(DoutorRepository())
pet_service = PetService(PetRepository())
agendamento_service = AgendamentoService(AgendamentoRepository())

def menu():
    print("\n🐾 Sistema de Clínica Veterinária")
    print("1. Gerenciar Clientes")
    print("2. Gerenciar Doutores")
    print("3. Gerenciar Pets")
    print("4. Gerenciar Agendamentos")
    print("0. Sair")

def submenu(entidade):
    print(f"\n📋 Menu {entidade}")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Buscar por ID")
    print("4. Atualizar")
    print("5. Remover")
    print("0. Voltar")

def gerenciar_clientes():
    while True:
        submenu("Clientes")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            id = int(input("ID: "))
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            cliente_service.cadastrar_cliente(id, nome, telefone, email)
        elif opcao == "2":
            for c in cliente_service.listar_clientes():
                print(f"{c.id} - {c.nome} ({c.email})")
        elif opcao == "3":
            id = int(input("ID: "))
            c = cliente_service.buscar_cliente(id)
            print(f"Nome: {c.nome}, Email: {c.email}" if c else "Cliente não encontrado.")
        elif opcao == "4":
            id = int(input("ID: "))
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            email = input("Novo email: ")
            atualizado = cliente_service.atualizar_cliente(id, nome, telefone, email)
            print("Atualizado com sucesso!" if atualizado else "Cliente não encontrado.")
        elif opcao == "5":
            id = int(input("ID: "))
            removido = cliente_service.remover_cliente(id)
            print("Removido com sucesso!" if removido else "Cliente não encontrado.")
        elif opcao == "0":
            break

def gerenciar_doutores():
    while True:
        submenu("Doutores")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            id = int(input("ID: "))
            nome = input("Nome: ")
            especialidade = input("Especialidade: ")
            crmv = input("CRMV: ")
            doutor_service.cadastrar_doutor(id, nome, especialidade, crmv)
        elif opcao == "2":
            for d in doutor_service.listar_doutores():
                print(f"{d.id} - {d.nome} ({d.especialidade})")
        elif opcao == "3":
            id = int(input("ID: "))
            d = doutor_service.buscar_doutor(id)
            print(f"Nome: {d.nome}, CRMV: {d.crmv}" if d else "Doutor não encontrado.")
        elif opcao == "4":
            id = int(input("ID: "))
            nome = input("Novo nome: ")
            especialidade = input("Nova especialidade: ")
            crmv = input("Novo CRMV: ")
            atualizado = doutor_service.atualizar_doutor(id, nome, especialidade, crmv)
            print("Atualizado com sucesso!" if atualizado else "Doutor não encontrado.")
        elif opcao == "5":
            id = int(input("ID: "))
            removido = doutor_service.remover_doutor(id)
            print("Removido com sucesso!" if removido else "Doutor não encontrado.")
        elif opcao == "0":
            break

def gerenciar_pets():
    while True:
        submenu("Pets")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            id = int(input("ID: "))
            nome = input("Nome: ")
            especie = input("Espécie: ")
            raca = input("Raça: ")
            idade = int(input("Idade: "))
            peso = float(input("Peso: "))
            cliente_id = int(input("ID do Cliente: "))
            pet_service.cadastrar_pet(id, nome, especie, raca, idade, peso, cliente_id)
        elif opcao == "2":
            for p in pet_service.listar_pets():
                print(f"{p.id} - {p.nome} ({p.especie}) - Cliente ID: {p.cliente_id}")
        elif opcao == "3":
            id = int(input("ID: "))
            p = pet_service.buscar_pet(id)
            print(f"{p.nome} - {p.raca}, {p.idade} anos" if p else "Pet não encontrado.")
        elif opcao == "4":
            id = int(input("ID: "))
            nome = input("Novo nome: ")
            especie = input("Nova espécie: ")
            raca = input("Nova raça: ")
            idade = int(input("Nova idade: "))
            peso = float(input("Novo peso: "))
            cliente_id = int(input("ID do cliente: "))
            atualizado = pet_service.atualizar_pet(id, nome, especie, raca, idade, peso, cliente_id)
            print("Atualizado com sucesso!" if atualizado else "Pet não encontrado.")
        elif opcao == "5":
            id = int(input("ID: "))
            removido = pet_service.remover_pet(id)
            print("Removido com sucesso!" if removido else "Pet não encontrado.")
        elif opcao == "0":
            break

def gerenciar_agendamentos():
    while True:
        submenu("Agendamentos")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            id = int(input("ID: "))
            cliente_id = int(input("ID do Cliente: "))
            pet_id = int(input("ID do Pet: "))
            doutor_id = int(input("ID do Doutor: "))
            data_str = input("Data e hora (YYYY-MM-DD HH:MM): ")
            data_hora = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
            agendamento_service.cadastrar_agendamento(id, cliente_id, pet_id, doutor_id, data_hora)
        elif opcao == "2":
            for a in agendamento_service.listar_agendamentos():
                print(f"{a.id} - Cliente {a.cliente_id}, Pet {a.pet_id}, Doutor {a.doutor_id} - {a.data_hora}")
        elif opcao == "3":
            id = int(input("ID: "))
            a = agendamento_service.buscar_agendamento(id)
            print(f"Cliente: {a.cliente_id}, Data: {a.data_hora}" if a else "Agendamento não encontrado.")
        elif opcao == "4":
            id = int(input("ID: "))
            cliente_id = int(input("ID do Cliente: "))
            pet_id = int(input("ID do Pet: "))
            doutor_id = int(input("ID do Doutor: "))
            data_str = input("Nova data e hora (YYYY-MM-DD HH:MM): ")
            data_hora = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
            atualizado = agendamento_service.atualizar_agendamento(id, cliente_id, pet_id, doutor_id, data_hora)
            print("Atualizado com sucesso!" if atualizado else "Agendamento não encontrado.")
        elif opcao == "5":
            id = int(input("ID: "))
            removido = agendamento_service.remover_agendamento(id)
            print("Removido com sucesso!" if removido else "Agendamento não encontrado.")
        elif opcao == "0":
            break

# Execução principal
while True:
    menu()
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        gerenciar_clientes()
    elif escolha == "2":
        gerenciar_doutores()
    elif escolha == "3":
        gerenciar_pets()
    elif escolha == "4":
        gerenciar_agendamentos()
    elif escolha == "0":
        print("Saindo... 👋")
        break
    else:
        print("Opção inválida.")
