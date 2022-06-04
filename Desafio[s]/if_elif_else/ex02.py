# Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.
#---------------------------------------------------------------------------------------------------------
print("\n")

num_1 = float(input('Digite o primeiro número: '))
num_2 = float(input('Digite o segundo número: '))
if num_1 % num_2 == 0:
    print('O primeiro é divisível pelo segundo.')
else:
    print('O primeiro não é divisível pelo segundo.')