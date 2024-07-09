# Exercício 1 - 09.07.2024
Envolve _Singleton_, _Factory_, e _Observer_.

## Tarefas
- Crie uma classe `Logger` usando o padrão _Singleton_ para garantir que apenas uma instância do objeto esteja executando e realizando o logging.
    - A classe deve ter um método `log` que recebe uma string (`mensagem`) e imprime na tela a mensagem `"LOG: {mensagem}"`
- Implementar uma classe _Factory_ de formas geométricas (`FormaFactory`) para criar diferentes tipos de formas. Dê suporte para, pelo menos, círculos (`Circulo`) e quadrados (`Quadrado`), pode incluir mais formas, se desejar.
- Use o padrão _Observer_ para notificar uma classe chamada `Tela` toda vez que uma nova forma for criada (lembrar de criar uma classe para funcionar de sujeito e a classe `Tela` vai funcionar de `Observer`).