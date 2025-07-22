from adapters.outbound.mock_locale_repository import listar_regioes
from domain.entities.user.payer import Payer
#lista para aguarda
regioes = []
clientes = []
def cadastrar_cliente():
    name = input("Nome do cliente: ")
    email = input("Email do cliente: ")
    password = input("Senha do cliente: ")
    phone_number = input("Numero do cliente: ")
    
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

    cliente = Payer(name, email,password, phone_number, regiao_escolhida)
    clientes.append(cliente)
    print(f" Payer '{name}' cadastrado com sucesso!")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        print("👥 Payers cadastrados:")
        for c in clientes:
            print(f"- {c.name} ({c.email}), Região: {c.regiao.name}")
