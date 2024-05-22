# Arquitetura de Sistemas - Introdução
![](https://calegari.dev/pt-br/posts/arquiteturas-de-sistemas-distribuidos/featured-image.png)
> À partir dos requisitos, entender e identificar os elementos do sistema (mas não definir efetivamente ainda).

**Motivação: desenvolvimento, <font color='#214278'>manutenção</font> e <font color='#214278'>reuso</font>**

- Classroom:
    - Plano de aulas
    - Slides
    - Códigos
    - Práticas
- Dinâmica de aulas
    - Práticas: **Visual Paradigm** ou **Astah**
- Diâmica da avaliação
    - _Prova escrita Individual_
- Bibliografia
    - Eduardo Bezerra. _Princípios de Análise e Projeto de Sistemas com UML._ GEN LTC; 3ª edição (2014)

## Por Quê Orientação a Objetos?
- Tipo: um conjunto de **valores**
    - Primitivo X Composto
- Tipo de dados: **tipo** + **operações**
- Tipo abstrato de dados: foco em ***o quê*** (não em _como_)
- Estrutura de dados: foco em ***como*** (não em _o quê_)
    - Multiplas implementações para o mesmo ADT (_Abstract Data Type_)
- Exemplo: **pilha** 
    - (_Uma possível implementação_)
    - Valores: coleção de <font color="green"> _int_ </font>
    - Operações:
        - _push_ (adicionar)
        - _pop_ (retirar)
        - _length_ (tamanho)

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230726165552/Stack-Data-Structure.png)

```c
#include <stdlib.h>
#include <stdio.h>
#include "stack.h"

void main() {
    STACK *s = create_stack();
    push(s, 20);
    push(s, 30);
    push(s, 50);
    pop(s);

    printf("size = %d\n", length_stack(s));

    print_stack(s);
    destruct_stack(s);
}

```

### Linguagens imperativas e estruturadas
Problemas
- Baixa coesão
- Sem controle de acesso
- Sem garantias de consistência
- Replicação de código

### Linguagens Imperativas e Orientadas a Objetos
Conceitos Básicos:
- Classes definem um tipo de dados
    - Tipo: atributos
    - Operações: métodos
- Objetos são instâncias de uma classe

Princípios Fundamentais
- Encapsulamento
- Polimorfismo

### Encapsulamento
> A maneira como os usuários do código interfarem com aquele objeto são controlados por uma interface. E um atributo do objeto só pode ser modificado internamente.

- Promove: alta coesão
- Modificadores de acesso:
    - public
    - private
    - protected

### Polimorfismo
Tipos:
- Coercion polymorphism (_casting_)
- Ad hoc polymorphism (_overloading_)
- Parametric polymorphism
- Inclusion polymorphism (_overriding_)

```python
# Definition of class Node
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

# Definition of class Stack using linked lists
class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def top(self):
        if self.top != None:
            return self.top.data

    def push(self, data):
        self.top = Node(data, self.top)
        self.size = self.size + 1

    def pop(self):
        if self.top != None:
            value = self.top.data
            self.top = self.top.next
            self.size = self.size - 1
            return value
        
    def clear(self):
        while self.size != 0:
            self.pop()
        
    def length(self):
        return self.size

    def __str__(self):
        values = []
        current = self.top
        while current != None:
            values = [str(current)] + values
            current = current.next
        return "base = " + str(values) + " = top"

# main program
if __name__ == "__main__":
    pilha = LinkedStack()
    pilha.push(3)
    pilha.push(5)
    pilha.push(7)
    print("Top value: " + str(pilha.top))
    print(pilha)
    print("\n")
        
    v = pilha.pop()
    print("Removed: " + str(v))
    print(pilha)
    print("\n")

    v = pilha.pop()
    v = pilha.pop()
    v = pilha.pop()
    print("Removed: " + str(v))
    print(pilha)
    print("\n")

    pilha.push(13)
    pilha.push(11)
    print("Size: " + str(pilha.length()))
    pilha.clear()
    print("Size: " + str(pilha.length()))
```

```java

public interface Stack<T> {

    public void print();
    public void clear();
    public void push(T v);
    T pop() throws StackException;
    T topValue() throws StackException;
    int length();

}
```

```java

public class Main {

	public static void main(String[] args) {
		Stack<Integer> s = new LStack<Integer>();
		
		s.push(20);
		s.push(30);
		s.push(50);
		try {
			s.pop();			
		} catch (StackException e) {
			System.err.println("This should not happen!");
			System.err.println(e);
		}

		s.print();
		System.out.println("size = " + s.length());
		

	}
	
}

```

### Linguagens Imperativas e Orientadas a Objetos
Problemas prévios
- Baixa coesão => **Encapsulamento**
- Sem controle de acesso => **Modificadores de Acesso**
- Sem garantias de consistência => **Interfaces**
- Replicação de código => **Polimorfismo**

## UML
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

![](https://www.tutorialspoint.com/uml/images/notation_class.jpg)

### Visibilidade
Marcações (modificadores) de acesso
- \+ publico (_public_)
- \- privado (_private_)
- \# protegido (_protected_)

### Interface
- Especificam apenas a assinatura dos métodos (foco: _o quê_)
- Classes, subsistemas e componentes **implementam** interfaces
- Exemplo: independência do meio de armazenamento
    - Isola as coleções de negócio de mudanças nas coleções de dados

![](https://i.sstatic.net/VVx6e.gif)

### Diferenças: classes, interfaces e classes abstratas
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

### Component
> Utilizado para representar algo mais físico do sistema, quando se está mais perto da visão de implementação (produção). Quais componentes são, onde rodam.

### Pacote
> Um grupo de classes.
![](https://cdn-images.visual-paradigm.com/guide/uml/what-is-package-diagram/02-simple-package-diagram-example.png)
- Mecanismo para organizar elementos em grupos
- Facilita o entendimento do sistema
- Favorece modularidade e reuso em larga escala
- Essencial para estruturar sistemas complexos

### Subsistema
> Estrutura-se o código em subsistemas, pensando em reutilizá-los em contextos diferentes. Todo subsistema deve ter uma interface.

### Diferença: subsistema e componentes
- Ambos encapsulam um comportamento modelado por interface
- **Subsistemas** representam componentes do modelo de **projeto**
- **Componentes** são a realização física dos subsistemas

### Relacionamentos
- Associação
    - Simples
    - Agregação
    - Composição
- Dependência
- Generalização
- Realização
