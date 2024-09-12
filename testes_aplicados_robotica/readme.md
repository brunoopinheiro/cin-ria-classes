# Testes Aplicados à Robótica

## Ementa
- Testes para robótica `!=` robótica para testes
- Motivações, conceitos básicos, definições
- Noções básicas sobre automação de testes
    - _framework_ de testes, _setup_, _teardown_, oráculo
- Automação de testes suportada por robôs
    - vantagens, desvantagens, exemplos de aplicações
- Apresentação de exemplos de robótica apliada a testes com base na literatura e em outros exemplos desenvolvidos no CIn.

## Motivação e Conceitos Básicos
> Testar é comparar **O que o sistema é** com **o que o sistema deveria ser**.

## Teste de Software
- O que é teste de software?
- Vocabulário
- O ciclo de vida de um defeito
- Oráculo de testes
- Geração e execução de casos de teste
- Níveis de teste e Pirâmide de testes
- Testes e visibilidade interna do SUT
- Qualidade Interna vs Qualidade Externa
- Caracterização de testes (objetivos)

## Software Testing
> Software testing consists of the **dynamic** verification that a program provides **expected** behaviors on a **finite** set of test cases, suitably **selected** from the usually infinite execution domain.

_Guide to the Software Engineering Body of Knowledge (SWEBOK)_

- **Dynamic**: O software precisa estar em execução.
- **Finite**: Testar exaustivamente é impossível na maior parte dos casos. Quando não o é, é impraticável.
- **Selected**: Relacionado a identificar a melhor forma de cobrir os casos de teste.
- **Expected**: Se não é feita uma comparação, não é um teste.

## Vocabulário
- **Erro**
    - Confusão ou mal-entendido na mente do programador.
    - Erro humano que causa uma falta.
- **Falta**
    - Representação de um erro (a confusão mental - o erro - se materializa em algum lugar do código-fonte, diagrama, modelo, etc);
    - Por exemplo: um `>` foi digitado ao invés de um `<`.
    - Causa de uma falha.
- **Falha**
    - Incapacidade do software de realizar a função requisitada.
    - Manifestação da falta.
    - Terminação anormal, loop, tela azul do Windows.

_IEEE 1044-2009 - IEEE Standard Classification for Software Anomalies. 07-Jan-2010._

## O Ciclo de Vida de um Defeito
> Bug / Fault / Defect

1. Execution touched the buggy code and state got infected.
2. Infection propagated to other parts of the state.
3. Infection was observed.

O foco da atividade de teste é **encontrar defeitos**.

## Oráculo de Testes
Um mecanismo que serve para determinar se um caso de teste passou ou falhou.

### O que muda com o uso de robôs para teste?
- Quase sempre invasivo (robô + computador para verificação do comportamento observado).
- Combinado com <font color="red">visão computacional</font> pode permitir uma execução não-invasiva.
- Execução não-invasiva é desafiadora:
    - complexidade do oráculo
    - menor controle na execução (precisa verificar o estado do SUT antes de executar a próxima ação)
    - alimentação energética do SUT ("novo" problema)
