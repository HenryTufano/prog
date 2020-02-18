import random
op=5
while op!=0:
  op=int(input('Seja bem-vindo ao Pedra,papel e tesoura \nSelecione uma opção digitando o número equivalente:\n[2] – Jogar com a outro Jogador\n[1] – Jogar com a CPU\n[0] – Sair do programa\nDigite o valor da opção selecionada: '))
  if op==1 :
    j=int(input('Escolha uma das opção\n[1]Pedra\n[2]Papel\n[3]Tesoura\nDigite o valor da opção selecionada:'))
    cpu = random.randint(1, 3)
    if(j==1 and cpu==1)or(j==2 and cpu==2)or(j==3 and cpu==3):
              if(j==1 and cpu==1):
                print('O jogador 1 escolheu: Pedra\nO CPU escolheu: Pedra\nEmpate\n')
              elif(j==2 and cpu==2):
                print('O jogador 1 escolheu: Papel\nO CPU escolheu: Papel\nEmpate\n')
              elif(j==3 and cpu==3):
                print('O jogador 1 escolheu: Tesoura\nO CPU escolheu: Tesoura\nEmpate\n')                
    elif(j==1 and cpu==2)or(j==2 and cpu==3)or(j==3 and cpu==1):
              if(j==1 and cpu==2):
                print('O jogador 1 escolheu: Pedra\nO CPU escolheu: Papel\nVoçê perdeu\n')
              elif(j==2 and cpu==3):
                print('O jogador 1 escolheu: Papel\nO CPU escolheu: Tesoura\nVoçê perdeu\n')
              elif(j==3 and cpu==1):
                print('O jogador 1 escolheu: Tesoura\nO CPU escolheu: Pedra\nVoçê perdeu\n')
    elif(j==1 and cpu==3)or(j==2 and cpu==1)or(j==3 and cpu==1):
              if(j==1 and cpu==3):
                print('O jogador 1 escolheu: Pedra\nO CPU escolheu: Papel\nVoçê Venceu\n')   
              elif(j==2 and cpu==1):
                print('O jogador 1 escolheu: Papel\nO CPU escolheu: Pedra\nVoçê venceu\n')
              elif(j==3 and cpu==2):
                print('O jogador 1 escolheu: Tesoura\nO CPU escolheu: Papel\nVoçê venceu\n')
  elif op==2:
    j=int(input('Escolha uma das opção\n[1]Pedra\n[2]Papel\n[3]Tesoura\nDigite o valor da opção selecionada:'))
    j2=int(input('Escolha uma das opção\n[1]Pedra\n[2]Papel\n[3]Tesoura\nDigite o valor da opção selecionada:'))
    if(j==1 and j2==1)or(j==2 and j2==2)or(j==3 and j2==3):
              if(j==1 and j2==1):
                print('O jogador 1 escolheu: Pedra\nO jogador 2 escolheu: Pedra\nEmpate\n')
              elif(j==2 and j2==2):
                print('O jogador 1 escolheu: Papel\nO Jogador 2 escolheu: Papel\nEmpate\n')
              elif(j==3 and j2==3):
                print('O jogador 1 escolheu: Tesoura\nO jogador 2 escolheu: Tesoura\nEmpate\n') 
    elif(j==1 and j2==2)or(j==2 and j2==3)or(j==3 and j2==1):
              if(j==1 and j2==2):
                print('O jogador 1 escolheu: Pedra\nO jogador 2 escolheu: Papel\nJogador 2 Venceu\n')
              elif(j==2 and j2==3):
                print('O jogador 1 escolheu: Papel\nO Jogador 2 escolheu: Tesoura\nJogador 2 Venceu\n')
              elif(j==3 and j2==1):
                print('O jogador 1 escolheu: Tesoura\nO jogador 2 escolheu: Pedra\nJogador 2 Venceu\n')                
    elif(j==1 and j2==3)or(j==2 and j2==1)or(j==3 and j2==2):
              if(j==1 and j2==3):
                print('O jogador 1 escolheu: Pedra\nO jogador 2 escolheu: Tesoural\nJogador 1 Venceu\n')
              elif(j==2 and j2==1):
                print('O jogador 1 escolheu: Papel\nO Jogador 2 escolheu: Pedra\nJogador 1 Venceu\n')
              elif(j==3 and j2==2):
                print('O jogador 1 escolheu: Tesoura\nO jogador 2 escolheu: Papel\nJogador 1 Venceu\n') 
  else:
    print('Fim do jogo! Volte sempre!')