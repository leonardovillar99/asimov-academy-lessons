correct_username = 'Leonardo'
correct_password = 'leo123'

username = input('Digite seu nome de usuário: ')
password = input('Digite sua senha: ')

if username == correct_username:
    if password == correct_password:
        print(f'Login realizado com sucesso, seja bem-vindo {username}.')
    else:
        print(f'Senha incorreta, tente novamente.')
else:
    print('Usuário não cadastrado no sistema.')
    