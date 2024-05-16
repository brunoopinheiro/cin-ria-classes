# 1) Escreva um programa que recebe 3 notas de prova e calcula:
# - A média delas
# - A média ponderada delas, considerando pesos 2, 2 e 3
# - A média ponderada delas, considerando pesos 1, 2 e 2
from typing import List
def media(notas: List[int | float], pesos: List[int | float] | None = None) -> float:
    """
    Args:
        notas (List[int  |  float]): A list of scores
        pesos (List[int  |  float] | None, optional): A list of weights. Defaults to None.

    Returns:
        _type_: the weighted average of the given lists
    """    
    if pesos is None:
        pesos = [1 for i in range(len(notas))]

    # tratar caso de tamanhos de lista diferentes

    soma = 0
    soma_pesos = 0
    for nota, peso in zip(notas, pesos):
        soma += nota * peso
        soma_pesos += peso

    return float(soma/soma_pesos)

def cli_media():
    print('1) Escreva um programa que recebe 3 notas de prova e calcula a média')
    
    input_scores = []
    get_scores = True
    while len(input_scores) < 3:
        i_score = input('Digite uma nota ou -1 para sair: ')
        try:
            i_score = float(i_score)
            if i_score == -1:
                get_scores = False
                return
            input_scores.append(i_score)
        except ValueError:
            pass

        if type(i_score) not in (int, float) or i_score < 0:
            print('Digite uma nota válida.')

    with_weights = input('Deseja adicionar pesos à nota? [S/N] ')
    if with_weights == 'S' or with_weights == 's':
        weights = []
        while len(weights) < len(input_scores):
            i_weight = input(f'Digite um peso para a nota {len(weights) + 1}: ')
            try:
                i_weight = float(i_weight)
                weights.append(i_weight)
            except ValueError:
                print('Digite um peso válido.')
        
        result = media(notas=input_scores, pesos=weights)
        print(f"Notas: {input_scores}")
        print(f"Pesos: {weights}")
        print(f"A média foi: {result:.2f}")

    else:
        result = media(notas=input_scores)
        print(f"Notas: {input_scores}")
        print(f"A média foi: {result:.2f}")
    



# 2) Faça programa que recebe um tempo dado em segundos e calcula quantos dias, horas, minutos e segundos ele representa.
def factor_time(time: int) -> dict:
    """
    Args:
        time (int): time in seconds

    Returns:
        dict: {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds,
        }
    """
    MIN = 60
    HOUR = 60
    DAY = 24

    minutes = time // MIN
    seconds = time % MIN

    hours = minutes // HOUR
    minutes = minutes % HOUR

    days = hours // DAY
    hours = hours % DAY

    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
    }


def cli_factortime():
    print('2) Faça programa que recebe um tempo dado em segundos e calcula quantos dias, horas, minutos e segundos ele representa.')

    i_seconds = input('Digite o tempo em segundos: ')
    try:
        i_seconds = int(i_seconds)
        result = factor_time(i_seconds)
        print(f"""
        Dias: {result['days']}
        Horas: {result['hours']}
        Minutos: {result['minutes']}
        Segundos: {result['seconds']}
        """)
    except ValueError:
        print("Digite um tempo válido em segundos.")


# 3) Faça um programa que leia um valor de mercadorias que um turista está trazendo de volta e calcula quanto ele terá que pagar de imposto na alfândega.
# A regra de imposto é:
# Até 500 de valor: sem imposto
# Acima de 500: 50% sobre o excedente
def calc_tax(valor_merc: float) -> float:
    LIMIT = 500
    tax = 0
    if valor_merc > LIMIT:
        excedente = valor_merc - LIMIT
        tax = excedente * 0.5

    return tax


def cli_calctax():
    print('3) Faça um programa que leia um valor de mercadorias que um turista está trazendo de volta e calcula quanto ele terá que pagar de imposto na alfândega.')

    valor_merc = input('Digite o valor das mercadorias: ')
    try:
        valor_merc = float(valor_merc)
        result = calc_tax(valor_merc)
        print(f"Valor a pagar: {result}")
    except ValueError:
        print("Digite um preço válido.")

# 4) A Locadora de Veículos Eudora lançou uma grande promoção esse mês: pagando apenas R$ 90 por diária, o cliente pode alugar um carro de passeio. 
# Para cada diária, o cliente recebe uma cota de quilometragem de 100 Km. Cada quilômetro a mais custará uma taxa extra de R$ 12.
# Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada por um cliente dessa locadora e exiba o valor total a ser pago com duas casas decimais.
def calc_carprice(days: int, total_km: int) -> float:
    PRICE_DAY = 90
    PRICE_EXKM = 12
    KM_DAY = 100

    quota_km = days * KM_DAY
    extra_km = total_km - quota_km

    base_price = days * PRICE_DAY
    extra_fee = extra_km * PRICE_EXKM

    return round((base_price + extra_fee), 2)


