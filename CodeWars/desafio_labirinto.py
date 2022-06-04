from time import sleep
import os

PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "2"
ROBO = "4"
SAIDA = "S"

LINHA = 0
COLUNA = 1

ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

somaMatriz = lambda x, y: (x[0] + y[0], x[1] + y[1])

def read_file(nomeArquivo: str) -> list:
    """Lê um arquivo txt e transforma em matriz."""
    labirinto = []
    with open (nomeArquivo, 'r') as arquivo:
        for line in arquivo:
            temp = []
            for caracters in line:
                if caracters != '\n':
                    temp.append(caracters)
            labirinto.append(temp)
    return labirinto

def print_labirinto(labirinto: list, move: tuple):
    """Printa o labirinto na tela e coloca um ponto onde ja passou o robô."""
    os.system('cls')
    for linha in labirinto:
        for caracters in linha:
            print(caracters, end='')
        print()
    labirinto[move[LINHA]][move[COLUNA]] = "."

def posicao_robo(labirinto: list) -> tuple:
    """Encontra a posição do robô no labirinto e retorna a posição."""        
    posicao = []                   
    for linha in labirinto:         
        for caracteres in linha:    
            if caracteres == "4":   
                posicao.append(labirinto.index(linha))      
                posicao.append(linha.index(caracteres))     
    return posicao

def movimento(posicaoAtual: tuple) -> bool:
    """Logica de movimento utilizando função recursiva ao inves de pilha."""
    sleep(0.3)
    labirinto[posicaoAtual[LINHA]][posicaoAtual[COLUNA]] = "R"
    print_labirinto(labirinto, posicaoAtual)

    direcoes = [
    CIMA,
    ESQUERDA,
    DIREITA,
    BAIXO
    ]
    for direcao in direcoes:
        passo = somaMatriz(posicaoAtual, direcao)
        if passo[0] < 0 or passo[1] < 0 or passo[0] >= len(labirinto) or passo[1] >= len(labirinto[0]):
            continue
        elif labirinto[passo[0]][passo[1]] == "#":
            continue
        elif labirinto[passo[0]][passo[1]] == "." and labirinto[somaMatriz(passo, direcao)[0]][somaMatriz(passo, direcao)[1]] != " ":
            continue
        elif labirinto[passo[0]][passo[1]] == 'S' :
            posicaoAtual = passo
            labirinto[posicaoAtual[LINHA]][posicaoAtual[COLUNA]] = "R"
            print_labirinto(labirinto, posicaoAtual)
            print('Caminho percorrido com sucesso.')
            return True
        else:
            if movimento(passo):
                return True
            labirinto[posicaoAtual[LINHA]][posicaoAtual[COLUNA]] = "R"
            sleep(0.3)
            print_labirinto(labirinto, posicaoAtual)

    return False


def main():
    global atual
    global labirinto
    labirinto = read_file(r'C:\Users\silvi\Desktop\Código[s]\CodeWars\labirinto.txt')
    atual = posicao_robo(labirinto)
    movimento(atual)


if (__name__ == '__main__'):
    main()