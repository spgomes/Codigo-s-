# Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário.
# Exemplo: dado o dicionário:
# >>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
# A saída deverá ser
# >>> {1: 8, 2: 4, 3: 6}
#-------------------------------------------------------------------------------------------------------
print("\n")

cores = {1:"vermelho", 2: "azul", 3:"marrom"}
comp:0
for key, value in cores.items():
    comp = len(value)
    cores[key] = comp
print(cores)