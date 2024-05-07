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

Exemplos:
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