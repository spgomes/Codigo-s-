# Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado.
# Exemplo:

# >>> Digite um estado: SP
# >>> O nome completo do estado é São Paulo.
#---------------------------------------------------------------------------------------------------------
print('\n')

dictEstados = dict(sp="São Paulo", mg="Minas Gerais", rj="Rio de Janeiro", ac="Acre", al="Alagoas", ap="Amapá",
am="Amazonas", ba="Bahia", ce="Ceará", es="Espirito Santo", go="Goiás", ma="Maranhão", mt="Mato Grosso",
ms="Mato Grosso do Sul", pa="Pará", pb="Paraíba", pr="Paraná", pe="Pernanbuco", pi="Piauí", rn="Rio Grande do Norte",
rs="Rio Grande do Sul", ro="Rondônia", rr="Roraima", sc="Santa Catarina", se="Sergipe", to="Tocantins", df="Distrito Federal")

estado = input('Digite a sigla do estado: ').lower()
print(f'O nome completo do estado é: {dictEstados[estado]}')