'''
Projeto Jogo Pedra Papel Tesoura
2024.08.13
Autor: Caroline
'''

# --> Bibliotecas
# Importa a funções do arquivo module.py
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption, displayHeaderT
from ppt import startPPT
from parimpar import startParImpar
#from parimpar import startParimpar


# --> Constantes, Variáveis e Listas

# --> Funções

# --> Main
msgs = ['Seja Bem-vind@ aos Jogos', 'PEDRA-PAPEL-TESOURA', 'PAR OU ÍMPAR']
displayHeader(msgs)
msgs = ['Digite 0 ---> Sair',
        'Digite 1 ---> Pedra-Papel-Tesoura',
        'Digite 2 ---> Par ou Ímpar']
displayHeaderT(msgs)
opUser = getUserOption('Sua escolha')
while not validateUserOption(opUser, ['0', '1', '2']):
  opUser = getUserOption('Sua escolha')
if(opUser == '1'):
  startPPT()
elif(opUser == '2'):
  startParImpar()
else:
  displayMsg('Até a Próxima...')

startPPT()
