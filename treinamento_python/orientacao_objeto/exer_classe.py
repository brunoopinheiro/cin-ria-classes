# Atividades de OO
# """
# 1)
# Crie uma classe Pessoa que tenha os atributos nome, idade e sexo. Adicione um método que imprima os dados da pessoa.
# """
class Pessoa():
    def __init__(self, name, age, sex):
        self._name = name
        self._age = age
        self._sex = sex


    def get_info(self) -> str:
        return f'''
        Nome: {self._name}
        Idade: {self._age}
        Sexo: {self._sex}
        '''


# # Teste
# # p1 = Pessoa("Alice", 30, "Feminino")
# # p1.cumprimentar()
# # Saída: nome: Alice, idade: 30, sexo: Feminino
def test_ex_1():
    print('Exercício 1 - Classe Pessoa')
    p1 = Pessoa('Alice', 30, 'Feminino')
    info = p1.get_info()
    print(info)

# """
# 2)
# Crie uma classe Retângulo que tenha os atributos largura e altura. Adicione métodos para calcular a área e o perímetro 
# do retângulo.
# """
class Retangulo():
    def __init__(
        self,
        width: float,
        height: float,
    ):
        self._width = width
        self._height = height


    def get_width(self) -> float:
        return self._width


    def get_height(self) -> float:
        return self._height


    def calc_perimeter(self) -> float:
        return (self._height + self._width) * 2


    def calc_area(self) -> float:
        return self._height * self._width


# # Teste
# # r = Retangulo(5, 10)
# # print(r.area())
# # Saída: 50
# # print(r.perimetro())
# # Saída: 30
def test_ex_2():
    print('Exercício 2 - Classe Retângulo')
    r = Retangulo(5, 10)
    print(r.calc_area())
    print(r.calc_perimeter())


# """
# 3)
# Crie uma classe ContaBancaria que tenha os atributos nome_cliente e saldo. Adicione métodos para depositar (depositar) 
# e sacar (sacar) dinheiro, garantindo que não seja possível sacar mais do que o saldo disponível.
# """
class BankAccount():
    def __init__(
        self,
        client_name: str,
        acc_balance: float,
    ):
        self._cliente_name = client_name
        self._acc_balance = acc_balance


    def get_balance(self) -> float:
        return self._acc_balance


    def update_balance(self, amount: float, operation: int = 1) -> float:
        if operation == 1:
            self._acc_balance += amount

        if operation == 2:
            self._acc_balance -= amount
        return self.get_balance()


    def get_clientname(self) -> str:
        return self._cliente_name


    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            return False
        self.update_balance(amount, 1)
        return True


    def withdraw(self, amount: float) -> str:
        try:
            if amount <= 0:
                raise ArithmeticError('Não é possível sacar um valor negativo.')

            if amount > self.get_balance():
                raise ArithmeticError('Não é possível sacar um valor maior que seu saldo.')

            new_value = self.update_balance(amount, 2)
            return f'Olá, {self.get_clientname()}. Novo Saldo: {self.get_balance()}'
        except ArithmeticError as a_err:
            return f'Olá, {self.get_clientname()}. {a_err}'

# # Teste
# # conta = ContaBancaria('José', 100)
# # conta.depositar(50)
# # print(conta.saldo)
# # Saída: 150
# # conta.sacar(30)
# # print(conta.saldo)
# # Saída: 120
# # conta.sacar(200)
# # print(conta.saldo)
# # Saída: Olá José. Não é possível sacar, pois seu saldo é de {saldo(variavel saldo)}
def test_ex_3():
    print('Exercício 3 - Classe Conta Bancária')
    conta = BankAccount('José', 100)
    print('Conta criada para José com valor inicial R$ 100,00')
    print('Depositando R$ 50,00')
    conta.deposit(50)
    print(f'Valor atual: {conta.get_balance()}')
    print('Sacando R$ 30,00')
    conta.withdraw(30)
    print(f'Valor atual: {conta.get_balance()}')
    print(conta.withdraw(200))
    print(conta.withdraw(-200))
    print(conta.withdraw(20))



