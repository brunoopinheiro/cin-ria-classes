# Imports
from typing import List, Any
from cmath import (
    sqrt,
    # cos,
    # sin,
    )
from random import (
    seed,
    choice,
    sample,
    )
from datetime import date


# 1) Crie uma classe chamada Invoice que possa ser utilizado
# por uma loja de suprimentos de informática
# para representar uma fatura de um item vendido na loja.
# Uma fatura deve incluir as seguintes informações como atributos:
# • o número do item faturado,
# • a descrição do item,
# • a quantidade comprada do item e
# • o preço unitário do item.
# Sua classe deve ter um construtor que inicialize os quatro atributos.
# Se a quantidade não for positiva, ela deve ser configurada como 0.
# Se o preço por item não for positivo ele deve ser configurado como 0.0.
# Forneça um método set e um método get para cada variável de instância.
# Além disso, forneça um método chamado # getInvoiceAmount
# que calcula o valor da fatura
# (isso é, multiplica a quantidade pelo preço por item)
# e depois retorna o valor como um double.
# Escreva um aplicativo de teste
# que demonstra as capacidades da classe Invoice.
class Invoice():
    def __init__(
        self,
        item_cod: int,
        description: str,
        quantity: int = 0,
        unt_price: float = 0.0,
    ):
        if quantity < 0:
            quantity = 0
        if unt_price < 0:
            unt_price = 0.0

        self._item_cod = item_cod
        self._description = description
        self._quantity = quantity
        self._unt_price = unt_price

    def get_itemcod(self) -> int:
        return self._item_cod

    def set_itemcod(self, new_code) -> int:
        self._item_cod = new_code
        return self.get_itemcod()

    def get_description(self) -> str:
        return self._description

    def set_description(self, new_desc: str) -> str:
        self._description = new_desc
        return self.get_description()

    def get_quantity(self) -> int:
        return self._quantity

    def set_quantity(self, new_quantity: int) -> int:
        if new_quantity < 0:
            return self.get_quantity()
        self._quantity = new_quantity
        return self.get_quantity()

    def get_untprice(self) -> float:
        return self._unt_price

    def set_untprice(self, new_price: float) -> float:
        if new_price < 0:
            return self.get_untprice()
        self._unt_price = new_price
        return self.get_untprice()

    def get_invoice_amount(self) -> float:
        return float(self.get_untprice() * self.get_quantity())

    def get_report(self) -> str:
        return f'''
        Produto: {self.get_itemcod()}
        Descrição: {self.get_description()}
        Estoque: {self.get_quantity()} und.
        Preço Und.: R$ {self.get_untprice():.2f}
        Invoice: R$ {self.get_invoice_amount():.2f}
        '''


def test_invoice():
    product_1 = Invoice(1, 'Produto 1', 5, 150.45)
    print(product_1.get_report())
    product_1.set_quantity(3)
    product_1.set_untprice(299.99)
    print(product_1.get_report())

    product_2 = Invoice(2, 'Produto 2', -3, -99)
    print(product_2.get_report())


# 2) A fim de representar empregados em uma firma,
# crie uma classe chamada Empregado que
# inclui as três informações a seguir como atributos:
# • um primeiro nome,
# • um sobrenome, e
# • um salário mensal.
# Sua classe deve ter um construtor que inicializa os três atributos.
# Forneça um método set e get para cada atributo.
# Se o salário mensal não for positivo, configure-o como 0.0.
# Escreva um aplicativo de teste que demonstra as capacidades da classe.
# Crie duas instâncias da classe e exiba o salário anual de cada instância.
# Então dê a cada empregado um aumento de 10%
# e exiba novamente o salário anual de cada empregado.
class Empregado():
    def __init__(
        self,
        first_name: str,
        last_name: str,
        monthly_payment: float,
    ):
        if monthly_payment < 0:
            monthly_payment = 0.0
        self._first_name = first_name
        self._last_name = last_name
        self._monthly_payment = monthly_payment

    def get_firstname(self) -> str:
        return self._first_name

    def get_lastname(self) -> str:
        return self._last_name

    def get_monthlypayment(self) -> float:
        return self._monthly_payment

    def set_firstname(self, name: str) -> str:
        self._first_name = name
        return self.get_firstname()

    def set_lastname(self, name: str) -> str:
        self._last_name = name
        return self.get_lastname()

    def set_monthlypayment(self, new_value: float) -> float:
        if new_value < 0:
            new_value = 0.0
        self._monthly_payment = new_value
        return self.get_monthlypayment()

    def __str__(self) -> str:
        return f'''
        Empregado: {self.get_firstname()} {self.get_lastname()}
        Pagamento Mensal: R$ {self.get_monthlypayment():.2f}
        Pagamento Anual: R$ {(self.get_monthlypayment() * 12):.2f}
        '''


