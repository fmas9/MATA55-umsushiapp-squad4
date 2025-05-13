def validar_pagamento(numero_cartao, cvv, validade, tipo):
    if not numero_cartao.isdigit() or len(numero_cartao) !=16:
        return "Número de cartão invalido."

    if not cvv.isdigit() or len(cvv) !=3:
        return "cvv invalido."
    if tipo.lower() not in ['credito','debito']:
        return "Pagamento validado com sucesso! Pedido confirmado."

    try:
        mes, ano = map(int, validade.split('/'))
        if not (1 <= mes <= 12):
            return "MES VALIDADOs"
    except: 
        return "Formado de validade invalido"

    return "Pagamento validado com sucesso"

print("Bem vindo ao SUSHI")
nome = input ("Digite seu nome:")
pedido = input("Oque deseja pedir:")

numero = input("Digite o numero do cartao com 16 digitos:")
cvv = input("Digite o cvv:")
validade = input("digite a validade(MM/AA):")
tipo = input("tipo:")

resposta = validar_pagamento(numero, cvv,validade, tipo)
print(f"\n {resposta}")

if "validado" in resposta:
            print(f"Obrigado, {nome}! seu pedido esta sendo preparado")