# """
# 4)
# Crie uma classe Aluno com os atributos nome e notas (uma lista de notas). Crie uma classe Turma que tenha uma lista de 
# alunos. Adicione métodos na classe Turma para calcular a média das notas de todos os alunos.
# """
from typing import List
class Student():
    def __init__(self, name: str, scores: List[int]):
        self._name = name
        self._scores = scores


    def add_score(self, score: int):
        if score >= 0 or score <= 10:
            self._scores.append(score)


    def get_scores(self):
        return self._scores

    
    def mean_scores(self):
        scores = self.get_scores()
        return sum(scores) / len(scores)


class CourseDiscipline():
    def __init__(self, name: str, students: List[Student]):
        self._name = name
        self._students = students


    def get_name(self) -> str:
        return self._name


    def get_students(self) -> List[Student]:
        return self._students


    def get_discipline_mean(self):
        students = self.get_students()
        means = [stdt.mean_scores() for stdt in students]
        return sum(means)/ len(means)


# # Teste
# # a1 = Aluno('Alice', [8, 7, 6])
# # a2 = Aluno('Bob', [9, 8, 7])
# # turma = Turma([a1, a2])
# # print(turma.media())
# # Saída: 7.5
def test_ex_4():
    print('Exercício 4 - Classes Aluno e Turma')
    a1 = Student('Alice', [8, 7, 6])
    a2 = Student('Bob', [9, 8, 7])
    turma = CourseDiscipline('Python Básico', [a1, a2])
    print(turma.get_discipline_mean())


# """
# 5)
# Crie uma classe base Veiculo com os atributos marca e modelo. Adicione um método informações que imprime as informações 
# do veículo. Crie subclasses Carro e Moto que herdam de Veiculo e adicionam um atributo específico (por exemplo, 
# numero_portas para Carro e cilindradas para Moto).
# """
class Vehicle():
    def __init__(
        self,
        brand: str,
        model: str,
    ):
        self._brand = brand
        self._model = model

    
    def __str__(self):
        return f'''
        Marca: {self._brand}
        Modelo: {self._model}
        '''


    def get_info(self):
        print(self.__str__())


class Car(Vehicle):
    def __init__(
        self,
        brand: str,
        model: str,
        n_doors: int,
    ):
        super().__init__(
            brand=brand,
            model=model,
        )
        self._n_doors = n_doors


    def __str__(self):
        return f'''
        Marca: {self._brand}
        Modelo: {self._model}
        N° de Portas: {self._n_doors}
        '''


class Motorcycle(Vehicle):
    def __init__(
        self,
        brand: str,
        model: str,
        cylinder_capacity: int,
    ):
        super().__init__(
            brand=brand,
            model=model,
        )
        self._cylinder_capacity = cylinder_capacity


    def __str__(self):
        return f'''
        Marca: {self._brand}
        Modelo: {self._model}
        Cilindradas: {self._cylinder_capacity} cc
        '''


# # Teste
# # c = Carro('Fiat', 'Uno', 4)
# # c.informacoes()
# # Saída: Fiat Uno, 4 portas
# # m = Moto('Honda', 'Biz', 125)
# # m.informacoes()
# # Saída: Honda Biz, 125 cilindradas
def test_ex_5():
    print('Exercício 5 - Veículo | Carro | Moto')
    c = Car('Fiat', 'Uno', 4)
    c.get_info()
    m = Motorcycle('Honda', 'Biz', 125)
    m.get_info()


# """
# 6)
# Crie uma classe Animal com os atributos nome e especie e adicione um método que imprime os dados do animal. Crie uma
# subclasse Mamifero que herda de Animal e adiciona um atributo cor_pelo. Crie uma subclasse Reptil que herda de Animal e
# adiciona um atributo tipo_escama.
# """
class Animal():
    def __init__(
        self,
        name: str,
        species: str,
    ):
        self._name = name
        self._species = species


    def get_info(self) -> dict:
        return {
            'Nome': self._name,
            'Espécie': self._species,
        }


    def __str__(self):
        infos = self.get_info()
        return infos.__repr__()


    def print_info(self):
        print(self.__str__()[1:-1]) # cut the {} at beginning and end


class Mammal(Animal):
    def __init__(
        self,
        name: str,
        species: str,
        fur_color: str,
    ):
        super().__init__(
            name=name,
            species=species,
        )
        self._fur_color = fur_color


    def get_info(self) -> dict:
        infos = super().get_info()
        infos['Cor do Pelo'] = self._fur_color
        return infos


