### Exercício 1
### Utilizando o built-in method input(), crie um programa que receba a altura e o peso de uma pessoa e imprima na tela o IMC da mesma.

altura = float(input('Digite o sua altura: '))
peso = int(input('Digite o seu peso: '))

imc = (peso / (altura ** 2))

print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Normal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 35:
    print('Obesidade grau I')
elif imc >= 35 and imc < 40:
    print('Obesidade grau II (Severa)')
else:
    print('Obesidade grau III (Mórbida)')