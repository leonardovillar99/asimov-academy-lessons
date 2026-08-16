### Exercício 1
# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#- A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
#- A mensagem "Reprovado", se a média for menor do que 7;
#- A mensagem "Aprovado com Distinção", se a média for igual a 10.

def pede_nota(numero):
    while True:
        nota = float(input(f'Digite a nota {numero}: '))
        if nota >= 0 and nota <= 10:
            return nota
        print('Nota inválida. Digite um valor entre 0 e 10.')

def calcula_media():
    print('-------------------------------------')
    print('INICIANDO SISTEMA DE CALCULO DE MÉDIA')
    print('-------------------------------------')

    n1 = pede_nota(1)
    n2 = pede_nota(2)
    n3 = pede_nota(3)
    n4 = pede_nota(4)

    media = (n1 + n2 + n3 + n4) / 4

    print('-------------------------------------')
    print('Média final: {}'.format(media))

    if media == 10:
        print('Aprovado com Distinção')
    elif media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')

calcula_media()

print('-------------------------------------')