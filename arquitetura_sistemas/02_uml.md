# Arquitetura de Sistemas - UML
![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/UML_logo.svg/800px-UML_logo.svg.png)
![](https://ideascale.com/wp-content/uploads/2022/03/UML-Diagram.png)

- **Elementos Básicos**
    - Objeto
    - Classe
    - Atributo
    - Operação
    - Interface
    - Componente
    - Pacote
    - Subsistema
    - Relacionamentos
    - Diagramas

# Diagrama de Classes
![](https://www.tutorialspoint.com/uml/images/notation_class.jpg)

## Visibilidade
Marcações (modificadores) de acesso
- \+ publico (_public_)
- \- privado (_private_)
- \# protegido (_protected_)

## Interface
- Especificam apenas a assinatura dos métodos (foco: _o quê_)
- Classes, subsistemas e componentes **implementam** interfaces
- Exemplo: independência do meio de armazenamento
    - Isola as coleções de negócio de mudanças nas coleções de dados

![](https://www.cs.sjsu.edu/~pearce/modules/lectures/oop/basics/interfaces_files/image002.jpg)

## Diferenças: classes, interfaces e classes abstratas
- Classes
    - Atributos e métodos
- Interfaces
    - Assinatura dos métodos
        - Função:
            - $int f(int x) { x = x + 10 }$
        - Assinatura:
            - $int f (int x);$
            - Foco em _o que_ e não em _como_
    - _Não pode ter atributos_
- Classes abstratas
    - Atributos e métodos
    - Assinatura de alguns métodos
        - _Ao menos um método não implementado_

## Component
> Utilizado para representar algo mais físico do sistema, quando se está mais perto da visão de implementação (produção). Quais componentes são, onde rodam.

## Pacote
> Um grupo de classes.
![](https://cdn-images.visual-paradigm.com/guide/uml/what-is-package-diagram/02-simple-package-diagram-example.png)
- Mecanismo para organizar elementos em grupos
- Facilita o entendimento do sistema
- Favorece modularidade e reuso em larga escala
- Essencial para estruturar sistemas complexos

## Subsistema
> Estrutura-se o código em subsistemas, pensando em reutilizá-los em contextos diferentes. Todo subsistema deve ter uma interface.

## Diferença: subsistema e componentes
- Ambos encapsulam um comportamento modelado por interface
- **Subsistemas** representam componentes do modelo de **projeto**
- **Componentes** são a realização física dos subsistemas

## Relacionamentos
![](https://www.researchgate.net/profile/Eliseu-Weber/publication/268395653/figure/fig1/AS:392287784849409@1470540104385/Figura-2-Notacao-grafica-do-diagrama-de-classes-UML-resumido.png)
- Associação
    - Simples (_Navigable association_)
    - Agregação (_Aggregation_)
    - Composição (_Composition_)
- Dependência (_Dependency_)
- Generalização (_Inheritance_)
- Realização (_Realization / Implementation_)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Uml_classes_en.svg/300px-Uml_classes_en.svg.png)

### Associação
> Relação estrutural entre classes

### Agregação
> Tipo especial de associação: relacionamento **todo-parte**
O todo possui um nível de abstração maior que a parte.

### Composição
> Tipo especial de agregação: relação de posse mais forte.

- O todo é responsável pela **criação da parte**.
- A parte não vive sem o todo.
- Não permite compartilhamento.

## Multiplicidade
> Quantos objetos participam de um relacionamento
- Especificado em cada uma das pontas da **associação**
- Exemplo:
    - _Uma pessoa está associada a uma empresa._
    - _Uma empresa está associada a uma ou mais pessoas._

### Navegação
> Indica a direção da associação
- Bidirecionais: mais difíceis de implementar e **acoplam** o modelo.

### Dependência
> Relacionamento não estrutural (denota **uso**)
- Mais fraco do que uma associação.
- Mudança em um elemento pode causar mudanças no outro.
- Dependência entre vários elementos UML
    - (e.g., classes, pacotes, componentes)

### Generalização
Uma classe compartilha a **estrutura** (atributos e relacionamentos) e **comportamento** (operações) de outras classes.
- Subclasse pode adicionar atributos, operações e relacionamentos.
- Tipos de herança: simples e múltipla.
- Herança Múltipla: Problemas potenciais
    - Quando o método não está na subclasse, onde procurar?
    - Superclasses com métodos de mesmo nome.

### Realização
> Um elemento serve como um contrato que o outro deve seguir.

## Mecanismos adicionais de UML
- Estereótipos
- Notas
- Propriedades (_tagged values_)
- Restrições
- OCL (_Object Constraint Language_)

### Estereótipo
> Permitem estender os elementos UML
- Exemplo: classes de fronteira (parte da categorização BCE)

### Notas
> Adicionam informações aos diagramas
- Ligada a um elemento UML

### Propriedades (_tagged values_)
> Permitem estender os elementos de UML
- Exemplos: _persistence, location_ (e.g., cliente ou servidor)

### Restrições
> Criam/modificam regras sobre elementos do modelo

### OCL (_Object Constraint Language_)
> Linguagem para definir/modificar regras sobre elementos do modelo.
- Invariantes de classe
- Pré e pós-condições de operações

# Diagrama de Sequências
![](https://developer.ibm.com/developer/default/articles/the-sequence-diagram/images/3101_figure8.jpg)
