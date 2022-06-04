# Em uma determinada país, as tarifas de táxi consistem em uma tarifa básica de R$4,00 mais R$0,25 para cada 140 metros
# percorridos. Escreva uma função que receba a distância percorrida (em quilômetros) como único parâmetro e retorna a
# tarifa total como único resultado. Escreva um programa que demonstre o uso da sua função.
#-------------------------------------------------------------------------------------------------------------------
print('\n')

def calcula_valor(a: float) -> float:
   return 4 + distancia * 1000 / 140 * 0.25


distancia = float(input('Digite a distância percorrida em KM: '))
print(f'Para uma distancia de {distancia}, o valor total é de {calcula_valor(distancia):.2f}.')
