'''
Jogo do Par ou Ímpar
2024.08.21
Autor: Caroline
'''

# Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT
from random import randint
from time import sleep

# Constantes, Variáveis e Listas
msgsInicio = ['Seja bem vind@ ao',
              'Jogo do PAR ou ÍMPAR',
              'Desenvolvido por: Caroline',
              'BOA SORTE >.<']
msgs = []
playAgain = ''
playerScore = 0
computerScore = 0

# Funções
def startParImpar(): # Dar um start no código
  while(True):
    clrScreen()
    displayHeader(msgsInicio)
    playParImpar()
    # Recomeçar o jogo
    playAgain = getUserOption('Deseja jogar novamente [s/n]')
    # Enquanto a resposta do user não for válida ele irá perguntar novamente, se for vália ele irá seguir com o jogo
    while not validateUserOption(playAgain, ['s', 'n', 'S', 'N']): 
      playAgain = getUserOption('Deseja jogar novamente [s/n]')
    if playAgain.lower() != 's':
      break

def displayMenu():
  msgs = ["Escolha: ",
     '[0] --> Par',
     '[1] --> Ímpar']
  displayLine()
  for msg in msgs:
    displayMsg(msg)
  displayLine()

def displayScore(typeScore, playerScore, computerScore):
  msgs = []
  msgs.append(typeScore)
  msgs.append(f'Player: {playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs)

def determineWinner(playerChoice, playerNumber, computerNumber):
  total = playerNumber + computerNumber
  result = ''
  if (total % 2 == 0 and playerChoice == '0') or (total % 2 != 0 and playerChoice == '1'):
    result = 'Você Ganhou :)'
  else:
    result = 'Você Perdeu :('
  msgs = [f'Número do Player: {playerNumber}', f'Número do PC: {computerNumber}', f'Total: {total}', result]
  displayHeaderT(msgs)
  return result # retornará o resultado

def playParImpar():
  playerScore = 0
  computerScore = 0
  # Enquanto a pontuação do computador e do player for menor que 2 execute o que estiver dentro do while
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua escolha') # Pega a resposta do usuário
    while not validateUserOption(playerChoice,['0','1']): # Valida a resposta do usuário
      displayMenu()
      playerChoice = getUserOption('Sua escolha')
    playerNumber = int(getUserOption('Escolha um número'))
    while not validateUserOption(str(playerNumber), [str(i) for i in range(6)]): # Valida a resposta do usuário
      playerNumber = int(getUserOption('Escolha um número'))
    computerNumber = randint(0,9) # Sorteia um número aleatório entre 0 e 5
    result = determineWinner(playerChoice, playerNumber, computerNumber) # Determina o resultado da partida
    if "Ganhou" in result: # Se o resultado for ganhou o próximo código será executado
      playerScore += 1
    elif "Perdeu" in result: # Se não, o próximo código será executado
      computerScore += 1
    if playerScore < 2 and computerScore < 2:
      displayScore("PLACAR", playerScore, computerScore)
    sleep(1)
  displayScore("PLACAR FINAL",playerScore,computerScore)
  if playerScore > computerScore:
    displayHeader(['Parabéns','YOU WIN!'])
  else:
    displayHeader(['Parabéns','YOU LOSE!'])


# Main