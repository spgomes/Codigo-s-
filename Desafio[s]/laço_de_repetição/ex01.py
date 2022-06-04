# Neste exercício, você criará um programa que calcula a média de uma coleção de valores inseridos pelo usuário
# e imprime-a na tela. O usuário digitará 0 como um valor para indicar que nenhum outro valor será fornecido.
# Seu programa deve exibir uma mensagem de erro se o primeiro valor inserido pelo usuário for 0.
#------------------------------------------------------------------------------------------------------------
print('\n')

lst = []
num_user = 0
c = 0

while True:
    c += 1
    num_user = float(input(f'Digite o {c}º número ou 0 para finalizar: '))
    lst.append(num_user)
    if num_user == 0:
        break
media = sum(lst) / (len(lst) - 1)

print(f'A média dos valores inseridos é {media}.')
