# Exercício Python 20: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# DICA ESTUDEM A BIBLIOTECA PYTHON RANDOM

import random

print("acerte qual é o número entre 0 e 5")
numero_usuario = int(input("insira o número:"))

numero_computador = random.randint(0, 5)

if numero_usuario == numero_computador :
    print(f"VOCÊ ACERTOU!!!😁 \n número:{numero_computador}")
else :
    print(f"você errou.😭 \n número:{numero_computador}")    