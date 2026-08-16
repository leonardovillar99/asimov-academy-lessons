capitais = {
    'Brasil': 'Brasília',
    'França': 'Paris',
    'Japão': 'Tóquio',
    'Inglaterra': 'Londres'
}

print('Brasil' in capitais)

while True:
    opt = input('Escolha uma das opções 1 ou 2 (se quiser sair pressione q): ')

    if opt in ('1', '2'):
        print(f'Opção selecionada: {opt}')
        break
    elif opt in ['q']:
        print('Saindo...')
        break
    else:
        print(f'Opção {opt} inválida, tente novamente.')
        