class Reptil(Animal):
    def __init__(
        self,
        name: str,
        species: str,
        scale_type: str,
    ):
        super().__init__(
            name=name,
            species=species,
        )
        self._scale_type = scale_type


    def get_info(self) -> dict:
        infos = super().get_info()
        infos['Tipo de Escama'] = self._scale_type
        return infos


# # Teste
# # a = Animal('Rex', 'Cachorro')
# # a.informacoes()
# # Saída: Nome: Rex, Espécie: Cachorro
# # m = Mamifero('Rex', 'Cachorro', 'Marrom')
# # m.informacoes()
# # Saída: Nome: Rex, Espécie: Cachorro, Cor do pelo: Marrom
# # r = Reptil('Snake', 'Cobra', 'Lisas')
# # r.informacoes()
# # Saída: Nome: Snake, Espécie: Cobra, Tipo de escama: Lisas
def test_ex_6():
    print('Exercício 6 - Animal | Mamífero | Reptil')
    a = Animal('Rex', 'Cachorro')
    a.print_info()
    m = Mammal(
        'Rex',
        'Cachorro',
        'Marrom',
    )
    m.print_info()
    r = Reptil('Snake', 'Cobra', 'Lisas')
    r.print_info()


# """
# 7)
# Crie uma classe base Funcionario com os atributos nome e salario. Adicione um método aumentar_salario que aumenta o
# salário em 10%. Crie subclasses Programador e Analista que herdam de Funcionario e sobrescrevem o método 
# aumentar_salario para aumentar o salário em 20% e 30%, respectivamente.
# """
class Employee():
    def __init__(
        self,
        name: str,
        salary: float,
    ):
        self._name = name
        self._salary = salary


    @staticmethod
    def _get_raise_rate() -> float:
        return 0.1


    def get_salary(self) -> float:
        return self._salary


    def set_salary(self, new_value: float) -> float:
        self._salary = new_value


    def raise_salary(self) -> float:
        old_salary = self.get_salary()
        raise_rate = self._get_raise_rate()
        self.set_salary(old_salary + (old_salary * raise_rate))
        return self.get_salary()


class Developer(Employee):
    @staticmethod
    def _get_raise_rate() -> float:
        return 0.2
    


class Analist(Employee):
    @staticmethod
    def _get_raise_rate() -> float:
        return 0.3
# # Teste
# # p = Programador('Alice', 5000)
# # p.aumentar_salario()
# # print(p.salario)
# # Saída: 6000
# # a = Analista('Bob', 5000)
# # a.aumentar_salario()
# # print(a.salario)
# # Saída: 6500
# # f = Funcionario('Carlos', 5000)
# # f.aumentar_salario()
# # print(f.salario)
# # Saída: 5500
def test_ex_7():
    print('Exercício 7: Funcionário | Programador | Analista')
    p = Developer('Alice', 5_000)
    p.raise_salary()
    print(p.get_salary())
    a = Analist('Bob', 5_000)
    a.raise_salary()
    print(a.get_salary())
    f = Employee('Carlos', 5_000)
    f.raise_salary()
    print(f.get_salary())

# """
# 8)
# Crie uma classe base FormaGeometrica com os atributos base e altura. Adicione um método calcular_area que retorna a área
# da forma geométrica. Crie subclasses Retangulo e Triangulo que herdam de FormaGeometrica e sobrescrevem o método
# calcular_area para retornar a área correta.
# """
class GeometricForm():
    def __init__(
        self,
        base,
        height,
    ):
        self._base = base
        self._height = height


    def calc_area(self) -> float:
        raise NotImplementedError


class Rectangle(GeometricForm):
    def calc_area(self) -> float:
        return self._base * self._height


class Triangle(GeometricForm):
    def calc_area(self) -> float:
        return (self._base * self._height)/2


# # Teste
# # r = Retangulo(5, 10)
# # print(r.calcular_area())
# # Saída: 50
# # t = Triangulo(5, 10)
# # print(t.calcular_area())
# # Saída: 25
def test_ex_8():
    print('Exercício 8 - Forma Geométrica | Retângulo | Triângulo')
    r = Rectangle(5, 10)
    print(r.calc_area())
    t = Triangle(5, 10)
    print(t.calc_area())