def test_ex2():
    empregado_1 = Empregado('Fulano', 'de Tal', 1600.00)
    print(empregado_1)
    empregado_2 = Empregado('Beltrano', 'da Silva', -3000)
    print(empregado_2)

    old_salary = empregado_1.get_monthlypayment()
    new_value = old_salary + (old_salary * 0.1)
    empregado_1.set_monthlypayment(new_value)
    print(empregado_1)

    empregado_2.set_monthlypayment(3000)
    old_salary = empregado_2.get_monthlypayment()
    new_value = old_salary + (old_salary * 0.1)
    empregado_2.set_monthlypayment(new_value)
    print(empregado_2)


# 3) Cria uma classe chamada Complex
# para representar números complexos e escreva um programa para testá-la.
# 1. Escolha uma representação para os números complexos,
# usando a forma retangular ou a forma polar.
# 2. Forneça três construtores
# que permitam que objetos dessa classe sejam inicializados
# ao serem alocados na memória:
# • um construtor sem parâmetros que inicializa o objeto como zero
# • um construtor com um parâmetro representando a parte real;
# a parte imaginária será zero
# • um construtor com dois parâmetros
# representando as partes real e imaginária
# 3. Defina operações para obter a parte real, a parte imaginária,
# o módulo (valor absoluto) e o ângulo de um número complexo.
# 4. Forneça a operação para determinar
# o inverso aditivo de um número complexo.
# 5. Forneça as operações aritméticas básicas com números complexos:
# adição, subtração, multiplicação e divisão.
# 6. Forneça as operações relacionais
# que permitem comparar dois números complexos.
# 7. Defina a operação toString para converter
# um número complexo em string Utilize o formato (a,b),
# onde a é a parte real e b é a parte imaginária.
# 8. Escreva um aplicativo de teste
# que demonstra as capacidades da classe Complex

# from cmath import (
#     sqrt,
#     cos,
#     sin,
#     )
class Complex():
    def __init__(
        self,
        x: float = 0,
        j: float = 0,
    ):
        self._x = x
        self._j = j
        self._value = complex(x, j)

    def __str__(self) -> str:
        return f'({self._x}, {self._j})'

    def getreal(self):
        return self._x

    def getimg(self):
        return self._j

    def getmodulus(self):
        return abs(sqrt((self._x ** 2 + self._j ** 2)))
# INCOMPLETA


def test_ex3():
    print('----')
    complex_1 = Complex()
    print(complex_1)

    print('----')
    complex_2 = Complex(3)
    print(complex_2)

    print('----')
    complex_3 = Complex(3.14, 10)
    print(complex_3)
    print(complex_3.getmodulus())
    # print(complex_3.getdeg())


# 4) Crie uma classe Aluno, que possui como atributo um nome e
# cpf. Crie outra classe chamada Equipe, que possui como
# atributo uma lista de participantes do Tipo Aluno e outro
# atributo chamado projeto.
# Crie uma terceira classe chamada GerenciadorEquipes. Essa
# classe possui como atributo uma lista de todas as equipes
# formadas. Ela deverá possuir o método criarEquipe, que recebe
# uma lista de alunos de uma equipe e diz se a equipe pode ser
# formada ou não. Caso não haja nenhum aluno da equipe a ser
# formada em uma outra equipe com o mesmo projeto, então a
# equipe é criada e acrescentada à lista. Caso contrário é
# informada que a equipe não pode ser criada.

