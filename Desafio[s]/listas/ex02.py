# Crie uma lista com 10 elementos (você escolhe quais serão) e imprima a lista na ordem inversa.
# Exemplo: para a lista [1, 3, 6, “H”, [7,7,7] a saída deve ser
# >>> [[7,7,7], “H”, 6, 3, 1]
#-----------------------------------------------------------------------------------------------------------
print("\n")
lista = []
for c in range(10):
    a = input(f'Digite o {c + 1}° valor da sua lista: ')
    lista.append(a)
lista.reverse()
print(f'A lista inversa é {lista}.')