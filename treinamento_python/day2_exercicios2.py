# 1) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
from getpass import getpass

def login():
    retry = True
    while retry is True:
        print('--- Cadastro de Novo Usuário ---')
        username = input('Digite seu usuário: ')
        password = getpass('Digite sua senha: ')

        if password != username:
            retry = False
            print('Usuário cadastrado com sucesso!')
        else:
            print('Usuário e senha não podem ser iguais. Tente novamente.')

# 2) Supondo que a população de um país A seja da ordem de 80_000 habitantes 
# com uma taxa anual de crescimento de 3% 
# e que a população de B seja 200_000 habitantes 
# com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
def growth_rate(
    pop_a: int,
    rate_a: float,
    pop_b: int,
    rate_b: float
    ) -> int:
    years = 0
    print(f'''
        Populações Iniciais
        A: {pop_a}
        B: {pop_b}
    ''')
    while pop_a < pop_b:
        years += 1
        # truncando, já que não existe meia pessoa
        pop_a += int(pop_a * rate_a)
        pop_b += int(pop_b * rate_b)
        print(f'População A: {pop_a}')
        print(f'População B: {pop_b}')
        print('\n')
    return years


# 3) Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
def cli_growthvalues():
    getting_inputs = True
    while getting_inputs is True:
        try:
            pop_a = int(input('População A: '))
            rate_a = float(input('Taxa de Crescimento (A): '))
            pop_b = int(input('População B: '))
            rate_b = float(input('Taxa de Crescimento (B): '))

            result = growth_rate(
                pop_a=pop_a,
                rate_a=rate_a,
                pop_b=pop_b,
                rate_b=rate_b,
            )

            print(f'Anos necessários: {result}')

            new_calc = input('Deseja executar novamente? [S/N]')
            if new_calc.upper() != 'S':
                getting_inputs = False
        except ValueError:
            print('Valores inválidos, tente novamente.')


# 4) Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.
from typing import Tuple
def even_and_odds(integer_list: list) -> Tuple[int, int]:
    evens = 0
    odds = 0
    for i in integer_list:
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1

    return (evens, odds)


def cli_evenodds():
    input_list = []
    while len(input_list) < 10:
        try:
            new_number = int(input('Digite um número: '))
            input_list.append(new_number)

        except ValueError:
            print('Por favor, digite valores válidos.')

    evens, odds = even_and_odds(input_list)
    print(f'''
    Pares: {evens}
    Impares: {odds}
    ''')


# 5) Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
def is_prime(i: int) -> bool:
    for j in range(2, i):
        if (i % j) == 0:
            return False
    return True


# 6) Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
def average(numbers_list: list) -> float:
    return sum(numbers_list) / len(numbers_list)


def average_students():
    try:
        classes = int(input('Nº de Turmas: '))

        students_list = []
        for i in range(classes):
            n_students = int(input(f'Nº de estudantes da turma {i + 1}: '))
            students_list.append(n_students)

        print(f'Média de alunos por turma é de {average(students_list)}')
    except ValueError:
        print('Utilize apenas valores inteiros.')


# 7) Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#     1- Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#     2- Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#     3- A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
def get_salary(
    initial_payment: float = 1_000.0,
    initial_year: int = 1995,
    final_year: int = 2024,
    initial_rate: float =  0.015,
    growth_rate: int = 2,
) -> float:
    salary = initial_payment
    current_year = initial_year + 1
    raise_amount = initial_rate

    while current_year < final_year:
        salary += salary * raise_amount
        raise_amount = raise_amount * growth_rate
        current_year += 1
        print(f'Salário R$ {salary:.2f}')

    return salary





# 8) Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deverá terminar quando for lido um número negativo.
def count_pools():
    pools = {
        'a': {
            'max': 25,
            'count': 0,
        },
        'b': {
            'max': 50,
            'count': 0,
        },
        'c': {
            'max': 75,
            'count': 0,
        },
        'd': {
            'max': 100,
            'count': 0,
        },
    }

    keep_inputing = True
    print('Digite números entre 1 e 100.')
    print('Digite um número negativo para sair.')
    while keep_inputing is True:
        try:
            new_number = float(input('Digite um número: '))
            if new_number < 0:
                keep_inputing = False
            elif new_number <= pools['a']['max']:
                pools['a']['count'] += 1
            elif new_number < pools['b']['max']:
                pools['b']['count'] += 1
            elif new_number < pools['c']['max']:
                pools['c']['count'] += 1
            elif new_number < pools['d']['max']:
                pools['d']['count'] += 1
            else:
                keep_inputing = False
        except ValueError:
            print('Digite apenas números.')

    print(f'''
    Numbers Pool:
    A: {pools['a']['count']}
    B: {pools['b']['count']}
    C: {pools['c']['count']}
    D: {pools['d']['count']}
    ''')
    return pools



if __name__ == "__main__":
    print('Resolução dos Exercícios - Condicional')


    # # Exercicio 1
    # login()


    # # Exercicio 2
    # years = growth_rate(
    #     pop_a=80_000,
    #     rate_a=0.03,
    #     pop_b=200_000,
    #     rate_b=0.015
    # )
    # print(f'Anos necessários: {years}')


    # # Exercício 3
    # cli_growthvalues()


    # # Exercicio 4
    # cli_evenodds()


    # # Exercicio 5
    # print(is_prime(1))
    # print(is_prime(2))
    # print(is_prime(3))
    # print(is_prime(4))
    # print(is_prime(7))
    # print(is_prime(8))


    # # Exercicio 6
    # average_students()


    # # Exercício 7
    # get_salary()


    # # Exercício 8
    # count_pools()