# from typing import List, Any
class Student():
    def __init__(
        self,
        name: str,
        cpf: str,
    ):
        self._name = name
        self._cpf = cpf

    def __str__(self) -> str:
        return f'***{self._cpf[3:9]}***'

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str) -> str:
        self._name = new_name
        return self.get_name()

    def get_cpf(self) -> str:
        return self._cpf

    def set_cpf(self, new_cpf: str) -> str:
        self._cpf = new_cpf
        return self.get_cpf()

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Student):
            return self.get_cpf() == other.get_cpf()
        return NotImplemented


class Team():
    def __init__(
        self,
        project: str,
        team_members: List[Student] = [],
    ):
        self._project = project
        self._team_members = team_members

    def __str__(self):
        return f'{self._project} {len(self._team_members)} members'

    def get_project(self) -> str:
        return self._project

    def set_project(self, new_project: str) -> str:
        self._project = new_project
        return self.get_project()

    def get_teammembers(self) -> List[Student]:
        return self._team_members

    def set_teammembers(
        self,
        new_list: List[Student]
            ) -> List[Student]:
        self._team_members = new_list
        return self.get_teammembers()

    def is_teammember(self, student: Student) -> bool:
        members = self.get_teammembers()
        return True if student in members else False


class TeamManager():
    def __init__(
        self,
        team_list: List[Team] = [],
    ):
        self._team_list = team_list

    def get_teamlist(self) -> List[Team]:
        return self._team_list

    def _addteam(self, new_team: Team) -> None:
        self._team_list.append(new_team)

    @staticmethod
    def valid_student(
        student: Student,
        teamlist: List[Team],
        new_project: str,
            ) -> bool:
        current_projects = []
        for team in teamlist:
            if team.is_teammember(student):
                project = team.get_project()
                current_projects.append(project)
        return False if new_project in current_projects else True

    def create_team(
        self,
        team_members: List[Student],
        project: str,
    ) -> bool:
        teams = self.get_teamlist()

        valid_label = []
        for stdt in team_members:
            valid = TeamManager.valid_student(stdt, teams, project)
            valid_label.append(valid)

        if all(valid_label):
            new_team = Team(project, team_members)
            self._addteam(new_team)
            return True
        return False


def test_ex4():
    # std1 = Student('Fulano', '12345678912')
    # print(std1)
    # same_person = Student('Fake Name', '12345678912')
    # print(std1 == same_person)  # should be True
    print('Testando Geranciador de Times')
    tm = TeamManager()
    new_members = [
        ('João Silva', '12345678901'),
        ('Maria Oliveira', '23456789012'),
        ('Carlos Pereira', '34567890123'),
        ('Ana Costa', '45678901234'),
        ('Paulo Sousa', '56789012345'),
        ('Fernanda Lima', '67890123456'),
        ('Marcos Almeida', '78901234567'),
        ('Beatriz Ribeiro', '89012345678'),
        ('Lucas Fernandes', '90123456789'),
        ('Patrícia Rocha', '01234567890'),
        ('Renato Santos', '11234567890'),
        ('Isabela Carvalho', '22345678901'),
    ]
    students = [Student(a, b) for a, b in new_members]
    projects = ['robotics', 'neural_networks', 'machine_learning', 'testing']
    seed(36)  # determining seed for reprodutibility
    for _ in range(5):
        print('\n')
        # select team meambers
        prj = choice(projects)
        team_members = sample(students, k=5)
        print('=== Criando Nova Equipe ===')
        print(prj)
        print([st.get_name() for st in team_members])
        result = tm.create_team(team_members, project=prj)
        if result is True:
            print('Equipe criada com sucesso.')
        else:
            print('Houveram conflitos na criação da Equipe.')

    print('\n')
    print('=== Verificando Times Criados ===')
    team_list = tm.get_teamlist()
    for team in team_list:
        print('\n')
        print(team)
        members = team.get_teammembers()
        for m in members:
            print(m.get_name())


