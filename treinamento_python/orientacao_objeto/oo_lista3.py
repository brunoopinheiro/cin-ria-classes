# 1) Crie uma classe Cliente que possui nome, sobrenome e cpf.









# 2) Crie uma classe abstrata Conta que descreve os método depositar, sacar, transferir e extrato e que possui um número de identificação, 
# um titular do tipo Cliente criado na questão anterior 1, saldo
#  - depositar: adiciona valor no saldo da conta.
#  - sacar: retira valor no saldo da conta
#  - tranferir: transfere valor para uma conta destino
#  - extrato: Exibe o número da conta e o saldo associado









# 2) Crie uma classe Conta Corrente que herda de Conta que possui um limite associado e pré definido e defina os métodos de Conta em Conta Corrente









# 3) Crie uma Classe Conta Investimento que herda de Conta e possui um atributo de saldo investimento e a taxa do investimento. 
# 1-Nessa Classe o Cliente pode escolher debitar ou sacar do saldo investimento além do seu saldo de Conta.
# 2-Implemente o método resgatar investimento que soma o saldo do investimento com o saldo da Conta e resgata para o saldo da Conta.
# 3-Implemente um método que define um valor bonus a ser resgatado dependendo de quanto valor o Cliente tem na Conta Investimento
#     - Se saldo investimento > 100000 -> bonus = 1000
#     - Se saldo investimento >= 50000 e < 100000 -> bonus = 500
#     - Se saldo investimento < 50000 -> bonus = 100
# 4-Implemente um método que resgata o bonus quando solicitado.










# 4) Crie uma classe Conta Poupança que herda da Classe Conta e possui uma taxa de juros de rendimento.
# 1-Nessa Classe o Cliente pode render os juros só quando o valor de saldo da conta poupança for maior que 1000.
# 2-Implemente o método alterar taxa que gera uma nova taxa aleatória para a Conta entre 0.5 e 1.2








# 5) Crie uma classe Historico que possui uma data de abertura (use datetime para pegar a hora atual) e uma lista de transações inicialmente vazia.
# Nessa classe temos o método imprime que nos retorna todas as transacoes feitas daquela conta.
# Modifique a classe Conta para receber tbm um historico de transações 
# e todos os métodos das classes que herdam de Conta precisam salvar os debitos, 
# saques e transferencias na na lista de transações da classe Historico.







# 6) Crie um arquivo main e faça algumas transações e display de informações para testar o código (tente dar total cobertura de todos os métodos e classes).