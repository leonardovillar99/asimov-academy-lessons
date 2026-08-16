produtos = {
    'banana': 4.5,
    'maçã': 8.2,
    'pera': 3.3
}

#print(dir(produtos)) # (Dir) Método que retorna uma lista dos métodos disponíveis para utilização com dicionários
#produtos.clear() # (Clear) Método que limpa o dicionário

print('---------------')

for produto in produtos.keys(): # (Keys) Método que retorna as chaves do dicionário
    print (produto)

print('---------------')

for valor in produtos.values(): # (Values) Método que retorna os valores do dicionário
    print (valor)

print('---------------')

for par in produtos.items(): # (Items) Retorna as tuplas com chaves e valores associados
    print(par)

print('---------------')

for k, v in produtos.items(): # (Items) Retorna as tuplas com chaves e valores associados
    print(f'{k} -> {v}')

print('---------------')

# (Update) Método que atualiza um dicionário com valores de outro dicionário
novos_produtos = {
    'arroz': 31.99,
    'feijão': 8.99,
    'melancia': 15.99
}
produtos.update(novos_produtos)
print(produtos)

print('---------------')

produtos_copia = produtos.copy()
produtos_copia['morango'] = 3.30
print(produtos_copia)

print('---------------')

# (Get) Método que retorna especificamento o valor da chave passada como parâmetro

print(produtos.get('banana'))
print(produtos['banana'])
print(produtos.get('pera'))
print(produtos['pera'])

print('---------------')

print(help(produtos.get)) # (Help) Retorna um descritivo com detalhes do método declarado

print('---------------')

# (as_integer_ratio) Métodos que retorna dois inteiros que quando divididos vão gerar o valor de saída
x = 4.5
print(x.as_integer_ratio())

y= 38.125
print(y.as_integer_ratio())

print('---------------')

# (is_integer) Métodos que retorna verdadeiro ou falso na verificação se o número passado como parâmetro é inteiro ou não
x = 4.5
print(x.is_integer())

print('---------------')

# (upper e lower) Métodos que retornam o valor como maiusculo e minusculo
palavra = 'Olá MunDo!'
print(palavra.upper())

palavra = 'Olá MunDo!'
print(palavra.lower())

print('---------------')

# (endswith e startswith) Métodos que retorna o conteúdo final e inicial de um texto no parâmetro passado
arquivo = '2023_01_01_NotaFiscal.pdf'
print(arquivo.endswith('.pdf'))
print(arquivo.endswith('.docx'))

print(arquivo.startswith('2023'))
print(arquivo.startswith('2022'))

if arquivo.startswith('2023') and arquivo.endswith('.pdf'):
    print('Nota fiscal encontrada')

print('---------------')

# (count) Método que realiza a contagem do parâmetro passado
texto = 'Hoje em dia todo dia é um novo dia. Mais um dia chega. Dia!'
print(texto.count('a'))
print(texto.count('dia'))
print(texto.lower().count('dia'))

print('---------------')

# (find e index) Métodos que retornam a posição do parâmetro passado dentro do texto
seq = 'aaaaaabaaaaaaaaabaaa'
print(seq.index('b'))
print(seq.find('c'))
print(seq[seq.find('b'):])

print('---------------')

# (isdigit e isalpha) Métodos que retornam se existem apenas números ou apenas letras do alfabeto
s1 = '942578865'
print(s1.isdigit())
s1 = 'Leonardo'
print(s1.isalpha())

print('---------------')

# (replace) Método que troca um caractere por outro dentro de um texto
frase = 'Estou estudando Python!'
print(frase.replace('!', '.'))
print(frase.replace('Python', 'Javascript'))

print('---------------')

# (split) Método que converte um string para uma lista
linha = 'Item1        Item2        Item3'
print(linha.split())

linha2 = 'Item1;Item2;Item3'
print(linha2.split(';'))

print('---------------')

# (join) Método que passa uma lista de string de volta para uma string
nomes = ['Marcelo', 'Paulo', 'João']
print('------'.join(nomes))

print('---------------')

# Métodos de listas e tuplas
tup = (0, 0, 0, 1, 0, 1, 0)
print(tup.index(1))
print(tup.count(0))

print('---------------')

l1 = [0, 0, 0, 1, 0, 1, 0]
l2 = l1.copy()
l1.clear()
print(l1)
print(l2)

print('---------------')

# (Append) Método que adiciona um elemento no fim da lista
for n in range(10):
    l1.append(n * 2)
print(l1)

l1.append('hello')
print(l1)

valores = [10, 30, -90, -1, 0, 1]
valores_positivos = []

for valor in valores:
    if valor > 0:
        valores_positivos.append(valor)
print(valores_positivos)

print('---------------')

# (Extend) Método que adiciona elementos de dentro de uma lista dentro de uma lista
numeros = [1, 2, 3, 4, 5]
numeros.extend([6, 7, 8, 9])
print(numeros)

print('---------------')

# (Insert) Método que adiciona um elemento na posição que desejar dentro de uma lista
vogais = ['a', 'i', 'o', 'u']
vogais.insert(1, 'e')
print(vogais)

#produtos.pop('banana') (Pop) Método que exclui o último elemento dentro de uma lista ou também remove o valor passado como parâmetro
#numeros.reverse() (Reverse) Método que reverte a ordem dos elementos dentro de uma lista
#numeros.sort (Sort) Método que ordena sequencialmente a ordem dos elementos dentro de uma lista

print('---------------')

# Lista
valores = list(range(10))
valores_maiores_que_cinco = []

for v in valores:
    if v > 5:
        valores_maiores_que_cinco.append(v)

maiores_que_cinco = [valor for valor in valores if valor > 5]

print(valores)
print(maiores_que_cinco)
print(valores_maiores_que_cinco)

lista_alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
teste = 'E'
indice = lista_alfabeto.index(teste)
print(indice)