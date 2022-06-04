# Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira
# (no formato antigo) com três letras, um traço e quatro números. Exemplos: 
#     • Dada a entrada ABT-1234 o programa deveria exibir True
#     • Dada a entrada JKL9999 o programa deveria exibir False
#     • Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá
#     exibir False 
#-----------------------------------------------------------------------------------------------------------
from re import T


print("\n")

placa_modelo = False
placa = input('Digite a placa do veiculo: ').upper()
if len(placa) != 8:
    print(placa_modelo)
elif placa[0] < "A" or placa [0] > "Z":
    print(placa_modelo)
elif placa[1] < "A" or placa [1] > "Z":
    print(placa_modelo)
elif placa[2] < "A" or placa [2] > "Z":
    print(placa_modelo)
elif placa[3] != "-":
    print(placa_modelo)
elif placa[4] < "0" or placa [4] > "9":
    print(placa_modelo)
elif placa[5] < "0" or placa [5] > "9":
    print(placa_modelo)
elif placa[6] < "0" or placa [6] > "9":
    print(placa_modelo)
elif placa[7] < "0" or placa [7] > "9":
    print(placa_modelo)
else:
    placa_modelo = True
    print(placa_modelo)