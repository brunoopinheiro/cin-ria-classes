# Python - Orientação a Objetos - Herança e Composição

## **Projete e implemente um sistema simples de gerenciamento de veículos com os seguintes requisitos**:
- Crie a classe base `Veiculo` que tem as propriedades comuns a todos os veículos como `fabricante` e `modelo` .
- Crie a classe `Carro` que herda da classe `Veiculo` e adiciona propriedades particulares a carros, como `num_portas` (você está livre para adicionar outras propriedades).
- Crie a classe `Moto` que herda de `Veiculo` and adiciona propriedades particulares a motos, como `tem_sidecar` (você está livre para adicionar outras propriedades).
- Use composição para criar uma classe `Garagem` que pode armazenar múltiplos objetos do tipo `Veiculo`. Esconda a variável que armazena os veículos na garagem, só permitindo acesso e manipulação por meio de métodos `entrar` e `sair` da garagem.
- Use delegação para implementar uma classe `Oficina` que delega os serviços de manutenção de veículos para diferentes classes do tipo `EstacaoServico`.