def cli_carprice():
    print('4) A Locadora de Veículos Eudora lançou uma grande promoção esse mês: pagando apenas R$ 90 por diária, o cliente pode alugar um carro de passeio.')

    days = input('Por quantos dias o carro ficou alugado? ')
    total_km = input('Qual a kilometragem rodada? ')

    try:
        days = int(days)
        total_km = int(total_km)
        result = calc_carprice(days=days, total_km=total_km)
        print(f'Valor a pagar: R${result:.2f}')
    except ValueError:
        print('Digite um valor numérico inteiro.')


# 5) Escreva um programa que exiba na saída padrão os 100 primeiros números naturais (inteiros positivos incluindo o zero).
def naturals_range(n_range: int = 100) -> None:
    naturals = [i for i in range(n_range)]
    return naturals


def cli_natrange():
    print('5) Escreva um programa que exiba na saída padrão os 100 primeiros números naturais (inteiros positivos incluindo o zero).')

    result = naturals_range()
    print(result)


# 6) Escreva um programa que exiba na saída padrão os 100 primeiros números primos.
def is_prime(i: int) -> bool:
    if i < 2:
        return False
    if i == 2:
        return True
    if (i % 2) == 0:
        return False
    for j in range(3, i, 2):
        if (i % j) == 0:
            return False
    return True


from typing import List
def n_primes(n: int = 100) -> List[int]:
    if n < 2:
        return []
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i) is True:
            primes.append(i)
        i += 1

    return primes


def cli_primes():
    print('6) Escreva um programa que exiba na saída padrão os 100 primeiros números primos.')

    result = n_primes()
    print(result)


# 7) Impares - Quadrados Consecutivos
from typing import Tuple
def get_consecutivesquares(odd_number: int) -> Tuple[int, int]:
    if odd_number % 2 == 0:
        return (0, 0)

    minor_half = odd_number // 2
    greater_half = minor_half + 1

    return (minor_half ** 2, greater_half ** 2)


def cli_consecutivesquares():
    print('7) Impares - Quadrados Consecutivos')

    get_input = True
    while get_input is True:
        try:
            odd_number = input('Digite um número impar: ')
            odd_number = int(odd_number)
            if odd_number % 2 == 0:
                raise ValueError

            minor_sqr, grt_sqr = get_consecutivesquares(odd_number)
            print(f'{grt_sqr} - {minor_sqr} = {odd_number}')
            get_input = False
        except ValueError:
            print('Digite um número válido.')


# 8) Printa consecutivamente 1 - 40
def print_consecutive(n) -> bool:
    if n < 1 or n > 40:
        return False

    numbers = []
    for i in range(1, n + 1):
        numbers.append(str(i))
        print(' '.join(numbers))
    
    return True


def cli_consecutiveprint():
    print('8) Printa consecutivamente 1 - 40')

    result = False
    while result is False:
        try:
            i_n = input('Digite um n entre 1 e 40: ')
            i_n = int(i_n)
            result = print_consecutive(i_n)
        except ValueError:
            print('Digite um número válido.')


# 9) Na física, um problema clássico de cinemática é encontrar a posição de um corpo ao longo do processo de queda acelerada por meio da gravidade.
# Faça um programa que calcula a altura H que um corpo cai sob ação da gravidade (g=9.8m/s^2) durante 7.5 segundos,
# sabendo que ele tem uma velocidade inicial v0 = 0.75m/s^2, vertical para baixo.
def calc_height(
    t: float,
    v0: float = 0.75, #m/s^2
    ) -> float:
    GRAVITY = 9.8 #m/s^2
    # h = v0 x t + 0.5 x g x t²
    height = (v0 * t) + 0.5 * GRAVITY * (t ** 2)
    return height


def cli_calheight():
    print('9) Na física, um problema clássico de cinemática é encontrar a posição de um corpo ao longo do processo de queda acelerada por meio da gravidade.')

    result = calc_height(t = 7.5)
    print(f'H: {result}')


# 10) Joãozinho investiu R$1000,00 na sua conta do Banco Iradoso por um ano.
# Sabendo que seu investimento rende 0.02% por dia útil, qual o montante que Joãozinho terá após 7 semanas de investimento?
def calc_rend(
    investimento: float,
    semanas: int,
    rend: float = 0.0002,
    ) -> float:
    DIAS_SEMANA = 5
    dias_totais = DIAS_SEMANA * semanas
    
    montante = investimento
    for i in range(1, dias_totais + 1):
        montante += montante * rend
        # print(f'Dia {i + 1}: {montante}')

    return montante


