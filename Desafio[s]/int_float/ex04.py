# Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima
# o Índice de Massa Corporal (IMC) do usuário.
#-----------------------------------------------------------------------------------------------------------
print("\n")
peso = float(input('Qual o peso em kg? '))
altura = float(input('Qual sua altura em metros? '))
imc = peso / (altura ** 2)
print(f'O seu indice de massa corporal (IMC) é de {imc:.2f}')
