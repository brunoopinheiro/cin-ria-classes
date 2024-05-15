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
    while get_scores:
        i_score = input('Digite uma nota ou -1 para sair: ')
        try:
            i_score = float(i_score)
            if i_score == -1:
                get_scores = False
                break
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
    for j in range(2, i):
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
    rend: float = 0.02,
    ) -> float:
    DIAS_SEMANA = 7
    dias_totais = DIAS_SEMANA * semanas
    
    montante = investimento
    for i in range(1, dias_totais + 1):
        montante += montante * rend

    return montante


def cli_calcrend():
    print('10) Joãozinho investiu R$1000,00 na sua conta do Banco Iradoso por um ano.')


    investimento = 1_000
    semanas = 7
    rend = 0.02
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
            break
        except (ValueError, IndexError):
            print("Digite uma opção válida.")



if __name__ == "__main__":
    main_cli()