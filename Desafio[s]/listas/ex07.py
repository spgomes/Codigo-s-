# Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta 
# lista para inteiro. Faça também o inverso, dada a mesma lista só que agora de elementos inteiros,
# converta todos os elementos para int.
#-----------------------------------------------------------------------------------------------------------
listaStr = ['1', '7', '99', '15']

listaInt = list(map(int, listaStr))
print(listaInt)

listaStr = list(map(str, listaInt))
print(listaStr)