def cli_calcrend():
    print('10) Joãozinho investiu R$1000,00 na sua conta do Banco Iradoso por um ano.')


    investimento = 1_000
    semanas = 7
    rend = 0.0002
    result = calc_rend(
        investimento=investimento,
        semanas=semanas,
        rend=rend,
    )

    print(f'''
    Investimento Inicial: R$ {investimento:.2f},
    Semanas de Investimento: {semanas},
    Rendimento base: {rend * 100} %
    Montante Final: R$ {result:.2f}
    ''')


# 11) Indique como verdadeiro ou falso:
# Duas variáveis definidas como “teste” e “Teste” são consideradas como idênticas.
def compare_names(str_a: str, str_b: str) -> bool:
    if str_a == str_b:
        return True
    return False


def cli_compare():
    str_a = input('Declare a primeira variável: ')
    str_b = input('Declare a segunda variável: ')

    result = compare_names(str_a, str_b)
    if result is True:
        print('Essas variáveis são consideradas idênticas.')
    else:
        print('Essas variáveis não são consideradas idênticas.')


# 12) Classifique o itens abaixo como nome de variável válido ou inválido.
# teclado_lidinho
# Germa66
# 1º_lugar
# PlayerID
# class
# Exiba "valido" ou "invalido no terminal"
from keyword import iskeyword
from re import match
import builtins
def check_variables(var_name: str) -> bool:
    reg = r'^(?!.*[A-Z].*[a-z])(?!.*[a-z].*[A-Z])[a-zA-Z_][a-zA-Z0-9_]*$'
    built_in_types = dir(builtins)
    try:
        if iskeyword(var_name) or var_name.isidentifier() is not True:
            return False
        if match(reg, var_name) is None:
            return False
        if var_name in built_in_types:
            return False
        return True
    except SyntaxError:
        return False


def cli_checkvarname():
    var_name = input('Declare sua variável: ')
    is_valid = check_variables(var_name)
    if is_valid is True:
        print('Válido')
    else:
        print('Inválido')


# 13) Suponha que você está mexendo com um banco de dados de números inteiros. 
# Você decide salvar cada valor numa variável e percebe que, em algum momento do código, você precisa trocar os valores de duas variáveis ( e ) entre si. 
# Ou seja, fazer com que  receba o valor de  e que  receba o valor de . 
# Faça um programa que realize essa troca de valores entre duas variáveis.
def swap_values(a, b) -> tuple:
    a, b = b, a
    return (a, b)


def cli_swapvalues():
    var_a = input('Digite o valor da primeira variável: ')
    var_b = input('Digite o valor da segunda variável: ')
    
    print(f'''
    === Valores Originais ===
    A: {var_a}
    B: {var_b}
    ''')

    print('--- Invertendo as coisas... ---')
    var_a, var_b = swap_values(var_a, var_b)

    print(f'''
    === Valores Invertidos ===
    A: {var_a}
    B: {var_b}
    ''')


# 14) Complete a tabela a seguir, respondendo True ou False. Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5.
def logic_check(var_a, var_b, operator) -> bool:
    return eval(f'{var_a} {operator} {var_b}')


def cli_logic():
    a = 4
    b = 10
    c = 5.0
    d = 1
    f = 5

    input_list = [
        [a, '==', c],
        [b, '>', a],
        [a, '<', b],
        [c, '>=', f],
        [d, '>', b],
        [f, '>=', c],
        [c, '!=', f],
        [c, '<=', c],
        [a, '==', b],
        [c, '<=', f],
        [c, '<', d],
    ]

    for check in input_list:
        print(check)
        var_a, operator, var_b = check
        print(logic_check(var_a, var_b, operator))


# 15) Escreva um programa que converta uma temperatura digitada em °C em °F. 
# A fórmula para essa conversão é: F = ((9 * C) / 5) + 32
def celcius_to_f(temperature: float) -> float:
    return float(((9 * temperature) / 5) + 32)


def cli_ctof():
    try:
        temperature = float(input('Temperatura em °C: '))
        temp_f = celcius_to_f(temperature)
        print(f'Temperatura em °F: {temp_f}')
    except ValueError:
        print('Digite uma temperatura válida')


# 16) Escreva um programa que leia três números e que imprima o maior e o menor.
from typing import List, Tuple
def min_and_max(numbers_list: List[int]) -> Tuple[int]:
    min_n = min(numbers_list)
    max_n = max(numbers_list)
    return (min_n, max_n)


