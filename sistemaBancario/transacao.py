from connect.connect import Connect
import random
from datetime import datetime
from sistemaBancario.contabancaria import Conta
from datetime import datetime


date = datetime.now()
date_f = date.strftime('%d-%m-%Y %H:%M:%S')
inicio = 'baTzas'
meio = 'Tba'
final = random.randint(00000, 99999)
numeros = random.randint(100000000000, 999999999999)
id_trans = inicio + str(numeros) + meio + str(final)


class Transacao():

    def __init__(self):
        self.conexao = Connect()
        self.conn = self.conexao.conn
        self.qry = self.conexao.cur

    def depositar(self, conta, cpf):
        user_list = []

        self.qry.execute(
            "SELECT saldo FROM bancoBA WHERE CONTA=%s AND CPF=%s;", (conta, cpf))

        for x in self.qry:
            user_list.append(x)

        if user_list.__len__() == 1:

            saldo = str(user_list).strip('[]' '()' ',')
            saldo_v = float(saldo)
            valor = float(input('digite o valor para deposito: '))
            saldo_a = (saldo_v+valor)
            self.qry.execute(
                "UPDATE bancoBA SET SALDO=%s WHERE CONTA=%s AND CPF=%s;", (saldo_a, conta, cpf))

            self.qry.execute(
                "INSERT INTO transacao(tipo_transacao, conta_origem, cpf_origem, valor, id_transacao, data_hora) VALUES (%s, %s, %s, %s, %s, %s)", ('deposito', conta, cpf, valor, id_trans, date_f))
            self.conn.commit()
            print('Desposito efetuado com sucesso')
        else:
            print('conta ou senha incorreta \n verifique os dados e tente novamente')

    def sacar(self, conta, cpf,):
        user_list = []
        self.qry.execute(
            "SELECT saldo FROM bancoBA WHERE CONTA=%s AND CPF=%s;", (conta, cpf))

        for x in self.qry:
            user_list.append(x)
        if user_list.__len__() == 1:
            saldo = str(user_list).strip('[]' '()' ',')
            saldo_v = float(saldo)
            valor = float(input('digite o valor para saque: '))
            if (saldo_v - valor) < 0:
                print('saldo insulficiente')
            else:
                saldo_a = (saldo_v-valor)
                self.qry.execute(
                    "UPDATE bancoBA SET SALDO=%s WHERE CONTA=%s AND CPF=%s;", (saldo_a, conta, cpf))

                self.qry.execute(
                    "INSERT INTO transacao(tipo_transacao, conta_origem, cpf_origem, valor, id_transacao, data_hora ) VALUES (%s, %s, %s, %s, %s, %s)", ('saque', conta, cpf, valor, id_trans, date_f))
                self.conn.commit()
                print('saque efetuado com sucesso')
        else:
            print('conta ou senha incorreta \n verifique os dados e tente novamente')

    def transferir(self, cpf, conta, conta2, cpf2, valor):
        self.qry.execute(
            "SELECT saldo FROM bancoBA WHERE CONTA=%s AND CPF=%s;", (conta, cpf))
        for x in self.qry:
            saldo = str(x).strip('[]' '()' ',')
            saldo = float(saldo)
            saldo_transfere = saldo - valor

        if (saldo_transfere) >= 0:
            self.qry.execute(
                "UPDATE bancoBA set Saldo=%s WHERE CPF=%s AND Conta=%s", (saldo_transfere, cpf, conta))

            self.qry.execute(
                "UPDATE bancoBA set Saldo = saldo + %s WHERE CPF=%s AND Conta=%s", (valor, cpf2, conta2))

            self.qry.execute(
                "INSERT INTO transacao(tipo_transacao, conta_origem, cpf_origem, valor, conta_destino, cpf_destino, id_transacao, data_hora ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )", ('Transferencia', conta, cpf, valor, conta2, cpf2, id_trans, date_f))

            self.conn.commit()
            print('trasferencia realizada com sucesso')
        else:
            print('Não possui salto suficiente para transferencia!')
