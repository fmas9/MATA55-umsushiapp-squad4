from backend.PoC.adapters.outbound.mock_locale_repository import listar_regioes
from backend.PoC.domain.entities.user.payer import Cliente
#lista para aguarda
regioes = []
clientes = []
def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    email = input("Email do cliente: ")
    senha = input("senha do cliente: ")
    telefone = input("Telefone do cliente: ")
    
    if not regioes:
        print("Cadastre ao menos uma região antes de adicionar um cliente.")
        return
    
    listar_regioes()
    try:
        opcao = int(input("Escolha o número da região do cliente: ")) - 1
        if opcao < 0 or opcao >= len(regioes):
            print("Região inválida.")
            return
        regiao_escolhida = regioes[opcao]
    except ValueError:
        print("Entrada inválida.")
        return

    cliente = Cliente(nome, email,senha,telefone , regiao_escolhida)
    clientes.append(cliente)
    print(f" Cliente '{nome}' cadastrado com sucesso!")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        print("👥 Clientes cadastrados:")
        for c in clientes:
            print(f"- {c.nome} ({c.email}), Região: {c.regiao.nome}")
