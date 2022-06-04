# Implemente um jogo em que o usuário tenha que adivinhar um número sorteado pelo computador.

#     1. O jogo deve sortear um número entre 1 e 100.
#     2. O usuário deve informar um número. O número informado pelo usuário deve ser validado: não pode ser
# inferior a 1 ou superior a 100. Enquanto o usuário informar um número inválido, o jogo deve solicitar a
# entrada de um novo número.
#     3. O número do usuário deve ser analisado:
#         a. Caso o usuário informe um número inferior ao número sorteado, o jogo deve apresentar a mensagem
# “O número sorteado é maior.”.
#         b. Caso o usuário informe um número superior ao número sorteado, o jogo deve apresentar a mensagem
# “O número sorteado é menor.”.
#         c. Caso o usuário informe um número igual ao número sorteado, o jogo deve apresentar a mensagem
# “Parabéns! Você acertou o número sorteado” e o jogo deve ser finalizado, sendo apresentado ao usuário a
# quantidade de tentativas efetuadas até este momento.
#     4. Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. Caso afirmativo, todo
# o processo deve ser repetido. Caso contrário, o jogo deve ser encerrado.
#----------------------------------------------------------------------------------------------------------
print("\n")

import random

numero_sort = int(random.randrange(1,101))
numero_user = 0
cont_tentativas = 0
jogar_novamente = 0

while True:
    numero_user = int(input('Digite um número inteiro entre 1 e 100: '))
    if numero_user < 1:
        continue
    if numero_user > 100:
        continue
    if numero_user < numero_sort:
        print('O número sorteado é maior.')
        cont_tentativas += 1
        continue
    if numero_user > numero_sort:
        print('O número sorteado é menor.')
        cont_tentativas += 1
        continue
    if numero_user == numero_sort:
         cont_tentativas +=1
         print(f'Parabéns! Você acertou o número sorteado!\n Você tentou um número de {cont_tentativas} vezes até acertar.')
         jogar_novamente = input('Digite Y se deseja jogar de novo: ').upper()
         if jogar_novamente == "Y":
             cont_tentativas = 0
             numero_sort = int(random.randrange(1,100))
             continue
         else:
            break
