# Faça um programa que remova strings vazias de uma lista de strings. 
# Exemplo: dada a lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] a saída deve ser
#>>> [“Olá”, “meu”, “nome”, “é”, “facilitador”]
#--------------------------------------------------------------------------------------------------------
print("\n")

lista = ["Olá", "", "meu", "nome", "", "é", "Silvio", ""]
lista = list(filter(("").__ne__, lista))
print(lista)