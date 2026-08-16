# LISTAS e TUPLAS

frutas = ['Maçã', 'Banana', 'Melão', 'Abacaxi', 'Manga']

print(frutas[1:3])

print(frutas[3])
print(len(frutas))
print(frutas[-1])

print('===========')

print(frutas)
frutas[0] = 'Abacate'
print(frutas)

print('===========')

del frutas[1]
print(frutas)

print('===========')

alunos = ('Leonardo', 'João', 'José', 'Rafael', 'Gabriel')

print(alunos[1:3])

print(alunos[1])

nome = 'Leonardo'

print(tuple(nome))