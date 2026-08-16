### Exercício 5
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. -- DONE
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
#1. Salário bruto.
#2. Quanto pagou ao INSS.
#3. Quanto pagou ao sindicato.
#4. O salário líquido.

salario_hora = float(input('Digite quanto você ganhar por hora: '))
horas_trabalhadas_mes = int(input('Digite quantas horas você trabalhou no mês: '))

salario_bruto = (salario_hora * horas_trabalhadas_mes)

desconto_irrf = (salario_bruto * 0.11)
desconto_inss = (salario_bruto * 0.08)
desconto_sindicato = (salario_bruto * 0.05)

salario_liquido = ((salario_bruto) - (desconto_irrf + desconto_inss + desconto_sindicato))

print(f'Seu salário bruto é de R${salario_bruto:.2f}\nVocê pagou R${desconto_irrf:.2f} de IRRF, R${desconto_inss:.2f} de INSS e R${desconto_sindicato:.2f} de sindicato.')
print(f'Seu salário líquido do mês é de R${salario_liquido:.2f}')