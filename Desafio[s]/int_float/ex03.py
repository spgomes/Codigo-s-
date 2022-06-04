# No exercício acima você calculou a área de um triângulo a partir da sua base e altura.
# Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área.
# Compare a resposta com o exercício acima, dada das mesmas entradas. Os resultados devem ser idênticos.
#-----------------------------------------------------------------------------------------------------------
print("\n")
from math import sqrt
lado1 = float(input('Insira o lado 1 do triângulo: '))
lado2 = float(input('Insira o lado 2 do triângulo: '))
lado3 = float(input('Insira o lado 3 do triângulo: '))
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    s = (lado1 + lado2 + lado3) / 2
    area = sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
    print(f'A área do triângulo é: {area:.2f}')
else:
    print('Essas retas não podem formar um triângulo.')
