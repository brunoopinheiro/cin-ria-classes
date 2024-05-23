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

Regra geral: uma classe para cada parte `ator`/`caso de uso`.

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
</div>

<h4>Classes de Controle</h4>

> Coordenam o comportamento (lógica de controle) do caso de uso **Interface** entre fronteiras e entidades.

Separação: uso da entidade x comportamento inerente à entidade.

**Usualmente**: uma por caso de uso.
- Várias: Comportamento complexo
- Nenhuma: Manipulação simples da informação.

### Passo 2: Identificar persistência
Identificar quais caso de análise deverão ser persistentes
- Para cada classe, criar uma classe de Cadastro
- Estereótipo: _<\<entity collection>>_
    - Entidades que representam a forma (_no sentido de coleção_) como estas classes serão mantidas (guardadas de forma permanente) no sistema.
    - _É a classe que vai gerenciar a persistência da entidade._
    - Ex.: <font color='#1583dc'>**<\<entity collection>> Cadastro Usuários**</font> é um grupo de <font color='#1583dc'>**<\<entity>> Usuários**</font>

### Passo 3: Distribuir Comportamento
Para cada fluxo de eventos
- Alocar responsabilidades do caso de uso às classes de análise.
- Modelar interações através de diagramas de interação.
    - Pode ser tanto o diagrama de sequencia, quanto o diagrama de colaboração

Estereótipos fornecem **guias**
- Fronteira = envolve comunicação com atores.
- Entidade = envolve informação encapsulada na abstração.
- Controle = envolve comportamento específico do caso de uso.

> _Cadastros são classes que vão controlar a persistência da entidade base._

Desdobramento: **novas classes** ou **relacionamentos**.

**Quantos diagramas?**
- Quantos forem necessários para identificar responsabilidades.
- Pelo menos o fluxo principal do caso de uso.

**Quais diagramas?**
- Sequência: fluxo no tempo, fluxo completo, fluxos complexos
- Colaboração: visualizar relacionamentos e responsabilidade, mais fáceis de desenhar (sessão de _brainstorm_).

### Passo 4: descrever responsabilidades
> Mensagens nos diagramas de interação resultam em responsabilidades nas classes receptores.

É importante refletir sobre os modelos criados
- Classes com responsabilidades similares => combinar?
- Classes com responsabilidades disjuntas => dividir?
- Classes sem ou com apenas uma responsabilidade => reexaminar!
- Classes que interagem com muitas outras => reexaminar!

### Passo 5: Descrever atributos e relacionamentos
**Atributos**
- Informações das classes identificadas
- Informação cujo valor é essencial
- Informação de propriedade exclusiva do objeto.
- Informação que pode ser lida ou escrita por operações
- Informações com comportamento complexo => **nova classe**
- Informação compartilhada => **nova classe**

**Relacionamentos**
- Diagrama de interação: mensagens entre objetos.
- Relacionamento **reflexivo**: comunicação entre objetos da classe.
- **Navegabilidade**: coerente com a direção da mensagem.
- Incluir também o **papel** (_role_) e a **multiplicidade**.

### Passo 6: Revisar os resultados
As classes de análise **satisfazem** os requisitos funcionais?

O modelo está consistente entre si e com os requisitos?

**Criar** novas, **modificar** ou **unificar** as classes de análise.
