import os
from functools import reduce


# Ler dados de um arquivo
def ler_dados(arquivo):
    livros = []
    with open(arquivo, 'r', encoding='utf-8') as file:
        books = file.read().split('\n')
        livros = [b.split(',') for b in books]
    return livros


# Função que cria um dicionário a partir de uma lista com os dados do livro
def livro_dict(livro):
    return {
        'titulo': livro[0],
        'autor': livro[1],
        'ano': int(livro[2]),
        'paginas': int(livro[3])
    }


# Função útil para encontrar livros com mais páginas
# do que uma quantidade mínima especificada
def filtra_num_pgs(livro, minimo):
    return True if livro['paginas'] > minimo else False


# Função útil para obter a soma de páginas dos livros
def soma_paginas(total, livro):
    return total + livro['paginas']


# Main function
def main():
    # Caminho do Arquivo
    file_path = os.path.join(os.getcwd(), 'biblioteca.txt')

    # Ler dados dos livros
    livros_bruto = ler_dados(file_path)

    # Cria uma lista de livros no formato de dicionário
    livros = list(map(livro_dict, livros_bruto))

    # Filtre livros com mais de 300 páginas
    livros_filtrados = list(filter(
        lambda liv: filtra_num_pgs(liv, 300),
        livros))
    titulos_livros_filtrados = [liv['titulo'] for liv in livros_filtrados]

    # Calcule o número total de páginas na biblioteca
    total_paginas = reduce(soma_paginas, livros, 0)

    # Use compreensão de listas
    # para obter todos os livros publicados antes de 1950
    livros_antigos = [liv['titulo'] for liv in livros if liv['ano'] < 1950]

    # Output results
    print('\n')
    print("Títulos dos livros com mais de 300 páginas:", titulos_livros_filtrados)
    print('\n')
    print("Total de páginas dos livros da biblioteca:", total_paginas)
    print('\n')
    print("Livros publicados antes de 1950:", livros_antigos)


if __name__ == "__main__":
    main()
