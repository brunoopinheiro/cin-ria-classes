# Projetar Arquitetura - Aula 1
## Relembrando: analisar casos de uso
Passos:
1. Encontrar classes de análise (para **cada caso de uso**);
2. Identificar necessidades de persistência (para **cada caso de uso**);
3. Distribuir Comportamento (para **cada caso de uso**);
4. Descrever responsabilidades (para **cada classe**);
5. Descrever atributos e relacionamentos (para **cada classe**);
6. Revisar os resultados.

Lembrando: **BCE** são estereótipos de análise.

## Projetar Arquitetura
Objetivo
- Avaliar o **conjunto** de classes de análise;
- Definir elementos de **projeto** (classes de projeto e subsistemas);
- Organizar os elementos de projeto em **pacotes**;
- Definir a estrutura da aplicação.

Reuso de Soluções: Padrões
- Padrões de projeto;
- Padrões Arquiteturais.

> Metodologias Ágeis dividem o processo em pequenas partes, priorizando funcionalidades a serem desenvolvidas, e deixando o projeto (macro) de forma mais abstrata, focando a analise apenas no conjunto de funcionalidades de cada _sprint_.

## Passo a Passo
1. Mapear classes de análise em elementos de projeto (elementos = **classes** e **subsistemas**)
    - Identificar classes que representem o mesmo elemento.
    - Documentar relação classe de análise -> classe de projeto
2. Identificar oportunidades de reuso
3. Definir a estrutura da aplicação

### Passo 1: Mapear em Elementos de Projeto
1. Identificar classes de projeto;
2. Identificar subsistemas;
3. Especificar a interface dos subsistemas;
4. Realizar o mapeamento.

Observações:
- 1 classe da análise → 0...n elementos de projeto;
- Mapeamento _m:n_

### Passo 1.1: Identificar classes de projeto
Recomendações Gerais
- Classe de análise **simples** → única classe de projeto
- Classe de análise **muito simples** → podem ser combinadas
- Classes de análise **complexas** → divididas ou virar subsistemas.

### Passo 1.1 Exemplo QIB
Conta
- Responsabilidades distintas: controle de acesso e conta bacária
- Separação favorece reuso.

![](diagrams/projeto_sistemas.drawio.png)

```java
class ContaInternet {
    private String login;
    private String senha;

    private ContaCorrente credenciais;

    public void m() {
        ContaCorrente conta = new ContaCorrente();
        // 'conta' does something here
    }

}

class ContaCorrente {
    private String numero;
    private double saldo;

}
```
### Passo 1.2: Identificar Subsistemas
Permitem dividir o sistema em partes independentes (componentes).
- Desenvolvido, testado e implantado de forma independente;
- Abstração de produtos ou sistemas externos.

Possíveis fonte (classes de análise):
- Classes de fronteira (interfaces com sistemas externos)
- Classes que fornecem serviços complexos

Possíveis fontes (componentes reutilizáveis):
- Software de comunicação;
- Acesso ao BD;
- Bibliotecas de utilitários;
- Produtos específicos da aplicação.