# 5) Crie uma classe para representar datas.
# 1. Represente uma data usando três atributos: o dia, o mês, e o ano.
# 2. Sua classe deve ter um construtor que inicializa os três atributos
# e verifica a validade dos valores fornecidos.
# 3. Forneça um construtor sem parâmetros que inicializa a data
# com a data atual fornecida pelo sistema operacional.
# 4. Forneça um método set um get para cada atributo.
# 5. Forneça o método toString para retornar uma representação
# da ata como string. Considere que a data deve ser formatada mostrando
# o dia, o mês e o ano separados por barra (/).
# 6. Forneça uma operação para avançar uma data para o dia seguinte.
# 7. Escreva um aplicativo de teste que demonstra as capacidades da classe.
# Garanta que uma instância desta classe
# sempre esteja em um estado consistente.
class Date_v2():
    def __init__(
        self,
        day: int = None,
        month: int = None,
        year: int = None,
    ):
        LONG_MONTHS = [1, 3, 5, 7, 8, 10, 12]
        THIRTHY_MONTHS = [4, 6, 9, 11]
        today = date.today()
        if day is None:
            day = today.day
        if month is None:
            month = today.month
        if year is None:
            year = today.year

        try:
            if not isinstance(day, int):
                raise ValueError
            if not isinstance(month, int):
                raise ValueError
            if not isinstance(year, int):
                raise ValueError

            self._year = year
            if month > 12:
                raise ValueError
            self._month = month

            if month in LONG_MONTHS and day > 31:
                raise ValueError
            if month == 2 and day > 29:
                raise ValueError
            if month in THIRTHY_MONTHS and day > 30:
                raise ValueError
            self._day = day
        except ValueError as err:
            print(err, "Argumentos inválidos para data.")

    def __str__(self):
        return f'{self._day}/{self._month}/{self._year}'

    @staticmethod
    def _getreftable() -> dict:
        reftable = {
            1: (31, 'Janeiro'),
            2: (29, 'Fevereiro'),
            3: (31, 'Março'),
            4: (30, 'Abril'),
            5: (31, 'Maio'),
            6: (30, 'Junho'),
            7: (31, 'Julho'),
            8: (31, 'Agosto'),
            9: (30, 'Setembro'),
            10: (31, 'Outubro'),
            11: (30, 'Novembro'),
            12: (31, 'Dezembro')
        }
        return reftable

    @staticmethod
    def get_maxday(month: int) -> int:
        reftable = Date_v2._getreftable()
        maxday = reftable[month][0]
        return maxday

    @staticmethod
    def getmonthname(month: int) -> str:
        reftable = Date_v2._getreftable()
        monthname = reftable[month][1]
        return monthname

    def nextyear(self):
        self._day = 1
        self._month = 1
        self._year += 1

    def nextmonth(self):
        if self._month == 12:
            self.nextyear()
        else:
            self._month += 1
            self._day = 1

    def nextday(self):
        day = self._day
        month = self._month
        if month == 12 and day == 31:
            return self.nextyear()
        if day == Date_v2.get_maxday(month):
            return self.nextmonth()
        self._day += 1


def test_ex5():
    today = Date_v2()
    print(today)
    other_date = Date_v2(15, 4, 2023)
    print(other_date)
    # invalid_date_1 = Date_v2(40, 4, 2023)
    # invalid_date_2 = Date_v2(25, 15, 2000)
    # invalid_date_3 = Date_v2(30, 2, 2001)
    # invalid_date_4 = Date_v2(14, 'fevereiro', 1999)
    today.nextday()
    print(today)
    yeareve = Date_v2(31, 12, 2023)
    print(yeareve)
    yeareve.nextday()
    print(yeareve)


