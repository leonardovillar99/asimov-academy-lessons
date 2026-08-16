### Exercício 3
### Desenho um código que extraia o domínio de um e-mail informado.

email = input('Informe seu endereço de e-mail: ')
email = email.split('@')[1]
dominio = email.split('.')[0]

print(f'Seu domínio de e-mail é: {dominio.upper()}')