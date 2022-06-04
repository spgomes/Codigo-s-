# Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário
# >>> {“matemática”: 81, “física”: 83, “química”: 87} 
# a saída deve ser 
# >>> {“química”: 87, “física”: 83, matemática”: 81}
#----------------------------------------------------------------------------------------------
print("\n")

notas = {
    "matemática": 81,
    "física": 83,
    "química": 87
}
print({k : v for k, v in sorted(notas.items(), key=lambda item: item[1], reverse=True)})
