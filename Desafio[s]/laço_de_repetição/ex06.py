# Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.
#------------------------------------------------------------------------------------------------------------
print('\n')

N = int(input("Digite o valor de N: "))

H = 0

for c in range(1, N + 1):
    H += 1 / c

print(H)