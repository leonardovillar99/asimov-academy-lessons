import os
import time

def mostra_menu():
    print('===============================')
    print('Bem vindo à locadora de carros!')
    print('===============================')
    print('O que deseja fazer?')

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def continuar():
    continuar = int(input('0 - CONTINUAR | 1 - SAIR\n'))
    limpa_tela()
    return continuar

lst_carros = {  'Chevrolet Tracker': 120, 
                'Chevrolet Onix': 90, 
                'Chevrolet Spin': 150, 
                'Hyundai HB20': 85, 
                'Hyundai Tucson': 120, 
                'Fiat Uno': 60, 
                'Fiat Mobi': 70, 
                'Fiat Pulse': 130
            }

lst_carros_alugados = {}

def mostra_carros():
    count = 0
    for m, v in lst_carros.items():
        count += 1
        print(f'[{count - 1}] {m} - R$ {v} /dia')
            
    print('\n===============================')

def mostra_carros_alugados():
    count = 0
    for m, v in lst_carros_alugados.items():
        count += 1
        print(f'[{count - 1}] {m} - R$ {v} /dia')

while True:
    mostra_menu()
    opcao = int(input('0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro\n'))

    if opcao == 0:
        limpa_tela()
        mostra_carros()
        if continuar() == 0:
            continue
        else:
            break        
    elif opcao == 1:
        nome_carro = list(lst_carros.keys())
        valor_carro = list(lst_carros.values())

        limpa_tela()
        print('[ ALUGAR ] Dê uma olhada em nosso portifólio.\n')
        mostra_carros()

        codigo = int(input('Escolha o código do carro:\n'))
        dias = int(input('Escolha por quantos dias deseja alugar:\n'))

        carro_escolhido = nome_carro[codigo]
        valor = valor_carro[codigo]
        valor_total = (valor * dias)

        limpa_tela()
        print(f'Você escolheu {carro_escolhido} por {dias} dia(s).')
        print(f'O aluguel totalizaria R$ {valor_total}. Deseja alugar?')

        alugar = int(input('\n0 - SIM | 1 - NÃO\n'))

        if alugar == 0:
            remove_carro = lst_carros.pop(carro_escolhido)
            add_alugado = lst_carros_alugados[carro_escolhido] = valor
            print('\nParabéns você alugou o {} por {} dia(s).\n'.format(carro_escolhido, dias))
            print('===============================')

            if continuar() == 0:
                continue
            else:
                break      
        else:
            break
    elif opcao == 2:
        limpa_tela()
        if len(lst_carros_alugados) == 0:
            print('Não existem carros alugados.')
            time.sleep(2)
            limpa_tela()
        else:
            print('Segue a lista de carros alugados. Qual você deseja devolver?')
            mostra_carros_alugados()

            devolver = int(input('\nEscolha o código do carro que deseja devolver:\n'))
            add_alugado = lst_carros[carro_escolhido] = valor
            remove_carro = lst_carros_alugados.pop(carro_escolhido)

            print('Obrigado por devolver o carro {}.'.format(carro_escolhido))

            print('\n===============================')
            if opcao == 0:
                limpa_tela()
                mostra_carros()
            if continuar() == 0:
                continue
            else:
                break 
    else:
        limpa_tela()
        continue    