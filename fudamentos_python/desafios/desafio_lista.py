numbersList = [1, 2, 5, 7, 9, 12, 15, 26]
total = 0

for n in numbersList:
    total += n
print(total)


#print(sum(numbersList))
#print(max(numbersList))

print('========================')

names = ['Leonardo', 'Fernando', 'Alan', 'Jose', 'Wilton', 'João']
nameListGraterThan5 = []
nameListLessThan5 = []

for i in names:
    if len(i) >= 5:
        nameListGraterThan5.append(i)
    else:
        nameListLessThan5.append(i)

print(f'Nomes com mais de 5 caracteres: {nameListGraterThan5}')
print(f'Nomes com menos de 5 caracteres: {nameListLessThan5}')

print('========================')

numbersList = [1, 2, 10, 38, 17, 12, 15, 8]

maximo = numbersList[0]

for i in numbersList:
    if i > maximo:
        maximo = i

print(f'O valor máximo dos valores {numbersList} é: {maximo}')

print('========================')

my_list = [1, 2, 3, 2, 4, 1, 5]
seen = set()
duplicates = []

for item in my_list:
    if item in seen:
        duplicates.append(item)
    else:
        seen.add(item)
print(f"Duplicate values: {duplicates}")