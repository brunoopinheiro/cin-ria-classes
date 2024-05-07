# Aula 2 - Modelos
## SysML
- Linguagens de modelagem tradicionais não suportam a modelagem de aspectos específicos do domínio de sistemas embarcados.
    - Portanto, linguagens específicas para o desenvolvimento de sistemas tem sido propostas, tais como SysML e MARTE.
- SysML (Systems Modeling Language) suporta a especificação, análise, design, verificação e validação de sistemas complexos.
    - Estes sistemas podem incluir hardware, software, informação, processos, pessoal e instalações.
    - Oferece recursos para modelagem de requisitos e relacionamento entre eles.
    - É uma linguagem de propósito geral.
        - Disponíveis propostas específicas para diferentes domínios.

### Taxonomia dos diagramas SysML
![](https://www.omgsysml.org/images/Figure-2.jpg)
- `Behavior Diagram`: Utilizados para visualizar, especificar, construir e documentar **aspectos dinâmicos** de um devido sistema.
- `Structure Diagram`: Existem para visualizar, especificar, construir e documentar os **aspectos estáticos** de um sistema.

### Exemplo: Hybrid SUV
![](https://sparxsystems.com/resources/gallery/diagrams/images/sysml-use-case-hybrid-suv-use-case.png)
![](https://sparxsystems.com/resources/gallery/diagrams/images/sysml-package-diagram-hsuv-analysis.png)
![](https://sparxsystems.com/resources/gallery/diagrams/images/sysml-sequence-diagram-start-vehicle.png)
![](https://sparxsystems.com/resources/gallery/diagrams/images/sysml-activity-diagram-provide-power.png)
![](https://sparxsystems.com/resources/gallery/diagrams/images/sysml-state-machine-diagram-acceleration.png)

## Diagrama de Casos de Uso
### Resumo da Notação
### Atores
- Elemento **externo** que **interage** com o sistema.
    - `Externo`: atores **não** fazem parte do sistema.
    - `Interage`: um ator **troca informações** com o sistema.
- Categorias de atores:
    - **cargos** (Empregado, Cliente, Gerente, Almoxarife, Vendedor, etc);
    - **organizações** (Empresa Fornecedora, Agência de Impostos, Administradora de Cartões, etc);
    - **outros sistemas** (Sistema de Cobrança, Sistema de Estoque de Produtos, etc);
    - **equipamentos** (Leitora de Código de Barras, Sensor, etc);
- Essa categorização indica que o conceito de ator depende do **escopo** do sistema.

### Caso de Uso
- Representa os objetivos que o sistema fornecerá suporte;
- O nome deve consistir em um verbo e um substantivo que descrevem a funcionalidade do sistema.
    - Exemplos: Monitorar Ambiente, Dirigir Veículo, etc.
- Define funcionalidade de um sistema, ***sem revelar a estrutura e o comportamento internos deste sistema***.
- Representado por um símbolo no formato oval com o nome do caso de uso.

### Exemplo - Hybrid gas/electric powered Sport Utility Vehicle (SUV)
![](https://astah.net/manual/sysml-and-system-safety/_images/usecase_dgm.png) 
Dicas ao definir um caso de uso
- Forneça um nome capaz de comunicar seu propósito
- Distribua seus elementos para minimizar o cruzamento de linhas.
- Organize seus elementos de maneira que os comportamentos e papeis semanticamente relacionados apareçam próximos.
- Tente não apresentar muitos tipos de relacionamentos. Se for necessário representá-los, inclua em um novo diagrama.

### Relacionamentos no diagrama de casos de uso
- A UML define diversos relacionamentos
    - _Comunicação_
    - _Inclusão_
    - _Extensão_
    - _Generalização_
- Para cada um desses elementos, a UML define uma notação gráfica e uma semântica específicas.

|    | Entre Atores | Entre Casos de Uso | Entre Ator e Caso de Uso |
|:---:|:---:|:---:|:---:|
| Comunicação | | | X |
| Inclusão | | X | |
| Extensão | | X | |
| Generalização | X | X | |

## Relacionamentos
### Comunicação
Conecta atores e caso de uso.
### Inclusão (Include)
Fornece mecanismos para incluir uma funcionalidade comum que é compartilhada entre varios casos de uso e é necessária para atingir os objetivos do ator do caso de uso de base a ser cumprido.
### Extensão (Extend)
Fornece funcionalidade opcional (opcional no sentido de não ser obrigado a cumprir os objetivos), que estende o caso de uso base em pontos de extensão definidos em condições especificadas.
### Generalização
Fornece um mecanismo para especificar variantes do caso de uso base.

## Fronteira do Sistema
- Fornece a funcionalidade que suporta os casos de uso;
- Representa um sistema que está sendo desenvolvido;
- Representado por um retângulo no diagrama de caso de uso;

![](https://templates.visual-paradigm.com/repository/images/36994afe-da24-490b-a738-ec69389e6848/use-case-diagram-design/use-case-diagram-multiple-projects-with-system-boundaries.png)

## Diagrama de Estados
### Para Que É Usado?
- Representação de comportamentos de um sistema;
- Possui um número de estados finitos;
- Comportamentos possíveis em cada estado;
- Quais mudanças são possíveis:
    - O que causa as mudanças de estado.
- Diagramas de estado expressam comportamento.
    - O que acontece em um sistema em uma determinada condição.

### Notação
- Estado
- Transição
- Evento
- Ação
    - Nas transições
    - Nos estados
- Condições de guarda

### Estado
- Tempo durante o qual o objeto satisfaz alguma condição.
- Uma configuração do sistema (ou entidade);
- Cada possível atribuição de valores aos atributos é um "estado";
- Uma situação conhecida.

**Exemplos:**
- Sala
    - Disponível
    - Em uso
    - Em reforma
- Aluno
    - Aprovado
    - Não aprovado
- Impressora
    - Imprimindo
    - Ociosa
    - Aguardando Papel

### Transição
- Representa mudança de estado;
- Evento + Condição + Ação;
- Evento:
    - Algo que acontece;
    - Estímulo externo ou interno;
    - Pode disparar uma transição.
- Condição:
    - Algo que deve ser verdade ou então a transição não será realizada.
    - Também conhecido como "guarda".
        - Quando um evento ocorre no estado A, se a condição C for verdadeira no momento, o sistema transfere para o estado B.

### _Statecharts_
- Proposto por David Harel em 1987
- Artigo Statecharts: A visual formalism for complex systems
- Diagramas de estado com mecanismos adicionais para:
    - lidar com a complexidade
    - melhorar a expressividade
- Parte da UML e SysML
- Suporte Ferramental
    - Modelagem, simulação e geração de código.
- Formalização
    - Raciocínio
- [Conceitos de Álgebra Booleana](https://www.inf.pucrs.br/emoreno/undergraduate/EC/cirdig/class_files/Aula02.pdf)

### Hierarquia
- Super e sub estados
- XOR-estados

### História
- Aciona o último sub-estado ativo nesse estado.
- Exemplo:
    - Ao exibir um alarme, ele será ligado ou desligado, de acordo com se ele estava ligado ou desligado antes.

### Hierarquia X Ortogonalidade
- Independência e Concorrência
- AND-estados

### Entrada Condicional
- Agrupa um conjunto de transições em um único evento com várias condições.

### Ações
- nas Transições
- nos Estados

## Diagrama de Blocos
- O diagrama de blocos representa os elementos estruturais do sistema denominados blocos, sua composição e classificação.
- Um Bloco é o elemento estrutural básico usado para modelar parte da estrutura do sistema.
- O diagrama é usado para descrever
    - Os blocos presentes no sistema
    - Como os blocos se relacionam
    - Características estruturais do bloco
    - Características funcionais do bloco incluem operações e recepções.

### Blocos
- Modelam qualquer tipo de entidade dentro do sistema de interesse ou no ambiente externo ao sistema.
    - **Exemplo**: Desktop Workstation representa um conjunto de propriedades como monitor, teclado, mouse, CPU, disco rígido, fabricante, custo, etc.
- _Optional compartments_
    - _Structural Features (or properties)_
        - _Parts_
        - _References_
        - _Values_
        - _Constraints_
        - _Ports_
            - _Standard - Full ports (in SysML v1.3)_
            - _Flow - Proxy ports (in SysML v.1.3)_
    - _Behavioural Features_
        - _Operations_
        - _Receptions_

| <<`block`>> Flight Computer |
|:---:|
| _constraints_ sm: Sufficient Memory |
| _values_ memoryCapacity: Mb dataPerOrbit: Mb |

### Propriedades das Partes
> Representam uma estrutura que é **interna** a um bloco, ou seja, um bloco `é composto` de suas propriedades "part" (noção de propriedade).

**Exemplo**: Podemos instalar uma determinada antena em apenas um satélite de cada vez, e não em dois ou mais simultaneamente. Porém, essa antena pode ser removida de um satélite e reinstalada em outro em algum momento.

**Sintaxe**: `<part name>: <type> [<multiplicity>]`
- `part name`: de acordo com o analista
- `type`: é o nome do bloco criado anteriormente
- `multiplicity`: é uma restrição no número de instâncias que a propriedade part pode representar dentro da composição, expressa como um único inteiro ou como um intervalo de inteiros. 0..* ou * (zero ou mais). Default é 1.

### Propriedades das Referências
> Representam uma estrutura **externa** a um bloco.

Um bloco com uma propriedade de referência `precisa dessa estrutura externa para algum propósito`, seja fornecer um serviço ou para trocar matéria, energia ou dados. Isso implica que algum tipo de conexão deve existir entre eles.

**Sintaxe**: `<reference name>:<type>[<multiplicity>]` 0..* default 1

### Propriedades dos Valores
> Podem representar uma quantidade (de algum tipo), um Booleano ou uma String. Na maioria das vezes é uma propriedade na qual você pode atribuir um valor.

**Sintaxe**: `<value name>:<type>[<multiplicity>]=<default value>` 0..* dafault 1

### Porta
> Representa um **ponto de interação** na fronteira de uma estrutura por meio da qual `entidades externas podem interagir` com essa estrutura. Seja para fornecer ou solicitar um serviço ou para trocar matéria, energia ou dados.

**Tipos**: standard port ou flow port.

- ***Standard Ports***
    - Modela os serviços (comportamentos) que um bloco fornece ou exige.
- ***Flow Ports***
    - Modela os tipos de matéria, energia ou dados que podem ser recebidos ou transmitidos.
    - **Sintaxe**: `<direction><name>:<type>`

### Interface
> Define um conjunto de **operations** (fornece serviço) e **receptions** (solicita serviço).

**Sintaxe**: `<operation name>(<parameter list>:<return type>)[<multiplicity>]`

### Behavioral Features - Operations
> Representa o comportamento assíncrono que um **bloco executa quando um cliente o chama**. Declarado formalmente, uma operação é invocada por um _call event_.

**Sintaxe**: `<operation name>(<parameter list>):<return type>[<multiplicity>]`

### Behavioral Features - Receptions
> Representa um comportamento que um **bloco executa quando um cliente envia um sinal que o aciona**. Declarado formalmente, uma recepção é invocada por um _signal event_.

**Sintaxe**: `<<signal>><reception name>(<parameter list>)`

## Relacionamento Entre Blocos
**Reference**: Significa que uma conexão pode existir entre instâncias desses blocos em um sistema.

**Associação/Composição (Composite)**: Representa decomposição estrutural. Uma instância do bloco na extremidade composta é constituida por um certo número de instâncias do bloco na extremidade.

**Generalização**: Relacionada ao conceito de herança e especializações. Operações e variáveis se repetem.

**Dependência**: um elemento do modelo, o cliente, depende de outro elemento do modelo, o fornecedor.