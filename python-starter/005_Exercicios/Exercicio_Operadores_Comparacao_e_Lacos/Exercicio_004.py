### Exercício 4
# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# (o próximo termo, a partir do terceiro, é sempre gerado a partir do somatório dos últimos dois). 
# Faça um programa capaz de gerar a série até o n−ésimo termo (onde o valor n deve ser inserido pelo usuário).

# FORMULA -> F(n) = F(n-1) + F(n-2)

tamanho = int(input("Digite o tamanho da série de fibonnaci: "))
fibo = [1,1]
for i in range(tamanho):
  fibo.append(fibo[-1] + fibo[-2])
  print(fibo)