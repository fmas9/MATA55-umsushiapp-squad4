from backend.PoC.domain.entities.locale import Locale
locales = []

def cadastrar_regiao(): #cadastro pelo gerente
    name = input("Nome da região: ")
    locale = Locale(name)
    locales.append(locale)
    print(f"✅ Região '{name}' cadastrada com sucesso!")

def listar_regioes():
    if not locales:
        print(" Nenhuma região cadastrada.")
    else:
        print("Regiões cadastradas:")
        for i, r in enumerate(locales, start=1):
            print(f"{i}. {r.nome}")