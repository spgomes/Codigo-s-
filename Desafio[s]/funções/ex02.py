# Escreva uma função que, dado três comprimentos de retas quaisquer, diga se essas três retas podem ou não formar um 
# triângulo, retornando true em caso positivo e false em caso negativo
# Dica n°1: Se algum dos comprimentos for negativo ou zero, não é possível formar um triângulo.
# Dica n°2: se qualquer um dos comprimentos for maior ou igual à soma dos outros dois, então os comprimentos não podem 
# ser usados para formar um triângulo. Caso contrário, eles podem formar um triângulo.
#--------------------------------------------------------------------------------------------------------------------
print('\n')

def validando_retas(lista: list):
    if lista[0] >= lista[1] + lista[2] or lista[1] >= lista[0] + lista[2] or lista[2] >= lista[0] + lista[1]:
        return False
    else:
        return True

lst = []
for c in range(3):
    c += 1
    retas = float(input(f'Digite o comprimento da {c}º reta: '))
    lst.append(retas)
print(validando_retas(lst))
