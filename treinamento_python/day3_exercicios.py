# 1) Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o
# valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total
# de juros pago.
def debt_payment(
    initial_debt: float,
    monthly_rate: float,
    monthly_payment: float,
):
    paid_amount = 0
    paid_fees = 0
    actual_debt = initial_debt
    months = 0

    while actual_debt > 0:
        months += 1
        if monthly_payment < actual_debt:
            actual_debt -= monthly_payment
            paid_amount += monthly_payment
            month_increase = actual_debt * monthly_rate
            actual_debt += month_increase
            paid_fees += month_increase
        else:
            paid_amount += actual_debt
            actual_debt = 0

    return {
        'months': months,
        'paid_total': paid_amount,
        'fees': paid_fees,
    }


def cli_debtpayment():
    try:
        print('=== Banco Iradoso - Planejamento de Pagamento ===')
        print('Valor Inicial da Dívida: ')
        initial_debt = float(input('>> '))
        print('Taxa de Juros Mensal: ')
        monthly_rate = float(input('>> '))
        print('Pagamento Mensal: ')
        monthly_payment = float(input('>> '))

        result = debt_payment(
            initial_debt=initial_debt,
            monthly_rate=monthly_rate,
            monthly_payment=monthly_payment,
        )

        print(f'''
        --- Relatório de Simulação ---
        > Valor Inicial da Dívida: R$ {initial_debt:.2f}
        > Taxa de Juros Mensal: R$ {monthly_rate:.2f}
        > Parcela: R$ {monthly_payment:.2f}

        Meses: {result['months']}
        Total Pago: R$ {result['paid_total']:.2f}
        Total em Juros: R$ {result['fees']:.2f}
        ''')
    except ValueError:
        print('Defina apenas valores numéricos.')


# 2) Escreva um programa que verifique se uma string é palíndromo. Uma string é palíndromo se continua o
# mesmo caso seus dígitos sejam invertidos. Exemplos: merecerem, saas
def check_palindrome(word: str) -> bool:
    return True if word == word[-1::-1] else False


def cli_palindrome():
    stop = False
    print('Verifica se uma palavra é um palíndromo.')
    print('Digite 0 para sair.')
    while stop is False:
        word = input('>> ')
        if word == '0':
            stop = True
        else:
            is_palindrome = check_palindrome(word)
            if is_palindrome is True:
                print('Palíndromo')
            else:
                print('Não é Palíndromo')


# 3) Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
def get_unique(list_a: list, list_b: list) -> list:
    uniques_list = []
    for ele_a, ele_b in zip(list_a, list_b):
        if ele_a not in uniques_list:
            uniques_list.append(ele_a)
        if ele_b not in uniques_list:
            uniques_list.append(ele_b)

    return uniques_list


# 4) Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
# >> Repetido


# 5) Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
def multiplication_table(number: int) -> None:
    print(f'Tabuada de {number}:')
    for i in range(10):
        print(f'{number} X {i + 1} = {number * (i + 1)}')


def cli_multitable():
    try:
        i_number = int(input('Número: '))
        multiplication_table(i_number)
    except ValueError:
        print('Não é um número válido.')


# 6) A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 

def fibonacci(n_term: int, sequence: list = []) -> str:
    if len(sequence) == n_term:
        return sequence
    if len(sequence) <= 1:
        sequence.append(1)
        return fibonacci(n_term, sequence)
    if len(sequence) <= n_term:
        last = sequence[-1]
        sec_last = sequence[-2]
        sequence.append((last + sec_last))
        return fibonacci(n_term, sequence)


# 7) Faça um programa que peça para n pessoas a sua idade, 
# ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
def calc_mean_age():
    stop = False

    students_list = []
    print("Informe as idades para análise. Digite 'stop' para parar.")
    while stop is False:
        try:
            input_value = input('>> ')
            if input_value.upper() == 'STOP':
                stop = True
            else:
                input_value = int(input_value)
                students_list.append(input_value)
        except ValueError:
            print('Informe uma idade positiva.')

    if len(students_list) > 2:
        mean_age = sum(students_list) / len(students_list)
        if mean_age >= 0 and mean_age < 26:
            print(f'Turma Jovem. Média: {mean_age:.2f}')
        elif mean_age < 60:
            print(f'Turma Adulta. Média: {mean_age:.2f}')
        else:
            print(f'Turma Idosa. Média: {mean_age:.2f}')
    else:
        print('Insira ao menos 2 alunos para análise.')


# 8) Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro,
# para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
def get_clients_list():
    client_codes = []
    clients_list = []
    stop = False
    while stop is False:
        try:
            print('Informe o código do cliente.')
            cod = int(input('>> '))
            if cod == 0:
                stop = True
            elif cod in client_codes:
                print('Código de cliente já cadastrado.')
            else:
                print('Informe a altura.')
                height = float(input('>> '))
                print('Informe o peso.')
                weight = float(input('>> '))

                new_client = {
                    'cod': cod,
                    'height': height,
                    'weight': weight,
                }
                clients_list.append(new_client)
                client_codes.append(cod)
                print('Cliente Cadastrado com sucesso.')
        except ValueError:
            print('Digitação Incorreta, corrija sua entrada.')

    return clients_list


# Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro,
# além da média das alturas e dos pesos dos clientes
from typing import Hashable
def mean_dictkey(list_dict: list, key: Hashable) -> float:
    values = [v[key] for v in list_dict]
    return sum(values)/len(values)


def gym_report(clients_list: list) -> str:
    if len(clients_list) == 0:
        print('Não há clientes cadastrados.')
        return {}
        
    report = {
        'height': {
            'max': max(clients_list, key=lambda x: x['height'])['cod'],
            'min': min(clients_list, key=lambda x: x['height'])['cod'],
            'mean': mean_dictkey(clients_list, 'height'),
        },
        'weight': {
            'max': max(clients_list, key=lambda x: x['weight'])['cod'],
            'min': min(clients_list, key=lambda x: x['weight'])['cod'],
            'mean': mean_dictkey(clients_list, 'weight'),
        },
    }

    print(f'''
    === Report ===
    Mais Alto: {report['height']['max']}
    Mais Baixo: {report['height']['min']}
    Média de Altura {report['height']['mean']:.2f}
    ---
    Mais Gordo: {report['weight']['max']}
    Mais Magro: {report['weight']['min']}
    Média de Peso: {report['weight']['mean']:.2f}
    ''')
    return report


def cli_gymreport():
    print('=== Iradoso GYM ===')
    print('--- Cadastro de Clientes ---')
    clients_list = get_clients_list()
    print('Montando Relatório...')
    gym_report(clients_list)


# 9) Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
def revert_upper(word: str) -> str:
    return word[-1::-1].upper()


def clirevertupper():
    print('Digite uma palavra para ser invertida.')
    word = input('>> ')
    print(revert_upper(word))


# 10) Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
def vertical_print():
    print('Digite uma palavra para ser impressa na vertical.')
    word = input('>> ')
    for letter in word.upper():
        print(letter)


# 11) Modifique o programa anterior de forma a mostrar o nome em formato de escada.
def ladder_print():
    print('Digite uma palavra para ser impressa em formato escada.')
    word = input('>> ')
    ladder = ''
    for letter in word.upper():
        ladder += letter
        print(ladder)


# 12) Altere o programa anterior de modo que a escada seja invertida.
def inverted_ladder_print():
    print('Digite uma palavra para ser impressa em formato escada invertida.')
    word = input('>> ')
    word = word.upper()
    for _ in range(len(word)):
        print(word)
        word = word[:-1]


# 13) Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
# O programa deverá então exibir o valor a ser pago na tela. 
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. 
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
def valor_pagamento(valor: float, atraso: int) -> float:
    if atraso == 0:
        return valor
    
    MULTA = 0.03
    JUROS_ATRASO = 0.001
    valor += valor * MULTA
    for _ in range(atraso):
        valor += valor * JUROS_ATRASO
    return valor

def cli_valorpagamento():
    print('=== Assistente de Pagamentos ===')

    count = 0
    total_pagamentos = 0
    stop = False
    while stop is False:
        try:
            print('Valor da Prestação: ')
            valor = float(input('>> '))
            if valor == 0:
                stop = True
            else:
                print('Dias em Atraso: ')
                atraso = int(input('>> '))
                valor_pgt = valor_pagamento(valor, atraso)
                count += 1
                total_pagamentos += valor_pgt
                print(f'Valor a pagar: R$ {valor_pgt:.2f}')
        except ValueError:
            print('Verifique a digitação.')

    print(f'''
    --- Relatório ---
    Pagamentos Efetuados: {count}
    Total pago: R$ {total_pagamentos:.2f}
    ''')


if __name__ == "__main__":
    print('Resolução - Exercícios Lista 4')

    # # Exercício 1
    # print('Exercicio 1')
    # cli_debtpayment()


    # # Exercício 2
    # print('Exercício 2')
    # cli_palindrome()


    # # Exercício 3
    # print('Exercício 3')
    # lista_a = ['Luffy', 'Zoro', 'Nami', 'Usopp', 'Sanji', 'Chopper', 'Robin']
    # print(f'Lista A: {lista_a}')
    # lista_b = ['Zoro', 'Jinbe', 'Sanji', 'Franky', 'Brook', 'Robin', 'Luffy']
    # print(f'Lista B: {lista_b}')
    # lista_unica = get_unique(lista_a, lista_b)
    # print(f'Elementos Únicos: {lista_unica}')


    # # Exercício 5
    # print('Exercício 5 - Tabuada')
    # cli_multitable()


    # # Exercício 6
    # print('Exercício 6 - Fibonacci')
    # result = fibonacci(10)
    # print(result)


    # # Exercício 7
    # print('Exercício 7 - Média das Idades')
    # calc_mean_age()


    # Exercício 8
    # print('Exercício 8 - Cadastro de Clientes de Academia')
    # cli_gymreport()


    # # Exercício 9
    # print('Exercício 9 - Invertendo Palavra Maiúsculo')
    # clirevertupper()


    # # Exercício 10
    # print('Exercício 10 - Print Vertical')
    # vertical_print()


    # # Exercício 11
    # print('Exercício 11 - Print Escada')
    # ladder_print()


    # # Exercício 12
    # print('Exercício 12 - Print Escada')
    # inverted_ladder_print()


    # Exercício 13
    print('Exercício 13 - Valor Pagamento')
    cli_valorpagamento()