# PoC (Prova de Conceito) do Sistema de Pagamentos API (FastAPI + Mock)

Esse diretório contém um serviço API em /PoC para prova de conceito do UML proposto no diretório /documentacao, o projeto foi desenvolvido usando **FastAPI**, simulando operações de **Pedidos (Orders)** e **Pagamentos (Payments)** com repositórios **mockados**.

## 📚 Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**
- **Uvicorn** (servidor ASGI)
- **Pydantic**

## ✨ Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/fmas9/MATA55-umsushiapp-squad4.git
```

2. Pré-requisito: Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode a aplicação localmente:

```bash
uvicorn adapters.inbound.fastapi_adapter:app --reload
```

4. Futuramente: Será possível acessar a documentação automática (Swagger):

- `http://localhost:8000/docs`

## 📌 Rotas Disponíveis para teste no CURL ou Insomnia, Postman

### ➔ Pedidos (Orders)

#### Criar um Pedido

- **POST** `/orders`
- Cria um novo pedido.

**Body da requisição:**

```json
{
  "items": ["Chessburger", "Coke"],
  "total_value": 19.90
}
```

**Resposta:**

```json
{
  "id": "uuid-gerado",
  "order_date": "2025-04-28T12:00:00",
  "items": ["Chessburger", "Coke"],
  "total_value": 19.9,
  "status": "InProgress"
}
```

#### Listar Pedidos

- **GET** `/orders`
- Retorna todos os pedidos registrados.

**Resposta:**

```json
[
  {
    "id": "uuid-gerado",
    "order_date": "2025-04-28T12:00:00",
    "items": ["Item 1", "Item 2"],
    "total_value": 100.0,
    "status": "InProgress"
  }
]
```

### ➔ Pagamentos (Payments)

#### Criar um Pagamento

- **POST** `/payments`
- Cria um novo pagamento para um pedido.

**Body da requisição:**

```json
{
  "order_id": "ID GERADO DO PEDIDO FEITO",
  "amount": 29.90,
  "payment_type": "credit"
}
```

**Tipos válidos para `payment_type`:**
- `credit`
- `debit`
- `pix`

**Resposta:**

```json
{
  "id": "uuid-gerado",
  "order_id": "ID GERADO DO PEDIDO PAGO",
  "amount": 29.9,
  "payment_type": "credit",
  "payment_date": "2025-04-28T12:10:00"
}
```

#### Listar Pagamentos

- **GET** `/payments`
- Retorna todos os pagamentos efetuados.

**Resposta:**

```json
[
  {
    "id": "uuid-gerado",
    "order_id": "ID GERADO",
    "amount": 29.9,
    "payment_type": "credit",
    "payment_date": "2025-04-28T12:10:00"
  }
]
```

## 📊 Observações de Implementação

- O repositório é **mockado** (em memória).
- Pode ser adaptado para integração com bancos de dados reais.
- Estrutura organizada em **modelo hexagonal**:
  - Entities, DTOs, Enums (domínio)
  - Adapters Inbound (FastAPI)
  - Adapters Outbound (Mock Repository)

## 💡 Futuras Melhorias

- Adicionar autenticação JWT
- Implementar paginação real nas listagens
- Persistência com banco de dados relacional (ex: PostgreSQL)

---