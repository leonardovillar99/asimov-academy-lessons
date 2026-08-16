import os
import time

def soma():
    n1 = float(input('\nQual o primeiro valor?\n'))
    n2 = float(input('Qual o segundo valor?\n'))
    res = (n1 + n2)
    print(f'\n{n1} + {n2} = {res}\n')

def subtracao():
    n1 = float(input('\nQual o primeiro valor?\n'))
    n2 = float(input('Qual o segundo valor?\n'))
    res = (n1 - n2)
    print(f'\n{n1} - {n2} = {res}\n')

def multiplicacao():
    n1 = float(input('\nQual o primeiro valor?\n'))
    n2 = float(input('Qual o segundo valor?\n'))
    res = (n1 * n2)
    print(f'\n{n1} x {n2} = {res}\n')

def divisao():
    n1 = float(input('\nQual o primeiro valor?\n'))
    n2 = float(input('Qual o segundo valor?\n'))
    res = (n1 / n2)
    print(f'\n{n1} / {n2} = {res}\n')

def exponenciacao():
    n1 = float(input('\nQual o primeiro valor?\n'))
    n2 = float(input('Qual o segundo valor?\n'))
    res = (n1 ** n2)
    print(f'\n{n1} ** {n2} = {res}\n')

def mostra_menu():
    print('0 : Soma \n1 : Subtração \n2 : Multiplicação \n3 : Divisão \n4 : Exponenciação')

while True:
    mostra_menu()

    while True:
        operacao = int(input('\nDigite a operação que deseja realizar: '))

        if operacao == 0 or operacao == 1 or operacao == 2 or operacao == 3 or operacao == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            mostra_menu()
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            mostra_menu()
            print('\nOpção inválida, digite apenas os números disponíveis acima para cada operação')
    
    match operacao:
        case 0:
            print('\nOperação de soma escolhida.')
            soma()
        case 1:
            print('\nOperação de subtração escolhida.')
            subtracao()
        case 2:
            print('\nOperação de multiplicação escolhida.')
            multiplicacao()
        case 3:
            print('\nOperação de divisão escolhida.')
            divisao()
        case 4:
            print('\nOperação de exponenciação escolhida.')
            exponenciacao()
        case _:
            print('\nOpção Inválida\n')

    print('==========================')

    opcao = int(input('\nDeseja fazer outra operação? 0 - SIM, 1 - NÃO\n'))
        
    if opcao == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    elif opcao == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Encerrando Calculadora...')

        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        break