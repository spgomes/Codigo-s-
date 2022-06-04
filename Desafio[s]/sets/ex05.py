# Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas
# respectivas chaves.
# Exemplo: dado o dicionário
# >>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80}
# A saída deve ser
# >>> Nota máxima -> Júnior : 80
# >>> Nota mínima -> Theodoro : 20
#--------------------------------------------------------------------------------------------------------
from multiprocessing.sharedctypes import Value


print("\n")

notas = {"Theodoro": 20, "Márcia": 50, "Júnior": 80}

valores = list(notas.values())
max = max(valores)
min = min(valores)
for key, value in notas.items():
    if value == min:
        print(f'Nota mínima: {key} : {value}')
    elif value == max:
        print(f'Nota máxima: {key} : {value}')
