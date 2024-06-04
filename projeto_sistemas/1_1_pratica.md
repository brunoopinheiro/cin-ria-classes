# Projeto de Sistemas – Prática 1

> Responda as questões abaixo considerando a descrição do sistema SisLivros, vista inicialmente na disciplina de Arquitetura de Sistemas. Os diagramas devem ser criados no Visual Paradigm. Esta atividade é em grupo (3 pessoas) e não vale nota.

## Especifique o CDU: manter o carrinho de compras.
**Pré Condições**: O usuário está logado.

**Fluxo Principal**:
1. Na tela de livro, o usuário seleciona a versão física do livro. `A1` `A2`
2. Na tela de livro, o usuário inclui uma cópia do livro no carrinho de compras.
3. O sistema atualiza as reservas de livros físicos no estoque. `E1`
4. O sistema salva o carrinho de compras atualizado.
5. O sistema exibe uma mensagem de que o carrinho foi atualizado.
6. Encerra o caso de uso.

**Fluxos Alternativos**:
- `A1`: O usuário seleciona a versão digital do livro.
    1. Na tela de produto, o usuário inclui o produto no carrinho de compras.
    2. Volta para o passo 4 do fluxo principal.
- `A2`: O usuário seleciona a opção de visualizar o carrinho de compras.
    1. O sistema abre uma nova tela e exibe os itens no carrinho. `A3` `A4` `A5` `E2`
    2. Encerra o caso de uso.
- `A3`: O usuário altera a quantidade de cópias de algum livro físico.
    1. O sistema atualiza as reservas de livros físicos no estoque. `E1`
    2. O sistema salva o carrinho de compras atualizado.
    3. O sistema exibe uma mensagem de que o carrinho foi atualizado.
    4. Volta para o passo `A2.1` do fluxo alternativo.
- `A4`: O usuário exclui algum livro físico do carrinho de compras.
    1. O sistema atualiza as reservas de livros físicos no estoque.
    2. O sistema salva o carrinho de compras atualizado.
    3. O sistema exibe uma mensagem de que o carrinho foi atualizado.
    4. Volta para o passo `A2.1` do fluxo alternativo.
- `A5`: O usuário exclui algum livro digital do carrinho de compras.
    1. O sistema salva o carrinho de compras atualizado.
    2. O sistema exibe uma mensagem de que o carrinho foi atualizado.
    3. Volta para o passo `A2.1` do fluxo alternativo.

## Analise o CDU: manter o carrinho de compras.

| **Classe** | **Atributos** | **Métodos** |
|:----------:|:-------------:|:-----------:|
| **Mensagem** |  | <ul><li>+Mensagem(pedido: Pedido): Mensagem</li><li>+Mensagem(livro: Livro): Mensagem</li><li>+Mensagem(carrinho: Carrinho): Mensagem</li></ul> |
| **TelaLivro** | -login: String<br>-livro: Livro | <ul><li>+selecionarLivroFisico()</li><li>+selecionarLivroDigital()</li><li>+incluirLivroCarrinho()</li></ul> |
| **TelaCarrinho** | -login: String<br>-carrinho: Carrinho | <ul><li>+TelaCarrinho(login: String): TelaCarrinho</li><li>+comprar()</li><li>+exibirCarrinho()</li><li>+alterarQuantidade(livro: Livro, quantidade: int)</li><li>+removerLivro(livro: Livro)</li></ul> |
| **ControladorCarrinho** |  | <ul><li>+selecionarLivroFisico(livro: Livro): LivroFisico</li><li>+selecionarLivroDigital(livro: Livro): LivroDigital</li><li>+incluirLivroCarrinho(login: String, livro: Livro): bool</li><li>+recuperarCarrinho(login: String): Carrinho</li><li>+atualizarCarrinho(login: String, carrinho: Carrinho): bool</li></ul> |
| _<\<Entity Collection>>_<br>**CadastroConta** |  | <ul><li>+buscarEndereco(login: String): Endereco</li><li>+salvarPedido(pedido: Pedido)</li><li>+recuperarCarrinho(login: String): Carrinho</li></ul> |
| _<\<Entity Collection>>_<br>**CadastroCarrinho** |  | <ul><li>+atualizarCarrinho(login: String, carrinho: Carrinho): void</li><li>+atualizarCarrinho(login: String, carrinho: Carrinho): void</li></ul> |
| _<\<Entity Collection>>_<br>**CadastroLivro** |  | <ul><li>+atualizarEstoqueFisico(carrinho: Carrinho): void</li><li>+reservarEstoqueFisico(livro: LivroFisico): bool</li><li>+reservarEstoqueFisico(carrinho: Carrinho): bool</li></ul> |
| **Livro** | -titulo: String<br>-autores: List<String><br>-paginas: int<br>-preco: double |  |
| **LivroFisico** | -ISBN-10: String<br>-quantidade: int |  |
| **LivroDigital** | -SIN: String |  |
| **ItemFilosoficoCarrinho** | -quantidade: int |  |
| **ItemDigitalCarrinho** |  |  |
| **ItemCarrinho** |  |  |
| **Carrinho** | -frete: double |  |

## Projete a arquitetura a partir dos CDUs: manter o carrinho de compras e comprar livros.
