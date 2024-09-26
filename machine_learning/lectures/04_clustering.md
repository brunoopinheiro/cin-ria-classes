# Clustering (Agrupamento)
- Particionar objetos em _clusters_ de forma que:
    - Objetos dentro de um cluster são similares
    - Objetos de clusters diferentes são diferentes
- Descobrir novas categorias de objetos de uma menira _não-supervisionada_
    - Rótulos de classe não são fornecidos à priori

## Tipos de Clustering
- Algoritmos Flat (ou Particional)
    - Geram partição "plana", i.e. não existe relação hierárquica entre clusters
- Algoritmos Hierárquicos
    - Geram uma hierarquia de clusters, i.e. cada cluster é associado a um cluster-pai mais genérico
        - Vantagem: diferentes visões dos dados
- **Hard**
    - Cada objeto pertence exclusivamente a um único grupo na partição
- **Fuzzy**
    - Cada objeto está associado a um cluster com um certo grau de pertinência.
        - Partição Fuzzy pode ser convertida facilmente para uma partição Hard
- **Deterministico**
    - Mesmo conjunto de dados e parâmetros de entrada resultam no mesmo agrupamento
- **Estocástico**
    - Mesmo conjunto de dados e parâmetros de entrada podem resultar em diferentes agrupamentos

## Algoritmo k-Means
- **Objetivo**: Encontra de forma interativa os _centróides_ dos clusters.
- **Passos**:
    1. Inicialização: Selecionar k objetos aleatórios como centróides iniciais
    2. Atribuição: Atribuir cada objeto ao centróide mais próximo
    3. Atualização: Recalcular os centróides
    4. Repetir passos 2 e 3 até atingir um critério de parada:
        - e.g., até um número máximo de iterações ou;
        - até não ocorrer alterações nos centróides (i.e., convergencia para um mínimo local da função de erro quadrado)

