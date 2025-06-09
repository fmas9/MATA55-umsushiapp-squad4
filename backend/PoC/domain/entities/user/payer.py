class Cliente: #cadastro do paciente
    def __init__(self, nome, email,senha, regiao, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.regiao = regiao
        self.telefone = telefone