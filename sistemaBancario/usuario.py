from connect.connect import Connect
from hashlib import md5
from validador.validador import *


class Usuario:

    def __init__(self):
        self.conexao = Connect()
        self.conn = self.conexao.conn
        self.qry = self.conexao.cur

    def findone(self):
        self.qry.execute("SELECT * FROM USUARIO;")
        return self.qry.fetchall()

    def create_user(self, nome, cpf, email, senha):
        senha_c = validar_senha(senha)
        nome_v = validar_nome(nome)
        cpf_v = validar_cpf(cpf)
        email_v = validar_email(email)

        self.qry.execute(
            "INSERT INTO usuario (nome, cpf, email, senha) VALUES (%s, %s, %s, %s);", (nome_v, cpf_v, email_v,
                                                                                       senha_c))

        self.conn.commit()

    def update(self, nome, cpf, email, senha):
        senha_c = validar_senha(senha)
        nome_v = validar_nome(nome)
        cpf_v = validar_cpf(cpf)
        email_v = validar_email(email)

        self.qry.execute(
            "UPDATE usuario SET nome=%s, cpf=%s, email=%s , senha=%s WHERE id=%s;", (nome_v, cpf_v, email_v,
                                                                                     senha_c, id,))

        self.conn.commit()

    def delete(self, cpf):
        self.qry.execute("DELETE FROM usuario WHERE cpf=%s;", (cpf,))

        self.conn.commit()

    def __del__(self):
        del self
