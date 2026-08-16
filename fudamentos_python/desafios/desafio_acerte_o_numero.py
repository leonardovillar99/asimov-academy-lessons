## DESAFIO ACERTE O NÚMERO (IF)

secretNumber = int(input('Escolha um número secreto: '))
guessNumber = int(input('Faça um chute para advinhar o número secreto: '))

if secretNumber == guessNumber:
    print('Uauuu, Você acertou de primeira, parabéns!!!')
    print(f'O número secreto é: {secretNumber}.')
elif secretNumber != guessNumber:
    print('Você errou, tente outra vez.')
    if secretNumber < guessNumber:
        print(f'O número {guessNumber} é maior do que o número secreto')
    else:
        print(f'O número {guessNumber} é menor do que o número secreto')

    guessNumber2 = int(input('Faça um segundo chute para advinhar o número secreto: '))
    if secretNumber == guessNumber2:
        print('Você acertou na segunda tentativa, parabéns!!!')
        print(f'O número secreto é: {secretNumber}.')
    elif secretNumber != guessNumber: 
        print('Você errou, tente outra vez.')
        if secretNumber < guessNumber2:
            print(f'O número {guessNumber2} é maior do que o número secreto')
        else:
            print(f'O número {guessNumber2} é menor do que o número secreto')

        guessNumber3 = int(input('Faça um terceiro chute para advinhar o número secreto: '))
        if secretNumber == guessNumber3:
            print('Você acertou na terceira tentativa, parabéns!!!')
            print(f'O número secreto é: {secretNumber}.')
        else:
            print('Você perdeu, todas as 3 tentativas se esgotaram :(')
            print(f'O número secreto é: {secretNumber}.')

## DESAFIO ACERTE O NÚMERO (WHILE)