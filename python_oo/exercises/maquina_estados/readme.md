### Exercício: Implementando uma Máquina de Estados para uma Máquina de Café

**Objetivo**: O objetivo deste exercício é aplicar os conceitos de máquinas de estados usando a biblioteca `transitions`, criando uma máquina de estados para uma máquina de café. 

**Cenário**:
Você foi encarregado de implementar uma máquina de estados para uma máquina de café. A máquina de café possui vários estados em que pode estar, e ela transita entre esses estados com base nas entradas do usuário e nas condições da máquina.

**Estados**:
1. **Idle**: A máquina de café está esperando por uma entrada do usuário.
2. **Selecting**: O usuário está selecionando o tipo de café.
3. **Paying**: O usuário está fazendo o pagamento.
4. **Brewing**: A máquina de café está preparando o café.
5. **Dispensing**: A máquina de café está dispensando o café.
6. **Out of Order**: A máquina de café está fora de serviço devido a algum problema.

**Transições**:
1. **start**: Transita de `Idle` para `Selecting`.
2. **select_coffee**: Transita de `Selecting` para `Paying`.
3. **pay**: Transita de `Paying` para `Brewing`.
4. **brew_complete**: Transita de `Brewing` para `Dispensing`.
5. **dispense_complete**: Transita de `Dispensing` para `Idle`.
6. **error**: Transita de qualquer estado para `Out of Order`.
7. **reset**: Transita de `Out of Order` para `Idle`.

**Ações**:
1. **on_enter_Brewing**: Inicia a preparação do café.
2. **on_enter_Dispensing**: Dispensa o café.
3. **on_enter_Out of Order**: Trata a condição de erro.

**Passos**:
1. **Definir os estados**: Use a biblioteca `transitions` para definir os estados da máquina de café.
2. **Definir as transições**: Use a biblioteca `transitions` para definir as transições entre os estados.
3. **Implementar a classe CoffeeMachine**: Defina a classe CoffeeMachine com métodos para cada estado e transição.
4. **Testar a máquina de estados**: Crie uma instância da classe CoffeeMachine e simule a interação do usuário com a máquina de café.