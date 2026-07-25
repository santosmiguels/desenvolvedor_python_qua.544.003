#Programa_01-01
import math

"""
Prog. que receba nome, peso e altura do usuário e informe na tela o seu IMC. Que é o diagnóstico com base no valor IMC.
"""
#TODO - atividade 01.

#Entrada da váriáveis

nome = ""
peso = ""
altura = ""

nome = input("Entre com o nome do usuário: ")
peso = float(input("Digite o peso do usuário: "))
altura = float(input("Entre com a altura do usuário: "))

imc = peso / altura**2

if imc < 18.5:
    print(f"O usuário {nome} tem o IMC = {imc}.")
    print("O usuário está em estado de magreza ou abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
    print(f"O usuário {nome} tem o IMC = {imc}.")
    print("O usuário está com o peso normal ou adequado.")
elif imc >= 25 and imc <= 29.9:
    print(f"O usuário {nome} tem o IMC = {imc}.")
    print("O usuário está com excesso de peso.")
elif imc >= 30 and imc <= 34.9:
    print(f"O usuário {nome} tem o IMC = {imc}.")
    print("O usuário está com obesidade grau I.")
elif imc >= 35 and imc <= 39.9:
    print(f"O usuário {nome} tem o IMC = {imc}.")
    print("O usuário está com obesidade grau II.")
else:
    print(f"O usuário {nome} tem o IMC = {imc}.")
    print("O usuário está com obesidade grau III (grave).")


