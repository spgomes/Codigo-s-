# Escreva um programa que leia um valor de nível sonoro do usuário em decibéis.
# Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho.
# Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o
# valor digitado está. Seu programa deve informar também quando o valor for menor que o ruído mínimo da
# tabela e maior que ruído máximo.
# Britadeira         --> 130
# Cortador de grama  --> 106
# Despertador        --> 70
# Comodo em silêncio --> 40
#---------------------------------------------------------------------------------------------------------
print('\n')

dic_ruido = {
            "Britadeira": 130,
            "Cortador de grama": 106,
            "Despertador": 70,
            "Cômodo em silêncio": 40
    }
dic_ruido2 = {k : v for k, v in sorted(dic_ruido.items(), key=lambda item: item[1])}
lista_valor_ruido = list(dic_ruido.values())
max_ruido = max(lista_valor_ruido)
min_ruido = min(lista_valor_ruido)
anterior_v = max_ruido
anterior_k = 0

valor_ruido = float(input('Digite o valor do ruido em decibéis: '))
for key, value in dic_ruido2.items():
    if valor_ruido == value:
        print(f'O ruido corresponde ao barulho da(o) {key}.')
        break
    elif valor_ruido > max_ruido:
        print(f'O ruido está maior que o valor máximo presente na tabela.')
        break
    elif valor_ruido < min_ruido:
        print(f'O ruido está menor que o valor mínimo presente na tabela.')
        break
    elif valor_ruido < value and valor_ruido > anterior_v:
        print(f'O ruido inserido enta entre {key} e {anterior_k}.')
        break
    else:
        anterior_v = value
        anterior_k = key
