lista_alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista_palavra = []

# Entrada de 5 letras válidas
while len(lista_palavra) < 5:
    letra = input('Digite uma letra do alfabeto (A-Z): ').upper()

    if letra not in lista_alfabeto:
        print('Caractere inválido. Digite novamente.')
        continue

    lista_palavra.append(letra)

# Monta a palavra final
palavra = "".join(lista_palavra)
print("Palavra digitada:", palavra)

# Entrada da chave da cifra
chave = int(input('Digite uma chave de 1 a 3: '))

# Aplica a cifra de César
nova_palavra = ""

for letra in palavra:
    indice = lista_alfabeto.index(letra)          # encontra posição
    novo_indice = (indice + chave) % 26           # deslocamento cíclico
    nova_letra = lista_alfabeto[novo_indice]      # letra resultante
    nova_palavra += nova_letra

# Exibe resultado
print("Palavra cifrada:", nova_palavra)
