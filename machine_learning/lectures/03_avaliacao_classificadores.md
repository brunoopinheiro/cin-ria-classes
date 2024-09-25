# Avaliação de Classificadores
## Métricas
- Existem muitas métricas usadas para diferentes propósitos, como:
    - Avaliar a qualidade de classificações (e.g., acurácia)
    - Avaliar a qualidade das probabilidades estimadas pelos models (e.g. Brier score ou MSE)
    - Avaliar a qualidade dos scores dos modelos quando usados para rankear exemplos (e.g. AUC)

### Métricas de Classificação
Baseadas comumente na matriz de confusão:

- Classe Positiva =
    - VP: Verdadeiros Positivos + FN: Falsos Negativos

- Classe Negativa =
    - VN: Verdadeiros Negativos + FP: Falsos Positivos

| | | Predito | |
|:--:|:--:|:--:|:--:|
| | | **Classe A** | **Classe B** |
| Verdadeiro | **Classe A** | VP | FN |
| .. | **Classe B** | FP | VN |

- Acurácia = (VP + VN) / (VP + VN + FP + FN)
    - Ou seja, (VP + VN) divididos por N, onde N é o número total de exemplos.

- Precisão para classe positiva = VP / (VP + FP)
    - Ou seja, quanto eu acerto quando dou uma resposta positiva

- Precisão para classe negativa = VN / (VN + FN)
    - Ou seja, quanto eu acerto quando dou uma resposta negativa.

- True Positive Rate (Recall, Sensibilidade) = VP / (VP + FN)
    - Ou seja, quanto eu consigo identificar a classe positiva.

- True Negative Rate (Especificidade) = VN / (VN + FP)
    - Ou seja, quanto eu consigo identificar a classe negativa
    - F-Measure (média harmônica de precision e recall) = $2 * \left(\frac{\text{Precision} * \text{Recall}}{\text{Precision} + \text{Recall}}\right)$
- Obs: Média harmônica é penalidade quando apenas uma das métricas tem valor alto.

### Suporte e Confiança para Regras
- No contexto de aprendizagem de regras se usa comumente o suporte e a confiança para avaliação.
    - Suporte = Cobertura da regra
    - Confiança = Precisão de regra
- Exemplo para regra:
    - Se (A ^ B) Então Classe = (Sim 711, Não 94)
    - Suporte = (717 + 94)/997, onde 997 é o número total de exemplos cobertos
    - Confiança = 717/(717 + 94), i.e., precisão da regra para os exemplos cobertos por ela.
- Para seleção das regras mais relevantes, se escolhe um suporte e confiança mínimos.

- Suporte ({X, Y}) = Exemplos que contém X e Y / Total de Exemplos

Base de Dados:
| | Sol | Vento | Resultados |
|:---: | :---: | :---: | :---: |
| 1 | Sim | Sim | Não vou à praia |
| 2 | Sim | Não | Vou à praia |
| 3 | Não | Não | Não vou à praia |
| 4 | Não | Sim | Não vou à praia |

...

## Métricas Para Avaliação de Rankings
- Curva Receiver-Operator Curve (ROC)
    - Taxa de FP versus taxa de TP para diferentes limiares de decisão
- Sensibilidade vs Especificidade
    - Muitas vezes conflitantes, em especial quando se usa funções de score para ordenar exemplos mais críticos.
        - Porque o colesterol LDL deve ser menor que 130? Por que não 120?

### Curva ROC
- TPR vs FPR considerando diferentes limiares de decisão
    - **Area Under the ROC Curve (AUC)** indica qualidade média do modelo considerando diferentes limiares de decisão.
- AUC é igual a 1 para um modelo perfeito
- AUC é igual 0.5 para um modelo aleatório
- AUC = probabilidade de um exemplo positivo escolhido aleatoriamente ter score maior que exemplo negativo escolhido aleatoriamente.

## Métricas de Avaliação de Probabilidades
- Avalia a qualidade das probabilidades estimadas pelo modelo
    - Obs.: um modelo pode ser um bom rankeador mas as probabilidades podem ser ruins (e.g, Naive Bayes, comumente)
- Exemplos de métricas, assumindo que y = 1 indica classe positiva, y = 0 indica classe negativa e p = prob. estimada para classe positiva;

> MSE (y, p) = (y - p) ^2 (ou Brier Score)

> MAE (y, p) = |y - p|

> LogLoss(y, p) = {
    - ln (p), se y = 1
    - ln (1-p), se y = 0
}

## Validação
- Existem diferentes tipos de validação, as mais comuns são:
    - Holdout
    - Cross Validation

- Holdout se refere ao particionamento do conjunto de dados entre treino e teste
    - É comum adotar a estratégia de particionar o conjunto entre 80% para treino e 20% para teste, por exemplo

- Já a validação cruzada é um método estatístico de avaliar a capacidade de geração dos modelos.

![Cross Validation](https://www.sharpsightlabs.com/wp-content/uploads/2024/02/cross-validation-explained_FEATURED-IMAGE.png)

## Lista de Exercícios
1. Crie uma árvore de decisão para o conjunto de dados Statlog Heart Dataset, com profundidade máxima igual a 2. Calcule a precisão e cobertura dos nós terminais da árvore. (Não precisa de split treino/teste)
2. Crie uma árvore de decisão para um conjunto de dados do seu interesse. Separe o conjunto de treinamento e teste. Treine a árvore com o conjunto de treinamento, gere a matriz de confusão para o conjunto de teste. Calcule a acurácia e teste diferentes valores para a profundidade da árvore.
3. Construa e avalie um modelo usando curva ROC. Qual o limiar de decisão necessário para se obter uma taxa de verdadeiros positivos maior que 0.9?
4. Compare os modelos de Regressão Logistica, AD, RF, SVM, Naive Bayes, e kNN, usando a métrica AUC ou outras métricas de interesse. Monte uma tabela com os resultados.
5. Para um determinado conjunto de dados, aplicar um modelo e plotar as curvas de Precision e Recall, bem como a curva ROC. Teste diferentes parâmetros para o modelo e plote a curva ROC para os diferentes parâmetros. Teste também diferentes limiares de decisão de classificação e analise como esses diferentes limiares afetam as métricas de classificação.
6. Utilize a validação cruzada para avaliar um conjunto de modelos utilizando diferentes métricas. Por fim, monte uma tabela com os resultados.