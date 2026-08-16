capitais = {
    'Rio Grande do Norte': 'Natal',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'São Paulo': 'São Paulo',
    'Santa Catarina': 'Florianópolis ',
    'Minas Gerais': 'Belo Horizonte'
}

tentar_novamente = True
rodadas = 0
acertos = 0

for estado, capital in capitais.items():
    if not tentar_novamente:
        break

    rodadas += 1
    print(f'Qual a capital do Estado {estado}?')

    resposta = input('Digite a resposta: ')

    if resposta.lower() == capital.lower():
        print('Você acertou!')
        acertos += 1
    else:
        print(f'Você errou, a capital de {estado} é {capital}')

    while tentar_novamente:
        opcao = input('Deseja continuar? Digite (s/n): ').lower()
        if opcao not in ['s', 'n']:
            print('Responda apenas com "s" para sim ou "n" para não.')        
            continue
        elif opcao == 'n':
            tentar_novamente = False
        break

calc_porcentagem = acertos / rodadas * 100

print(f'Você acertou {acertos} respostas de {rodadas} rodadas.\nPorcentagem de acertos: {calc_porcentagem:.2f}%')