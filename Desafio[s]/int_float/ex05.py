# Escreva um programa que leia do usuário um número de 4 digitos e imprima a soma destes digitos.
# Exemplo se o usuário digitar 3141 seu programa deverá imprimir na rela 3 + 1 + 4 + 1 = 9
#-----------------------------------------------------------------------------------------------------------
print("\n")
# Primeira forma de resolver
n = input('Digite um número inteiro de 4 dígitos: ')
n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])
n4 = int(n[3])

print(f'{n1} + {n2} + {n3} + {n4} = {n1 + n2 + n3 + n4}')

# Sugunda fomar de resolver usando for
print("\n")
soma = 0
n = input('Digite um número inteiro de 4 dígitos: ')
for c in range(len(n)):
    soma += int(n[c])
print (f'{n[0]} + {n[1]} + {n[2]} + {n[3]} = {soma}')
