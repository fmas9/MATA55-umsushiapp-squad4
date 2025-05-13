import qrcode
import crcmod
import random
import string
import time

def gerar_id_transacao():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def gerarPayload(nome, chave_pix, valor, cidade, id_transacao, fileNameQrcode):
    valor = valor.replace(",", ".")  # Formato correto
    conta_empresa_tam = f'0014BR.GOV.BCB.PIX01{len(chave_pix):02}{chave_pix}'
    valor_compra_tam = f'{len(valor):02}{float(valor):.2f}'
    addDataField_tam = f'05{len(id_transacao):02}{id_transacao}'
    
    payloadFormat = '000201'
    merchantAccount = f'26{len(conta_empresa_tam):02}{conta_empresa_tam}'
    transactionAmount = f'54{valor_compra_tam}'
    merchantName = f'59{len(nome):02}{nome}'
    merchantCity = f'60{len(cidade):02}{cidade}'
    addDataField = f'62{len(addDataField_tam):02}{addDataField_tam}'
    crc16 = '6304'

    payload = f'{payloadFormat}{merchantAccount}52040000' \
              f'5303986{transactionAmount}5802BR' \
              f'{merchantName}{merchantCity}{addDataField}{crc16}'

    payload_completa = gerarCrc16(crc16, payload)

    imgQrcode = qrcode.make(payload_completa)
    imgQrcode.save(fileNameQrcode)

    return payload_completa

def gerarCrc16(crc16Code, payload):
    crc16 = crcmod.mkCrcFun(poly=0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)
    crc16Code_formatado = hex(crc16(payload.encode('utf-8'))).replace('0x', '').upper().zfill(4)
    
    return f'{payload}{crc16Code_formatado}'

# Entrada do usuário
nome = "Um Sushi"
chave_pix = "umsushi@gmail.com"
cidade = "Lauro de Freitas"
id_transacao = gerar_id_transacao()  # ID aleatório
valor = input("Digite o valor do pagamento (ex: 25.99): ")

# Nome de arquivo único para cada QR Code
fileNameQrcode = f'qrcode_{int(time.time())}.png'

payload = gerarPayload(nome, chave_pix, valor, cidade, id_transacao, fileNameQrcode)

print("Chave copia e cola:", payload)


#Transformando o qrcode em um arquivo json
import json

# Criando um dicionário com os dados do PIX
dados_pix = {
    "nome": nome,
    "chave_pix": chave_pix,
    "cidade": cidade,
    "id_transacao": id_transacao,
    "valor": valor,
    "payload": payload,  # O código copia-e-cola gerado
    "qrcode_imagem": fileNameQrcode  # Nome do arquivo gerado
}

# Convertendo para JSON
json_pix = json.dumps(dados_pix, indent=4)

# Salvando o JSON em um arquivo
with open("pix_qrcode.json", "w") as arquivo_json:
    arquivo_json.write(json_pix)

print("JSON gerado com sucesso!")