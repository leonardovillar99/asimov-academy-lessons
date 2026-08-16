# Escreva o seu código aqui :-)
"""
for i in range (11):
    print(i);

print('-----------')

a = 1
while a < 11:
    print(a);
    a+= 1;

print('-----------')
"""

count_erros = 0
lst_tentativas = []

while True:
    secret = input('Digite sua senha: ')

    if secret == 'admin123':
        print('Senha correta.')
        break
    else:
        print('Senha incorreta, tente novamente.')
        count_erros += 1
        lst_tentativas.append(secret)

        if count_erros == 3:
            print(f'Tentativas {count_erros} excedidas, usuário bloqueado.')
            print(f'Senhas digitadas: {lst_tentativas}.')
            break

print(len(lst_tentativas[0]))
print(f'{lst_tentativas[1:3]}.')
