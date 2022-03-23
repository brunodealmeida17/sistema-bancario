from venv import create
import pprint
from sistemaBancario.contabancaria import Conta
from sistemaBancario.usuario import Usuario
from sistemaBancario.transacao import Transacao

User = Conta()
#User.create_user('Bruno almeida', '04352598143', '7027781', 50, 'teste@teste.com', '142536')
#User.create_user('Lara monique', '70084715642', '7027781', 580, 'teste@teste1.com', '1425136')
rows = User.buscar_transacao('04352598143')

print("\n -- Lista de Transferencias -- \n")
pprint.pprint(rows)


#c1 = Transacao()

#c1.depositar('437978', '04352598143')

#c1.transferir('04352598143', '437978', '452673', '70084715642', 30)
#c1.transferir('70084715642', '452673', '437978', '04352598143', 150)

#c1.sacar('437978', '04352598143')
