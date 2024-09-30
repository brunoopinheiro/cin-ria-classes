# Interpretabilidade de Modelos
## Por que?
- Questões de regulação para tomada de decisão que afetam humanos
- Modelos complexos podem ser auditados
- Aumentar a confiança no uso dos modelos de AM

> **Book** _Interpretable Machine Learning: A Guide for Making Black Box Models Explainable_, Christoph Molnar

## Abordagens Gerais
1. Métodos intrínsecos: interpretabillidade alcançada restringindo a complexidade dos modelos
    - Exemplos: regras, modelos lineares, árvores de decisão
    - Possivelmente com uma perda na qualidade pelo fato de priorizar métodos simples
2. Métodos post hoc: aplicar métodos que analisam um modelo complexo após seu treinamento
    - Treinar um modelo de alta qualidade e extrair explicações a posteriori
    - Diferentes estratégias

## Métodos Agnósticos ou Não-Agnósticos
1. Agnósticos: métodos que podem ser utilizados para qualquer modelo de aprendizagem
    - Modelo de AM é visto como uma caixa preta
2. Não-agnóstico: métodos específicos para modelos
    - Métodos caixa branca como aqueles que tentam gerar explicações a partir dos pesas das redes neurais

## Feature Importance
- Método para **explicações** baseados em medir a importância das variáveis para as prediçõesdo modelo a ser explicado.
- ...

### FI Global Gnóstico (para Random Forest)
- Métodos Gnósticos
    - Baseados na redução do critério de impureza
        - Considerar todas as árvores que usam o atributo e medir a redução média de impureza causada pelo atributo.
    - Baseado no número de vezes em que o atributo é selecionado entre todas as árvores de decisão.
### FI Global Agnóstico - Permutation Feature Importance
1. Estimar o erro do modelo original para cada instância
2. Para cada feature:
3. ...
