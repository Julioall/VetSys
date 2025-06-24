from repositories.cliente_repository import ClienteRepository
from services.cliente_servico import ClienteService

# Criando o repositório e o serviço
repositorio = ClienteRepository()
servico = ClienteService(repositorio)

# Cadastrando alguns clientes
servico.cadastrar_cliente(1, "Ana", "62-99999-1111", "ana@email.com")
servico.cadastrar_cliente(2, "Carlos", "62-88888-2222", "carlos@email.com")

# Listando todos os clientes
print("📋 Lista de clientes:")
for cliente in servico.listar_clientes():
    print(f"ID: {cliente.id} - Nome: {cliente.nome}")

# Buscando um cliente por ID
print("\n🔍 Buscando cliente com ID 1:")
cliente = servico.buscar_cliente(1)
if cliente:
    print(f"Cliente encontrado: {cliente.nome} - {cliente.email}")
else:
    print("Cliente não encontrado.")

# Atualizando um cliente
print("\n✏️ Atualizando cliente com ID 2:")
servico.atualizar_cliente(2, "Carlos Silva", "62-77777-3333", "c.silva@email.com")

# Mostrando cliente atualizado
cliente = servico.buscar_cliente(2)
print(f"Cliente atualizado: {cliente.nome} - {cliente.telefone}")

# Removendo um cliente
print("\n🗑️ Removendo cliente com ID 1:")
servico.remover_cliente(1)

# Listando clientes após remoção
print("\n📋 Lista atualizada de clientes:")
for cliente in servico.listar_clientes():
    print(f"ID: {cliente.id} - Nome: {cliente.nome}")
