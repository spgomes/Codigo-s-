#Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
#-------------------------------------------------------------------------------------------------------------------
print('\n')

def reverso(num):
    reversed(num)
    return ''.join(reversed(num))


n1 = str(input('Digite o valor que queira inverter: '))
print(reverso(n1))