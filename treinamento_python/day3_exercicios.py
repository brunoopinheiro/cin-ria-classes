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
    # cli_multitable()


    # Exercício 6
    result = fibonacci(10)
    print(result)