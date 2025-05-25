from backend.PoC.domain.entities.locale import Regiao
regioes = []

def cadastrar_regiao(): #cadastro pelo gerente
    nome = input("Nome da região: ")
    regiao = Regiao(nome)
    regioes.append(regiao)
    print(f"✅ Região '{nome}' cadastrada com sucesso!")

def listar_regioes():
    if not regioes:
        print(" Nenhuma região cadastrada.")
    else:
        print("Regiões cadastradas:")
        for i, r in enumerate(regioes, start=1):
            print(f"{i}. {r.nome}")