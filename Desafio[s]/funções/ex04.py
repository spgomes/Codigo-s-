# Embaralha palavras: Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres
# embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra
# combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa
# alta ou caixa baixa, independentemente de como foram digitados.
#-----------------------------------------------------------------------------------------------------------------
print('\n')

from random import shuffle


def embaralha_string(a: str) -> str:
    str_list = [letra.lower() for letra in a]
    shuffle(str_list)
    return "".join(str_list)



user_input = str(input('Digite a palavra que deseja embaralhar: '))
print(embaralha_string(user_input))