# 6) Escreva um programa completo para jogar o jogo da velha.
# Para tanto crie uma classe JogoDaVelha:
# • a classe deve conter como dados privados
# um array bidimensional 3x3 para representar a grade do jogo
# • crie uma enumeração para representar
# as possibilidades de ocupação de uma casa na grade
# (vazia, jogador 1 ou jogador 2)
# • o construtor deve inicializar a grade como vazia
# • forneça um método para exibir a grade
# • permita dois jogadores humanos
# • forneça um método para jogar o jogo;
# todo movimento deve ocorrer em uma casa vazia;
# depois de cada movimento,
# determine se houve uma derrota ou um empate.
class HashGame():
    @property
    def boardmap(self):
        return {
            1: (2, 0),
            2: (2, 1),
            3: (2, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (0, 0),
            8: (0, 1),
            9: (0, 2),
        }

    @property
    def winning_combinations(self):
        return [
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)],  # diagonals
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],  # columns
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],  # rows
        ]

    @property
    def sampleboard(self):
        return [
            [7, 8, 9],
            [4, 5, 6],
            [1, 2, 3],
        ]

    @property
    def initialboard(self):
        return [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def __init__(
            self,
            player1_mark: str,
            player2_mark: str,
    ):
        self._p1m = player1_mark
        self._p2m = player2_mark
        self.movesp1 = []
        self.movesp2 = []
        self.board = self.initialboard
        self.count = 1
        self.player = 1

    @staticmethod
    def printboard(boardstate: list) -> None:
        print(' {} | {} | {} '.format(*boardstate[0]))
        print('---+---+---')
        print(' {} | {} | {} '.format(*boardstate[1]))
        print('---+---+---')
        print(' {} | {} | {} '.format(*boardstate[2]))

    def nextplayer(self):
        self.count += 1
        self.player = 2 if self.player == 1 else 1

    def registerplay(self, move):
        if self.player == 1:
            self.movesp1.append(move)
        if self.player == 2:
            self.movesp2.append(move)

    def setboard(self, newboard):
        self.board = newboard
        self.nextplayer()

    def getplay(self):
        playermark = self._p1m if self.player == 1 else self._p2m
        newboard = self.board
        try:
            play = int(input('Digite a coordenada da sua jogada: '))
            i, j = self.boardmap[play]
            if self.board[i][j] != ' ':
                raise AssertionError
            newboard[i][j] = playermark
            return (True, newboard, (i, j))
        except (ValueError, AssertionError):
            print('Jogada inválida.')
            return (False, self.board, (-1, -1))

    def assert_endgame(self):
        if self.count == 10:
            return (True, None)
        p1_moveset = set(self.movesp1)
        p2_moveset = set(self.movesp2)

        for win_c in self.winning_combinations:
            set_win_c = set(win_c)
            if set_win_c.issubset(p1_moveset):
                return (True, 1)
            if set_win_c.issubset(p2_moveset):
                return (True, 2)

        return (False, None)

    def play(self):
        print('Jogo da Velha!')
        print('As coordenadas do jogo são:\n')
        self.printboard(self.sampleboard)
        print('\n')

        stop = False
        while stop is False:
            print('=======')
            print(f'Rodada: {self.count}')
            self.printboard(self.board)
            stop, winner = self.assert_endgame()

            if stop is False:
                print(f'Sua vez, Jogador {self.player}')
                valid, newboard, move = self.getplay()
                if valid:
                    self.registerplay(move)
                    self.setboard(newboard)

            if stop is True:
                if winner is None:
                    print('Deu velha! Tentem novamente!')
                else:
                    print(f'Parabéns, Jogador {winner}. Você venceu!')


def test_ex6():
    hashgame = HashGame('X', 'O')
    hashgame.play()


if __name__ == "__main__":
    # # Ex1
    # print('Exercício 1 - Invoice')
    # test_invoice()

    # # Ex2
    # print('Exercício 2 - Empregado')
    # test_ex2()

    # # Ex3 - INCOMPLETO
    # print('Exercício 3 - Números Complexos')
    # test_ex3()

    # # Ex4
    # print('Exercício 4 - Gerenciador de Times')
    # test_ex4()

    # # Ex5
    # print('Exercício 5 - Data v2')
    # test_ex5()

    # Ex6
    print('Exercício 6 - Jogo da Velha')
    test_ex6()