def cli_minmax():
    numbers_list = []

    stop = False

    print("""
        Digite os números para serem avaliados.
        Para parar, digite 'stop'
    """)
    while stop is False:
        try:
            new_number = input('>> ')
            if new_number == 'stop':
                stop = True
            else:
                new_number = float(new_number)
                numbers_list.append(new_number)
        except ValueError:
            print('Digite um valor numérico válido.')

    if len(numbers_list) > 0:
        min_n, max_n = min_and_max(numbers_list)
        print(f"""
        MIN: {min_n}
        MAX: {max_n}
        """)


# 17) Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve
# perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação
# mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a
# comprar dividido pelo número de meses a pagar.
def bank_loan(house_value: float, salary: float, years: int) -> bool:
    MONTHS = 12
    THRESHOLD = 0.3
    monthly_pay = house_value / (years * MONTHS)
    if monthly_pay > salary * THRESHOLD:
        return False
    return True


def cli_bankloan():
    try:
        print('== Banco Iradoso - Simulação de Empréstimo ===')
        print('Valor do imóvel.')
        house_value = float(input('>> '))
        print('Salário do contratante.')
        salary = float(input('>> '))
        print('Tempo de financiamento (em anos).')
        years = int(input('>> '))
        print('Calculando...')
        result = bank_loan(house_value, salary, years)

        print(f'''
        --- Relatório da Simulação:
        Valor do Imóvel: R$ {house_value:.2f}
        Salário: R$ {salary:.2f}
        Tempo Financiamento: {years} anos

        Resultado: {'Aprovado!' if result is True else 'Não Aprovado.'}
        ''')
    except ValueError:
        print('Valores inválidos.')


# 18) Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa
# verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o
# número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1
# não são primos e que 2 é o único número primo que é par
def cli_isprime():
    try:
        i_number = int(input('Digite um número primo: '))
        # Usa a função is_prime definida para resolução da questão 6
        result = is_prime(i_number)
        if result is True:
            print('Número primo.')
        else:
            print('Não é um número primo.')
    except ValueError:
        print('Valor inválido. Digite um número inteiro.')


# Main Running Function
def main_cli():
    program_options = [
        {
            'key': 1,
            'description': 'Calcula Médias',
            'function': cli_media,
        },
        {
            'key': 2,
            'description': 'Converte Segundos em Dias, Horas, Minutos e Segundos',
            'function': cli_factortime,
        },
        {
            'key': 3,
            'description': 'Calcula imposto sobre valor da mercadoria',
            'function': cli_calctax,
        },
        {
            'key': 4,
            'description': 'Calcula preço de aluguel de carro',
            'function': cli_carprice,
        },
        {
            'key': 5,
            'description': 'Exibe 100 primeiros números naturais',
            'function': cli_natrange,
        },
        {
            'key': 6,
            'description': 'Exibe 100 primeiros números primos',
            'function': cli_primes,
        },
        {
            'key': 7,
            'description': 'Imprime diferença de dois quadrados',
            'function': cli_consecutivesquares,
        },
        {
            'key': 8,
            'description': 'Imprime lista de numeros',
            'function': cli_consecutiveprint,
        },
        {
            'key': 9,
            'description': 'Calcula H de queda livre',
            'function': cli_calheight,
        },
        {
            'key': 10,
            'description': 'Calcula Investimento',
            'function': cli_calcrend,
        },
        {
            'key': 11,
            'description': 'Compara Variáveis',
            'function': cli_compare,
        },
        {
            'key': 12,
            'description': 'Classifica Variáveis',
            'function': cli_checkvarname,
        },
        {
            'key': 13,
            'description': 'Inverte valores de variáveis',
            'function': cli_swapvalues,
        },
        {
            'key': 14,
            'description': 'Compara valores da lista',
            'function': cli_logic,
        },
        {
            'key': 15,
            'description': 'Converte °C para °F',
            'function': cli_ctof,
        },
        {
            'key': 16,
            'description': 'Encontra Minimo e Máximo',
            'function': cli_minmax,
        },
        {
            'key': 17,
            'description': 'Simulação de Empréstimo',
            'function': cli_bankloan,
        },
        {
            'key': 18,
            'description': 'Verifica Números Primos',
            'function': cli_isprime,
        },
    ]

    print("=== Escolha um exercício ===")

    for option in program_options:
        print(f"{option['key']}: {option['description']}")
    
    while 1 == 1:
        option = input('Digite a opção que deseja executar: ')
        try:
            option = int(option)
            cli_function = program_options[option - 1]['function']
            print('-------')
            cli_function()
            return
        except (ValueError, IndexError):
            print("Digite uma opção válida.")



if __name__ == "__main__":
    main_cli()