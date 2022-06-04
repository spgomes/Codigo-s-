# Escreva um programa que calcule o número pi com 15 aproximações. 
# A primeira aproximação deve considerar apenas o primeiro termo da série, ou seja 3. 
# A segunda aproximação deve considerar a soma até o segundo termo, e assim por diante!
#--------------------------------------------------------------------------------------------
print('\n')

pi = 0

for aprox in range(15):
    if aprox == 0:
        pi += 3
        continue

    dobro_aprox = aprox * 2
    denominador = dobro_aprox * (dobro_aprox + 1) * (dobro_aprox + 2)

    if aprox % 2 != 0:
        pi += 4 / denominador
    else:
        pi -= 4 / denominador

print(f"O número pi com 15 aproximações é {pi}")
