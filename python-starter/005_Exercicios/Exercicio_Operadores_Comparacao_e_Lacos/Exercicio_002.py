### Exercício 2
# Escreva um script que leia três números e mostre o maior e o menor deles.

print('-------------------------------------')

lst_numeros = []

while True:
    numero = int(input('Digite um número: '))
    lst_numeros.append(numero)

    if len(lst_numeros) == 3:
        break

print('-------------------------------------')
print('Sua lista contém os valores: {}'.format(lst_numeros))
print('-------------------------------------')

def ler_numeros():
    maior_numero = max(lst_numeros)
    menor_numero = min(lst_numeros)

    print('O menor número da lista é {} e o maior é {}'.format(menor_numero, maior_numero))

ler_numeros()

print('-------------------------------------')