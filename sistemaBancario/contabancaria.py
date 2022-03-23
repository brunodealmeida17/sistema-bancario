from datetime import datetime
from connect.connect import Connect
import random
from hashlib import md5


class Conta:

    def __init__(self):
        self.conexao = Connect()
        self.conn = self.conexao.conn
        self.qry = self.conexao.cur

    # Criando Usuario

    def create_user(self, nome, cpf, rg, saldo, email, senha,):

        senha_c = md5(senha.encode()).hexdigest()

        conta = random.randint(100000, 999999)
        agencia_v = "0001"
        self.qry.execute("INSERT INTO bancoBA (nome, cpf, rg, conta, agencia, saldo, email, senha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                         (nome, cpf, rg, conta, agencia_v, saldo, email, senha_c))

        print(f'sua conta é {conta} e sua agencia é {agencia_v}')

        self.conn.commit()

    def buscar_transacao(self, cpf):
        self.qry.execute(
            "SELECT cpf_origem, conta_origem, valor, tipo_transacao, id_transacao FROM transacao WHERE cpf_origem=%s;", (cpf,))
        return self.qry.fetchall()
