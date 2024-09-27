# Análise e Limpeza de Dados
## Introdução
- A eficiência de uma solução depende em muitos cases do tamanho do problema.
- Dimensão de um problema de aprendizado
    - Número de atributos
    - Número de exemplos de treinamento
- A dimensão de um problema de aprendizado interfere em muitos casos na:
    - Qualidade das respostas (precisão) dos algoritmos
    - e no custo do aprendizado

## Redução de Atributos
- Em geral, espera-se que todos os atributos sejam relevantes, porém nem sempre é possível garantir isso.
- Além disso, alguns atributos são redundantes e assim poderiam ser eliminados.
- Objetivo: reduzir o número de atributos sem perda de informação.
- Abordagens: Seleção X Extração de Atributos

## Extração de Atributos
- Criação de atributos relevantes através da combinação dos atributos originais
- Muito usado para análise exploratória

### PCA - Principal Component Analysis
- Cada nova dimensão é uma _combinação linear_ das variáveis originais dos dados.
- Cada nova dimensão é chamda de _componente principal_.
