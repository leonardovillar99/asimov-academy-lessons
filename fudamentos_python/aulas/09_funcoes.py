print('--------- FUNÇÕES ---------')

# (def)
def somar_dois(n):
    return n + 2

print(somar_dois(10))

def my_function():
  print("Hello from a function")

my_function()


def calc_media(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4

    if media >= 6:
        status = 'Aprovado'
    else:
        status = 'Reprovado'
    
    return media, status

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))

# Desempacotar os valores retornados
media, status = calc_media(n1, n2, n3 , n4)
print(f'Sua média final é: {media:.1f} e seu resultado é: {status}')
# Saída: Sua média final é: 7.50 e seu resultado é: 

print()