# Arquitetura de Sistemas - Análise de Casos de Uso
## Essência: modelar antes de programar
- Engenharia de software: ***model-driven development***
- Em alguns contextos: **model => code** de forma (semi)automática.
- Diferenças: **análise** x **projeto** de sistemas
    | Análise | Projeto |
    |:---|:---|
    | Foco no problema | Foco na solução |
    | Visão geral da arquitetura | Proximidade com o código |
    | Foco em RF | Foco em RNF |
    | Modelo mais simples | Modelo mais complexo |
- Atributos de qualidade
    - Correto, complexo, extensível, fácil entendimento, etc.
    - **Coesão** (proximidade das partes) + **Acoplamento** (intensidade das conexões)
        > **Coesão**: Uma classe deve ter tudo o que é necessário para representar o conceito, **e nada mais**.
        > **Acoplamento**:

        > Buscar **Alta Coesão** e **Baixo Acoplamento**

## Analisar casos de uso
Objetivo: encontrar classes iniciais (análise) e distribuir comportamento
Passos (_do **RUP**_):
1. <mark>Encontrar classes de análise (para cada **caso de uso**).</mark>
2. Identificar necessidades de persistência (para cada **caso de uso**).
3. <mark>Distribuir comportamento (para cada **caso de uso**).</mark>
4. Descrever responsabilidades (para cada **classe**).
5. Descrever atributos e relacionamentos (para cada **classe**).
6. <mark>Revisar os resultados.</mark>

### Passo 1: encontrar classes de análise
Categorização **BCE**
- B = _boundary_ (fronteira)
- C = _control_ (controle)
- E = _entity_ (entidade)

![](https://www.visual-paradigm.com/servlet/editor-content/guide/uml-unified-modeling-language/robustness-analysis-tutorial/sites/7/2019/08/robustness-analysis-diagram-symbols.png)
Esses estereótipos desaprecem no projeto de sistemas.

<h4>Classes de Fronteira</h4>

> Modelam a interação entre o sistema e o seu ambiente. Isolam o sistema de mudanças do ambiente externo. Atores devem se comunicar apenas com classes de fronteira.

Exemplos:
- GUI;
    - Foco: **informações** apresentadas (não: projeto gráfico)
- Interface com outros sistemas;
- Interface com dispositivos.
    - Foco: quais protocolos devem ser definidos (não: implementação)

FOCO: Responsabilidades

<h4>Classes de Entidade</h4>

> Abstrações e **conceitos chave** dos casos de uso. Armazenam e controlam informações do sistema.

Fontes:
- Conhecimento do negócio.
- Glossário.
- Modelo de negócios.
- Documento de requisitos.
- Especificações do caso de uso.
<br><br>

Orientações gerais a partir da descrição do caso de uso.
- Identifique **substantivos**
- Remova candidatos redundantes e vagos.
- Remova atores que apenas interagem com o sistema.
- Remova atributos e operações.

<div style="border: 2px solid; padding: 8px; margin: 4px;">
<h4>Classes de Entidade: Efetuar Login</h4>

Este caso de uso é responsável por autenticar um usuário do sistema.

**Pré-condição**: nenhuma
**Pós-condição**: um usuário válido é logado e sua sessão é registrada no sistema.

**Fluxo de eventos principal**
1. O cliente informa login e senha.
2. O sistema verifica se o login e a senha são válidos (verifica-se se o login e senha pertencem a uma conta).
3. O sistema registra o início de uma sessão de uso.

**Fluxos secundários**
- No passo 2, se o login ou a senha forem inválidos, o sistema exibe uma mensagem e volta ao passo 1.
<br/><br/>
<div style="border: 1px dashed">
    <h5>Classes: </h5>
    <ul>
        <li>Usuário</li>
        <li>Conta</li>
        <li>Sessão</li>
    </ul>
</div>
</div>