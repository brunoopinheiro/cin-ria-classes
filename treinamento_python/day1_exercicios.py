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
    ...


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
    ]

    print("=== Escolha um exercício ===")

    for option in program_options:
        print(f"{option['key']}: {option['description']}")
    
    while 1 == 1:
        option = input('Digite a opção que deseja executar: ')
        try:
            option = int(option)
            cli_function = program_options[option - 1]['function']
            cli_function()
            break
        except (ValueError, IndexError):
            print("Digite uma opção válida.")



if __name__ == "__main__":
    main_cli()