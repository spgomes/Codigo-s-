# Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições.
# Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser:
# >>> O maior elemento é 8 e está na posição 3
# >>> O menor elemento é 3 e está na posição 4
#Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.
#-----------------------------------------------------------------------------------------------------------

print("\n")

lista = []
for c in range(6):
    a = int(input(f'Digite o {c + 1}° valor inteiro da sua lista: '))
    lista.append(a)
max = max(lista)
min = min(lista)
print(f'O maior elemento está na posição {lista.index(max)}.')
print(f'O menor elemento está na posição {lista.index(min)}.')
