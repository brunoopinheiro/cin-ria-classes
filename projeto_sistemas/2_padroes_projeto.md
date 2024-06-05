# Padrões de Projeto - Aula 2
## 1. Introdução
Não é fácil projetar software orientado a objetos reusáveis
- Experiência prévia é fundamental

Padrões de projeto sistematicamente nomeiam, explicam e avaliam **soluções recorrentes** no projeto de software orientado a objetos.
- Nome do padrão
- O problema
- A solução
- As consequências

## 2. Padrões de Projeto
No livro [**Design Patterns**](https://en.wikipedia.org/wiki/Design_Patterns):
|  |  |
| --- | --- |
| Nome do padrão e classificação | Objetivo |
| Nomes alternativos | Motivação |
| Aplicabilidade | Estrutura (OMT) |
| Participantes | Colaborações |
| Consequências | Implementação |
| Exemplo de Código | Usos reais |
| Padrões Relacionados |  |

### 2.1. Catálogo de 23 Padrões de Projeto

| Padrão | Escopo | Propósito |
| :---: | :---: | :---: |
| Factory Method (107) | Class | Creational |
| Abstract Factory (87) | Object | Creational |
| Builder (97) | Object | Creational |
| Prototype (117) | Object | Creational |
| Singleton (127) | Class | Creational |
| Adapter (139) | Class | Structural |
| Adapter (139) | Object | Structural |
| Bridge (151) | Object | Structural |
| Composite (163) | Object | Structural |
| Decorator (175) | Object | Structural |
| Facade (185) | Object | Structural |
| Flyweight (195) | Object | Structural |
| Proxy (207) | Object | Structural |
| Interpreter (219) | Class | Behavioral |
| Template Method (325) | Class | Behavioral |
| Chain of Responsibility (223) | Object | Behavioral |
| Command (233) | Object | Behavioral |
| Iterator (257) | Object | Behavioral |
| Mediator (273) | Object | Behavioral |
| Memento (283) | Object | Behavioral |
| Observer (293) | Object | Behavioral |
| State (305) | Object | Behavioral |
| Strategy (315) | Object | Behavioral |
| Visitor (331) | Object | Behavioral |

### 2.1.1. Critérios
**Propósitos**
- **Creational**: processo de criação de objetos;
    - **Class**: subclasses decidem qual objeto criar;
    - **Object**: delega a criação de objetos para outra classe.
- **Structural**: composição de classes e objetos;
    - **Class**: usa herança para compor classes;
    - **Object**: descreve como compor objetos para formar estruturas maiores.
- **Behavioral**: como classes e objetos interagem.
    - **Class**: usa herança para descrever algoritmos e fluxos de controle;
    - **Object**: Como objetos cooperam para realizar tarefa conjunta.

**Escopo**
- **Class**: relação entre classes e subclasses (estáticos);
- **Object**: relação entre objetos (dinâmicos) ← _a maioria_.

Alguns padrões são normalmente utilizados com outros: `Composite` com `Iterator` ou `Visitor`.

Alguns padrões representam possibilidades alternativas: `Prototype` é normalmente uma alternativa para `Abstract Factory`.

Alguns padrões criam estruturas parecidas com objetivos diferentes: `Composite` e `Decorator`.

Padrões de projeto possuem **relações entre si**!

### 2.2. Nosso foco: 10 dos 23 padrões
- **Criacionais**
    - Classe: _Factory Method_
    - Objeto: _Abstract Factory_, _Singleton_
- **Estruturais**
    - Classe: _Adapter_
    - Objeto: _Adapter_, _Composite_, _Decorator_, _Facade_
- **Comportamentais**
    - Classe: _Template Method_
    - Objeto: _Observer_, _Strategy_

### 2.2.1. Criacional + Classe: _Factory Method_ (107)
Define uma interface para criar um objeto, mas delega para as subclasses a decisão de que classe instanciar.

![](https://realpython.com/cdn-cgi/image/width=960,format=auto/https://files.realpython.com/media/The-Factory-Method-Pattern-in-Python_Watermarked.6516a91d4d41.jpg)
[_Real Python: Factory Method_](https://realpython.com/factory-method-python/)

Implementação simples do padrão _Factory Method_ em `Python`:
```python
from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def save(self):
        print("Document saved in", self.filename)

    def revert(self):
        print("Document reverted to last saved state")


class MyDocument(Document):
    def __init__(self, filename):
        self.filename = filename

    def open(self):
        print("MyDocument opened")

    def close(self):
        print("MyDocument closed")


class Application(ABC):
    def __init__(self):
        self.documents = []

    @abstractmethod
    def create_document(self, filename):
        pass

    def new_document(self, filename):
        doc = self.create_document(filename)
        self.documents.append(doc)
        return doc

    def open_document(self, filename):
        doc = self.create_document(filename)
        doc.open()
        self.documents.append(doc)
        return doc


class MyApplication(Application):
    def create_document(self, filename):
        return MyDocument(filename)
```

### 2.2.2. Criacional + Objeto: _Abstract Factory_ (87)
Provê uma interface para criar famílias de objetos dependentes ou relacionados sem precisar especificar suas classes concretas.

![](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-en-2x.png?id=a488ca862db731876fa0513bb2105640)
[_Refactoring Guru: Abstract Factory_](https://refactoring.guru/design-patterns/abstract-factory)

### 2.2.3. Criacional + Objeto: _Singleton_ (127)
Garante que uma classe só terá uma instância e provê um ponto global de acesso a ela.

![](https://refactoring.guru/images/patterns/content/singleton/singleton-2x.png?id=accb2cc7594f7a491ce01dddf0d2f876)
[_Refactoring Guru: Singleton_](https://refactoring.guru/design-patterns/singleton)

Implementação simples do padrão _Singleton_ em `Python`:
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

Implementação do padrão _Singleton_ em `Java`:
```java
public class Fachada {

    private int x = 0;
    private static Fachada instance = null;

    private Fachada() {

    }

    public static Fachada getInstance() {
        if (Fachada.instance == null) {
            Fachada.instance = new Fachada();
        }
        return Fachada.instance;
    }

    public int getX() {
        return x;
    }

    public void setX(int v) {
        this.x = v;
    }
}


public class Programa {

    public static void main(String[] args) {
        Fachada f1 = Fachada.getInstance();
        Fachada f2 = Fachada.getInstance();

        System.out.println(f1);
        System.out.println(f2);

        f1.setX(20);
        System.out.println(f2.getX());
    }
}
```

> **ATENÇÃO**: _Singletons_ e _Fachadas_ são considerados um ponto de gargalo no sistema. É importante atentar para a carga a ser suportada pela instância dessa classe.

### 2.2.4. Estrutural + Objeto: _Adapter_ (139)
Converte a interface de uma classe em outra interface que o cliente espera encontrar.

![](https://refactoring.guru/images/patterns/content/adapter/adapter-en-2x.png?id=e0ab0f6103b0b7b0648a8fda592ffab8)
[_Refactoring Guru: Adapter_](https://refactoring.guru/design-patterns/adapter)

