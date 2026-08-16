### Exercício 4 
# Faça um programa para uma loja de tintas. A pessoa informa a área em m2 que deseja pintar, e o script calculará a 
# quantidade de latas de tinta que a pessoa deve comprar e o valor. Considere que cada litro de tinta pinta 3m2, que cada lata contém 18L e que custa R$ 80.

import math

area = float(input('Informe a área em m² total que deseja pintar: '))
litro_lata = 18
preco_lata = 80

print('================================================================')

litros_gastos = (area / 3) # Outra forma de calcular -> (area / litro_lata) * 6
total_latas = math.ceil(litros_gastos / litro_lata)
valor_total = (total_latas * preco_lata)

print(f'Para pintar um total de {area} m² será gasto {litros_gastos:.2f} litros de tinta')
print(f'Você precisará comprar {total_latas} lata(s) de tinta')
print(f'Para {total_latas} lata(s) o valor total será de R${valor_total:.2f}')

print('================================================================')