# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as
# temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso:
# Exemplo de saída:
# >>> Meses com temperatura acima da média anual de 35,5°:
# >>> 1 – janeiro
# >>> 3 – março
# >>> 6 – junho
#-----------------------------------------------------------------------------------------------------------
print("\n")

lista = []
listaMes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
somaTemperatura = 0
mediaTemperatura = 0
for c in listaMes:
    temp = float(input(f'Digite a temperatura media do mês {c}: '))
    lista.append(temp)
somaTemperatura = sum(lista)
mediaTemperatura = somaTemperatura / len(lista)
print(f'A media de temperatura do ano foi de: {mediaTemperatura:.2f}°C')
print('Os meses com temperatura maior que a média foram:')
for c in lista:
    if c > mediaTemperatura:
        print(f'{c}°C - {listaMes[lista.index(c)]}')
