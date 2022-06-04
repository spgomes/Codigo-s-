# Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
# •	A soma de A e B;
# •	A diferença quando se subtrai B de A;
# •	O produto (multiplicação) entre A e B;
# •	O quociente (parte inteira da divisão) quando se divide A por B;
# •	O resto da divisão entre A e B;
# •	O resultado de log10 de A;
# •	O resultado de A elevado a B;
#------------------------------------------------------------------------------------------------------------
print("\n")
from math import log10
a = int(input("Digite o valor para A: "))
b = int(input("Digite o valor para B: "))
print('A soma de A + B é: {:.2f}'.format(a + b))
print('A diferença quando se subtrai B de A é: {:.2f}'.format(b - a))
print('O produto entre A e B: {:.2f}'.format(a * b))
print('O quoeficiente quando se divide A por B: {}'.format(a // b))
print('O resto da divisão entre A e B: {}'.format(a % b))
print('O resultado de log10 de A: {:.2f}'.format(log10(a)))
print('O resultado de A elevado a B: {:.2f}'.format(a ** b))
