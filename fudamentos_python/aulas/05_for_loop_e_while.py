# print('=== FOR LOOP ===')
# for n in range(10):
#     print(n)

# print('=== WHILE ===')

# count = 0

# while count < 10:
#     count = count + 1
#     print(count)


# ===== ADVINHAR NÚMERO SECRETO =====
# secret_number = 10
# chances = 3

# for chance in range (chances):
#     attempt = int(input('Digite um número para advinhar qual é o número secreto: '))
#     if attempt == secret_number:
#         print(f'Parabéns, você acertou! O número secreto é {secret_number}.')
#         break
#     else:
#         if attempt >= chances:
#             print(f'\nVocê errou as {chance + 1} tentativas, o número secreto era: {secret_number}!\nJogo encerrado.')
#             break
#         else:
#             print(f'Você errou a tentativa de número {chance + 1}, tente novamente!')

clientes = [
    ('Leonardo', 'xxx-xxx-xxx.xx', 'xxx@gmail.com'),
    ('Giovanna', 'xxx-xxx-xxx.xx', 'xxx@gmail.com')
]

for nome, cpf, email in clientes:
    print('\n---------------------------------------------------------')
    print(f'Nome: {nome}, \nCPF: {cpf}, \nEmail: {email}')
    print('---------------------------------------------------------')

nome = 'Juliano'

for n in nome:
    print(n)