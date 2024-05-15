# 1) Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.
def calc_tip(bill_price: float, tip: float = 0.1) -> float:
    return bill_price * tip


# 2) Faça uma função que receba uma lista de números armazenados de forma crescente, 
# e dois valores ( limite inferior e limite superior), 
# e exiba a sublista cujos elementos são maiores ou iguais ao limite inferior e menores ou iguais ao limite superior.
# Exemplo:
# lista inicial=[12,14,15,16,18,20,24,26,28,32,34,38]
# limite inferior=13
# limite superior = 26
# lista exibida: [14,15,16,18,20,24,26]
from typing import List
def get_limits(values_list: List[int], inf_limit: int, sup_limit: int):
    sublist = []
    for n in values_list:
        if n >= inf_limit and n <= sup_limit:
            sublist.append(n)

    return sublist


# 3) Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def sum_three(a: int | float, b: int | float, c: int | float) -> float:
    return float(a + b + c)


# 4) Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def positive_or_negative(value: int | float) -> str:
    if value > 0:
        return 'P'
    else:
        return 'N'


# 5) Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. 
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. 
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
A = 'A.M.'
P = 'P.M'
def convert_hour(hour_value: int):
    if hour_value > 12:
        return [(hour_value - 12), P]
    elif hour_value == 24:
        return [0, A]
    else:
        return [hour_value, A]


def ampm_hours() -> str:
    keep_converting = True

    while keep_converting is True:
        try:
            hour = input('Digite o valor das horas: ')
            minutes = input('Digite o valor dos minutos: ')
            hour = int(hour)
            minutes = int(minutes)
            c_hour, period = convert_hour(hour)
            
            print(f'{c_hour}:{minutes} {period}')

            should_continue = input('Deseja continuar convertendo? [S/N]')
            if should_continue.upper() != 'S':
                keep_converting = False
        except ValueError:
            print('Digite um valor inteiro válido.')


# 6) Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def get_reversed(value: int) -> int:
    str_value = str(value)
    r_value = str_value[-1::-1]
    return int(r_value)


# 7) Faça um programa de implemente um jogo de Craps. 
# O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
WIN = 'Natural'
LOSE = 'Craps'
POINT = 'Ponto'
def evaluate(value: int, tries: int, first_point: int | None = None) -> str:
    if tries == 1 and value in (7, 11):
        return WIN
    
    if first_point is not None and value == first_point:
        return WIN
    
    if tries == 1 and value in (2, 3, 12):
        return LOSE
    
    if tries > 1 and value == 7:
        return LOSE

    if tries == 1:
        return POINT

    return POINT

def craps_game():
    first_point = None
    tries = 0
    finish_game = False

    while finish_game is False:
        try:
            tries += 1
            dice_value = int(input('Lance seus dados: '))
            if dice_value > 12 or dice_value < 2:
                raise ValueError

            result = evaluate(dice_value, tries=tries, first_point=first_point)
            if result in (WIN, LOSE):
                print(result)
                finish_game = True
            else:
                print(result)
                if first_point is None:
                    first_point = dice_value

        except ValueError:
            print('Não tente trapacear.')


# 8) Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. 
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. 
# Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
def adjust_values(value: int) -> int:
    if value < 1:
        return 1
    elif value > 20:
        return 20
    
    return value


def is_corner(row: int, column: int, max_column: int, max_row: int) -> bool:
    if row != 1 and row != max_row: 
        return False
    if column != 1 and column != max_column:
        return False
    if row == 1 or row == max_row:
        if column != 1 and column != max_column:
            return False
    return True


def print_rectangle(rows: int = 1, columns: int = 1):
    rows = adjust_values(rows)
    columns = adjust_values(columns)

    print(f'Construindo um retângulo de {rows} x {columns} \n')

    for row in range(1, rows + 1):
        line = ""
        for column in range (1, columns + 1):
            if is_corner(row, column, columns, rows) is True:
                line = line + '+'
            elif column == 1 or column == columns:
                line = line + '|'
            elif row == 1 or row == rows:
                line = line + '-'
            else:
                line = line + '.'
        print(line)


# 9)
# a)Faça uma função que verifique se uma lista está vazia, caso esteja, retorne True, caso contrário, retorne False.
# b)Altere a função para se a lista estiver vazia, preencha com 5 valores aleatórios de 1 a 100.
# c)Altere a função para receber uma lista e um valor, caso a lista esteja vazia, preencha com a quantidade de valores.
# d)Faça uma função que ordene uma lista de forma decrescente.
def empty_list_v1(check_list: list) -> bool:
    if len(check_list) > 0:
        return False
    return True


from random import randint
def empty_list_v2(check_list: list) -> list:
    if len(check_list) > 0:
        return check_list
    
    for i in range(5):
        check_list.append(randint(1, 100))

    return check_list


def empty_list_v3(check_list: list, elements: int) -> list:
    if len(check_list) > 0:
        return check_list
    
    for i in range(elements):
        check_list.append(randint(1, 100))

    return check_list


def sort_list(check_list: list) -> list:
    new_list = sorted(check_list, reverse=True)
    return new_list


if __name__ == "__main__":
    # Exercicio 1
    print('Exercicio 1')
    print(calc_tip(1_000))
    print('\n')

    # Exercicio 2
    print('Exercicio 2')
    lista_inicial=[12,14,15,16,18,20,24,26,28,32,34,38]
    limite_inferior=13
    limite_superior = 26
    sublist = get_limits(
        values_list=lista_inicial,
        inf_limit=limite_inferior,
        sup_limit=limite_superior
    )
    print(sublist)
    print('\n')

    # Exercicio 3
    print('Exercicio 3')
    print(sum_three(10, 5, 6.5))
    print('\n')


    # Exercicio 4
    print('Exercicio 4')
    print(positive_or_negative(0.1))
    print(positive_or_negative(-2))
    print('\n')


    # Exercicio 5
    print('Exercicio 5')
    ampm_hours()
    print('\n')


    # Exercicio 6
    print('Exercicio 6')
    print(get_reversed(217))
    print('\n')


    # Exercicio 7
    print('Exercicio 7')
    craps_game()
    print('\n')


    # Exercicio 8
    print('Exercicio 8')
    print_rectangle(10, 23)
    print('\n')


    # Exercicio 9
    print('Exercicio 9')
    print(empty_list_v1([]))
    print(empty_list_v1([1]))

    print(empty_list_v2([]))
    print(empty_list_v2([1, 2]))

    print(empty_list_v3([], 8))
    print(empty_list_v3([1, 2, 3], 8))

    input_list = [randint(1, 20) for i in range(10)]
    print(sort_list(input_list))