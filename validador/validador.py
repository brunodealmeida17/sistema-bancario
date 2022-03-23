from getpass import getpass
import re
from hashlib import md5


def validar_nome(nome):
    tamanho_nome = len(nome)
    if tamanho_nome <= 32:
        return nome
    else:
        print('nome invalido insira nome novamente!')
        validar_nome()


def validar_email(email):
    if re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', email):
        return email
    else:
        print("E-mail inválido")
        validar_email()


def validar_cpf(cpf):
    cpfd = int(cpf)
    while True:
        # cpf = '16899535009'
        novo_cpf = cpf[:-2]  # Elimina os dois últimos digitos do CPF
        reverso = 10  # Contador reverso
        total = 0

        # Loop do CPF
        for index in range(19):
            if index > 8:  # Primeiro índice vai de 0 a 9,
                index -= 9  # São os 9 primeiros digitos do CPF

            # Valor total da multiplicação
            total += int(novo_cpf[index]) * reverso

            reverso -= 1  # Decrementa o contador reverso
            if reverso < 2:
                reverso = 11
                d = 11 - (total % 11)

                if d > 9:  # Se o digito for > que 9 o valor é 0
                    d = 0
                total = 0  # Zera o total
                novo_cpf += str(d)  # Concatena o digito gerado no novo cpf

        # Evita sequencias. Ex.: 11111111111, 00000000000...
        sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

        # Descobri que sequências avaliavam como verdadeiro, então também
        # adicionei essa checagem aqui
        if cpf == novo_cpf and not sequencia:
            return cpf
        else:
            print('CPF Inválido! teste novamente')
            break


def validar_senha(senha):
    senha_c = md5(senha.encode()).hexdigest()
    while True:

        if senha.islower():
            print("A senha deve ter pelo menos um caractere MAIUSCULO: ")
            break
        elif len(senha) < 7:
            print("A senha deve ter pelo menos 8 caracteres: ")
            break
        elif senha.isalpha():
            print("Necessita de um numero: ")
            break
        elif senha.isalnum():
            print("Necessita de um Caractere especial: ")
            break
        else:
            return senha_c
