from random import randint


def soma_digitos(s):
    """Assuma que s é uma string,
    o valor de retorno da função
    é a soma de dígitos decimais
    dentro de s.
    Por exemplo: 'ab2c3de' -> 5
    Use try/except na implementação"""
    soma = 0
    for char in s:
        try:
            soma += int(char)
        except (TypeError, ValueError):
            soma += 0
    return soma


def encontre_um_numero_par(L: list[int]):
    """Assuma que L é uma lista de inteiros.
    Retorno o primeiro número par da lista L.
    Se não houver nenhum número par,
    lance um erro do tipo ValueError"""
    for n in L:
        if n % 2 == 0:
            return n
    raise ValueError('Nenhum num. par encontrado.')


def main():
    print('Soma Dígitos')
    print(soma_digitos('ab2c3de'))
    print(soma_digitos('12345'))
    print(soma_digitos('abcde'))
    print()
    print('Encontre Um Número Par')
    for _ in range(10):
        try:
            rng_nums = [randint(1, 99) for _ in range(6)]
            print('INPUT: ', rng_nums)
            print(encontre_um_numero_par(rng_nums))
        except ValueError as err:
            print("Erro: ", err)
        finally:
            print()


if __name__ == '__main__':
    main()
