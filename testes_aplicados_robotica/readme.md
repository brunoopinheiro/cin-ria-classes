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

## Geração de Casos de Teste
- Manual
    - O testador escreve um teste (passo a passo da execução) que pode ser:
        - em linguagem natural (e.g., inglês, português); ou
        - um software testador
- Automática
    - Uma ferramenta cria testes (passo a passo da execução) automaticamente:
        - em linguagem natural (e.g., inglês, português); ou
        - um software testador

## Execução de casos de teste
- Manual
    - O testador executa o teste manualmente lendo o passo a passo do caso de teste em linguagem natural (e.g., inglês, português)
- Automática
    - Um computador (ou um robô) executa o teste automaticamente.

| Tipo de Teste | Manual | Automático |
|---------------|--------|------------|
| Gerado Manualmente | Testador escreve manuamente e executa manualmente | Testador escreve manualmente e executa automaticamente |
| Gerado Automaticamente | Testador executa manualmente | Testador executa automaticamente |

### O que muda com o uso de robôs?
- Testes podem ser gerados manualmente ou automaticamente.
- Não faz sentido falar em execução manual.
- Conhecimento em LPs e desenvolvimento de software praticamente obrigatórios.
    - uma alternativa é o uso de CNLs, block-based languages ou o uso de ferramentas "_record & replay_".
- Conhecimento em robótica ajuda, mas não é essencial (principalmente se um bom framework de testes estiver disponível).

# Why Automating Testing?
1. **Efficiency:** Automated tests (usually) execute much faster than manual tests, enabling quicker feedback on code changes and speeding up the testing process.
2. **Repeatability:** Automated tests can be run consistently (most of the time), ensuring that the same tests are executed under the same conditions each time, reducing the risk of human errors.
3. **Accuracy:** Automation eliminates human errors and ensures consistent test execution, leading to more reliable and accurate results. 
4. **Cost Savings:** While there's an initial investment in setting up automation, it saves costs in the long run by reducing the need for extensive manual testing.
5. Parallel Testing: Automation enables simultaneous testing across various configurations, devices, or plataforms, enhancing testing efficiency.
6. **Increased Test Coverage:** Automated testing enables broader test coverage by executing a large number of test cases acress various scenarios, which is often impractical with manual testing due to time constraints.
7. **Complex Scenarios:** Automated tests are useful for testing complex scenarios that involve multiple user interactions, data combinations, or system configurations.
8. **Resource Optimization:** Automated testing frees up testers from repetitive tasks, allowing them to focus on more critical aspects of testing.
9. **CI/CD:** _(Continuous Integration/Continuous Deployment)_ Automated testing integrates seamlessly into CI/CD pipelines, enabling rapid and frequent releases without compromising quality.
10. **Regression Testing:** quickly verify that new code changes haven't introduced unintended issues into previously functioning parts of the software.

## What About Cons?
1. Initial Investment
2. Complexity
3. Maintenance Overhead
4. Not suitable for some testing techniques (e.g., usability)
5. Tool and Technology Changes

# Testing Framework
- Tools that enable developers to write automated tests.
- Available in most modern languages
    - For example: Java's JUnit, Python's pytest, C#'s NUnit, Ruby's rspec

> There are multiple frameworks for these programing languages.

- The basic structure of an automated test case (a.k.a. test script)
    - Precondition
    - Action
    - Postcondition

> AAA (Arrange, Act, Assert)