# """
# 9)
# Crie uma classe base Figura com os atributos cor e preenchida. Adicione um método informacoes que imprime as informações
# da figura. Crie subclasses Circulo e Quadrado que herdam de Figura e adicionam um atributo específico (por exemplo,
# raio para Circulo e lado para Quadrado).
# """
class Figure():
    def __init__(
        self,
        color: str,
        filled: bool,
    ):
        self._color = color
        self._filled = filled


    def get_info(self) -> dict:
        return {
            'Cor': self._color,
            'Preenchida': self._filled,
        }


    def __str__(self):
        infos = self.get_info()
        return infos.__repr__()


    def print_info(self):
        print(self.__str__()[1:-1])


class Circle(Figure):
    def __init__(
        self,
        color: str,
        filled: bool,
        radius: float,
    ):
        super().__init__(
            color=color,
            filled=filled,
        )
        self._radius = radius


    def get_info(self) -> dict:
        infos = super().get_info()
        infos['Raio'] = self._radius
        return infos


class Square(Figure):
    def __init__(
        self,
        color: str,
        filled: bool,
        size: float,
    ):
        super().__init__(
            color=color,
            filled=filled,
        )
        self._size = size


    def get_info(self) -> dict:
        infos = super().get_info()
        infos['Lado'] = self._size
        return infos


# # Teste
# # c = Circulo('Azul', True, 5)
# # c.informacoes()
# # Saída: Cor: Azul, Preenchida: True, Raio: 5
# # q = Quadrado('Vermelho', False, 10)
# # q.informacoes()
# # Saída: Cor: Vermelho, Preenchida: False, Lado: 10
def test_ex_9():
    print('Exercício 9 - Figura | Círculo | Quadrado')
    c = Circle('Azul', True, 5)
    c.print_info()
    q = Square('Vermelho', False, 10)
    q.print_info()


# """
# 10)
# Crie uma classe base Cliente com os atributos nome e idade. Adicione um método informacoes que imprime os dados do
# cliente. Crie subclasses ClientePessoaFisica e ClientePessoaJuridica que herdam de Cliente e adicionam um atributo
# específico (por exemplo, cpf para ClientePessoaFisica e cnpj para ClientePessoaJuridica).
# """
class Client():
    def __init__(
        self,
        name: str,
        age: int,
    ):
        self._name = name
        self._age = age


    def get_info(self) -> dict:
        return {
            'Nome': self._name,
            'Idade': self._age,
        }


    def __str__(self):
        infos = self.get_info()
        return infos.__repr__()


    def print_info(self):
        print(self.__str__()[1:-1]) # cut the {} at beginning and end


class ClientePessoaFisica(Client):
    def __init__(
        self,
        name: str,
        age: int,
        cpf: str,
    ):
        super().__init__(
            name=name,
            age=age,
        )
        self._cpf = cpf


    def get_info(self) -> dict:
        info = super().get_info()
        info['CPF'] = self._cpf
        return info


class ClientePessoaJuridica(Client):
    def __init__(
        self,
        name: str,
        age: int,
        cnpj: str,
    ):
        super().__init__(
            name=name,
            age=age,
        )
        self._cnpj = cnpj


    def get_info(self) -> dict:
        info = super().get_info()
        info['CNPJ'] = self._cnpj
        return info
# # Teste
# # pf = Cliente
# # pf.informacoes()
# # Saída: Nome: Alice, Idade: 30, CPF: 123.456.789-00
# # pj = ClientePessoaJuridica('Empresa', 10, '123.456.789/0001-00')
# # pj.informacoes()
# # Saída: Nome: Empresa, Idade: 10, CNPJ: 123.456.789/0001-00
# # cf = ClientePessoaFisica('Alice', 30, '123.456.789-00')
# # cf.informacoes()
# # Saída: Nome: Alice, Idade: 30, CPF: 123.456.789-00
def test_ex_10():
    print('Exercício 10 - Cliente | Pessoa Física | Pessoa Jurídica')
    pj = ClientePessoaJuridica('Empresa', 10, '123.456.789/0001-00')
    pj.print_info()
    cf = ClientePessoaFisica('Alice', 30, '123.456.789-00')
    cf.print_info()


if __name__ == "__main__":
    print('=== Resolução Exercícios: Classes ===')
    print('\n')
    test_ex_1()
    print('\n')
    test_ex_2()
    print('\n')
    test_ex_3()
    print('\n')
    test_ex_4()
    print('\n')
    test_ex_5()
    print('\n')
    test_ex_6()
    print('\n')
    test_ex_7()
    print('\n')
    test_ex_8()
    print('\n')
    test_ex_9()
    print('\n')
    test_ex_10()