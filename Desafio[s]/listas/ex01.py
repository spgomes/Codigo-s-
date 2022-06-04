# Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão).
# Imprima na tela o elemento e sua respectiva posição na lista. Exemplo: para a lista [1, 3, 6, “H”, [7,7,7]] 
# a saída deve ser:
# >>> Elemento 1 na posição 0
# >>> Elemento 3 na posição 1
# >>> Elemento 6 na posição 2
# >>> Elemento “H” na posição 3
#------------------------------------------------------------------------------------------------------------
print("\n")
lista = []
for c in range(5):
    a = input(f'Digite o {c + 1}° valor da sua lista: ')
    lista.append(a)
print(f'O elemente que esta na posição 0 é o: {lista[0]}')
print(f'O elemente que esta na posição 1 é o: {lista[1]}')
print(f'O elemente que esta na posição 2 é o: {lista[2]}')
print(f'O elemente que esta na posição 3 é o: {lista[3]}')
