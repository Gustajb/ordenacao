"""
Dada uma lista de palavras, escreva um programa 
que receba uma lista de frutas e mostre:
- a lista original
- a lista ordenada
- a lista na ordem inversa

Caso o usuário digite sair, pare de solicitar dados.

REFATORANDO CÓDIGO
Crie uma função para:
    - Ordenação
    - Ordenação na ordem inversa

"""

import os
os.system("cls || clear")

lista_frutas = ["banana", "laranja", "uva", "abacaxi", "maçã"]

print("\nLista original")
print(lista_frutas)

lista_ordenada = sorted(lista_frutas)
print("\nLista organizada")
print(lista_ordenada)

lista_inversa = sorted(lista_frutas,reverse = True)
print("\nLista inversa")
print(lista_inversa)