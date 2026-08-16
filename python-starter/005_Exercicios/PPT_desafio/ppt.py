import os
import random

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

lst_game_options = ['Pedra', 'Papel', 'Tesoura']

player_points = 0
computer_points = 0

while True:
    limpa_tela()
    print('=' * 43)
    print('Bem vindo ao jogo de Pedra, Papel e Tesoura')
    print('=' * 43)

    print('\nPLACAR:')
    print(f'Você: {player_points}')
    print(f'Computador: {computer_points}')
    
    player_choice = int(input('\nEscolha o seu lance: \n0 - Pedra | 1 - Papel | 2 - Tesoura\n'))
    computer_choice = random.randint(0, 2)

    player = lst_game_options[player_choice]
    computer = lst_game_options[computer_choice]

    if (computer_choice == 0 and player_choice == 2) or (computer_choice == 1 and player_choice == 0) or (computer_choice == 2 and player_choice == 1):
        print('\n===========================')
        print('Sua jogada: {} \nJogada do computador: {}'.format(player, computer))
        print('Você perdeu')
        computer_points += 1
        print('===========================\n')

        jogar_novamente = int(input('Jogar novamente? 0 - SIM | 1 - NÃO\n'))
        if jogar_novamente == 0:
            continue
        else:
            limpa_tela()
            break
    elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
        print('\n===========================')
        print('Sua jogada: {} \nJogada do computador: {}'.format(player, computer))
        print('Você ganhou')
        player_points += 1
        print('===========================\n')

        jogar_novamente = int(input('Jogar novamente? 0 - SIM | 1 - NÃO\n'))
        if jogar_novamente == 0:
            continue
        else:
            limpa_tela()
            break
    else:
        print('\n===========================')
        print('Sua jogada: {} \nJogada do computador: {}'.format(player, computer))
        print('Empate')
        print('===========================\n')

        jogar_novamente = int(input('Jogar novamente? 0 - SIM | 1 - NÃO\n'))
        if jogar_novamente == 0:
            continue
        else:
            limpa_tela()
            break