import os
from datetime import date

os.system('cls')

class Cachorro:
    def __init__(self, nome, idade, peso, raca, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.raca = raca
        self.genero = genero

cachorro = Cachorro('Kira', 1, 37, 'Malamute do Alasca', 'Fêmea')
cachorro2 = Cachorro('Lola', 14, 17, 'SRD', 'Fêmea')

print(f'Nome: {cachorro.nome} | Idade: {cachorro.idade} ano(s) | Peso: {cachorro.peso}kg | Raça: {cachorro.raca} | Gênero: {cachorro.genero}')
print(f'Nome: {cachorro2.nome} | Idade: {cachorro2.idade} ano(s) | Peso: {cachorro2.peso}kg | Raça: {cachorro2.raca} | Gênero: {cachorro2.genero}')