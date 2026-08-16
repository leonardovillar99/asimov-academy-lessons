### Exercício 3 
#Nome na vertical em escada. 
#F
#FU
#FUL
#FULA
#FULAN
#FULANO

nome = str(input('Digite o seu nome: ')).upper()
lst_nome = []

for l in nome:
    lst_nome.append(l)
    print("".join(lst_nome))