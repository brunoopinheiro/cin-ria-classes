# 1) Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início. 
# 1ª string: AABBEFAATT 2ª string: BE Resultado: BE encontrado na posição 3 de AABBEFAATT
from typing import Tuple
def find_substring(string_a: str, string_b: str) -> Tuple[bool, int]:
    if len(string_b) > len(string_a):
        return (False, -1)

    if string_b in string_a:
        return (True, string_a.find(string_b))
    
    return (False, -1)


def print_substring(string_a: str, string_b: str) -> None:
    result, index = find_substring(string_a, string_b)
    if result is True:
        print(f'Resultado: {string_b} encontrado na posicao {index} de {string_a}')
        return
    print(f'Resultado: {string_b} não encontrada em {string_a}')

def test_ex1() -> None:
    string_a = 'AABBEFAATT'
    string_b = 'BE'
    print_substring(string_a, string_b)



# 2) Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas. 
# 1ª string: AAACTBF 2ª string: CBT Resultado: CBT A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns a ambas.
def intersection_string(string_a: str, string_b: str) -> str:
    i_string = ''
    for letter in string_a:
        if letter in string_b and not letter in i_string:
            i_string = i_string + letter

    return i_string


def test_ex2() -> None:
    string_a = 'AAACTBF'
    string_b = 'CBT'
    print(intersection_string(string_a, string_b))


# 3) Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde você quer jogar e alternar entre os jogadores. 
# A cada jogada, verifique se a posição está livre. Verifique também quando um jogador venceu a partida. 
# Um jogo da velha pode ser visto como uma lista de 3 elementos, na qual cada elemento é outra lista, também com três elementos.
# jogo_da_velha = [
#     [00, 01, 02],
#     [10, 11, 12],
#     [20, 21, 22],
# ]
# Exemplo do jogo:
#  X | O |
# ---+---+---
#    | X | X
# ---+---+---
#    |   | O
# Em que cada posição pode ser vista como um número. Confira a seguir um exemplo das posições mapeadas para a mesma posição de seu teclado numérico.
#  7 | 8 | 9
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  1 | 2 | 3
from typing import Tuple
PLAYER_1 = 'X'
PLAYER_2 = 'O'
BOARD_MAP = {
    1: (2, 0),
    2: (2, 1),
    3: (2, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (0, 0),
    8: (0, 1),
    9: (0, 2),
}
WINNING_COMBINATIONS = [
    [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)], # diagonals
    [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], # columns
    [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)] # rows
]
SAMPLE_BOARD = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
]


def printboard(print_board: list = SAMPLE_BOARD) -> None:
    print(' {} | {} | {} '.format(*print_board[0]))
    print('---+---+---')
    print(' {} | {} | {} '.format(*print_board[1]))
    print('---+---+---')
    print(' {} | {} | {} '.format(*print_board[2]))


def get_play(board, player_mark) -> Tuple[bool, list]:
    new_board = board
    try:
        play = int(input('Digite a coordenada da sua jogada: '))
        i, j = BOARD_MAP[play]
        if board[i][j] != " ":
            raise AssertionError

        new_board[i][j] = player_mark
        return (True, new_board, (i, j))
    except (ValueError, AssertionError):
        print('Jogada inválida')
        return (False, board, (-1, -1))


def assert_endgame(movesp1, movesp2, count) -> Tuple[bool, None | int]:
    if count == 10:
        return (True, None)
    p1_moveset = set(movesp1)
    p2_moveset = set(movesp2)

    for win_c in WINNING_COMBINATIONS:
        set_win_c = set(win_c)
        if set_win_c.issubset(p1_moveset):
            return (True, 1)
        if set_win_c.issubset(p2_moveset):
            return (True, 2)

    return (False, None)


def hash_game() -> None:
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

    movesp1 = []
    movesp2 = []
    stop = False
    count = 1
    print('Jogo da Velha!')
    print('As coordenadas de jogo são:')
    printboard()
    while stop is False:
        print('=========')
        print(f'Rodada {count}\n')
        printboard(board)
        stop, winner = assert_endgame(
            movesp1=movesp1,
            movesp2=movesp2,
            count=count,
            )
        
        if stop is False:
            player = 2 if count % 2 == 0 else 1
            print(f'Sua vez, Jogador {player}')
            valid, board, move = get_play(
                board,
                PLAYER_2 if count % 2 == 0 else PLAYER_1,
                )
            if valid:
                count += 1
                if player == 1:
                    movesp1.append(move)
                if player == 2:
                    movesp2.append(move)

        if stop is True:
            if winner is None:
                print('Deu velha! Tentem novamente!')
            else:
                print(f'Parabéns, Jogador {winner}. Você venceu!')


def test_ex3():
    hash_game()


# 4) Escreva uma função que receba a base e a altura de um triângulo e retorne sua área.
def calc_tri_area(base, height) -> float:
       return (base * height)/2


# 5) Defina uma função recursiva que calcule o maior divisor comum (M.D.C.) entre dois números a e b, em que a > b
def recursive_gcd(a: int, b:int, i:int | None = None) -> int:
    if i is not None and i == 0:
        return -1
    if a % b == 0:
        return b
    elif i is not None:
        if a % i == 0 and b % i == 0:
            return i
        return recursive_gcd(a, b, i = i - 1)
    else:
        return recursive_gcd(a, b, i = b - 1)


# 6) Usando a função mdc definida no exercício anterior, defina uma função para calcular o menor múltiplo comum (M.M.C.) entre dois números. mmc(a, b) = |a × b| / mdc(a, b) 
# Em que |a × b| pode ser escrito em Python como: abs(a * b).
def lcm(a: int, b: int) -> int:
    return abs(a * b) / recursive_gcd(a, b)


# 7) Reescreva a função para cálculo da sequência de Fibonacci da lista anterior, sem utilizar recursão.
def fibonacci_v2(n: int) -> list:
    fibo_list = []
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            fibo_list.append(1)
        else:
            next_number = fibo_list[-2] + fibo_list[-1]
            fibo_list.append(next_number)

    return fibo_list


# 8) Escreva um programa Python que itere os inteiros de 1 a 50. Para múltiplos de três imprima "Fizz" em vez do número e para múltiplos de cinco imprima "Buzz". Para números múltiplos de três e cinco, imprima "FizzBuzz".
# Saída de amostra:
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz
def fizzbuzz(n: int = 50) -> None:
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# 9) Escreva um programa Python para exibir o signo do Zodíaco Chinês para o ano em que você nasceu.
# Ordem dos signos:
# 0 - Dragão
# 1 - Cobra
# 2 - Cavalo
# 3 - Ovelha
# 4 - Macaco
# 5 - Galo
# 6 - Cachorro
# 7 - Porco
# 8 - Rato
# 9 - Boi
# 10 - Tigre
# 11 - Lebre
def chinese_sign(birth_year: int) -> str:
    ref_years = {
        0: 'Macaco',
        1: 'Galo',
        2: 'Cachorro',
        3: 'Porco',
        4: 'Rato',
        5: 'Boi',
        6: 'Tigre',
        7: 'Lebre',
        8: 'Dragão',
        9: 'Cobra',
        10: 'Cavalo',
        11: 'Ovelha',
    }
    year_key = birth_year % 12
    return ref_years[year_key]


if __name__ == "__main__":
    # # Ex1
    # print('Exercício 1 - Substring')
    # test_ex1()


    # # Ex2
    # print('Exercício 2 - Caracteres Comuns')
    # test_ex2()


    # # Ex3
    # print('Exercício 3 - Jogo da Velha #')
    # test_ex3()


    # # Ex4
    # print('Exercício 4 - Área do Triângulo')
    # print(calc_tri_area(5, 4))


    # # Ex5
    # print('Exercício 5 - MDC Recursivo')
    # print(recursive_gcd(50, 30))


    # # Ex6
    # print('Exercício 6 - MMC')
    # print(lcm(20, 9))


    # # Ex7
    # print('Exercício 7 - Fibonacci não recursivo')
    # print(fibonacci_v2(1))
    # print(fibonacci_v2(2))
    # print(fibonacci_v2(5))
    # print(fibonacci_v2(10))


    # # Ex8
    # print('Exercício 8 - FizzBuzz')
    # fizzbuzz()


    # Ex9
    print('Exercício 9 - Signo Horoscopo Chinês')
    for i in range(1984, 2045):
        print(i, chinese_sign(i))