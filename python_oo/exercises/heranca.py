class A:
    def __init__(self) -> None:
        self.visivel = 'Informação Visível'
        self.__invisivel = 'Informação Privada'

    def __str__(self) -> str:
        return 'A'

    def print_invisivel(self):
        return self.__invisivel


class B(A):
    def __str__(self) -> str:
        return super().__str__() + 'B'

    def print_invisivel(self):
        return super().print_invisivel() + ' dentro de B'


class C(B):
    def __str__(self) -> str:
        return super().__str__() + 'C'


class D(C):
    def __str__(self) -> str:
        return super().__str__() + 'D'


class E(D):
    def __str__(self) -> str:
        return super().__str__() + 'E'


if __name__ == '__main__':
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    print(str(a) + ' | ' + str(type(a)) + ' | ' + str(isinstance(a, A))+ ' | ' + a.visivel + ' | ' + a.print_invisivel())
    print(str(b) + ' | ' + str(type(b)) + ' | ' + str(isinstance(b, A))+ ' | ' + b.visivel + ' | ' + b.print_invisivel())
    print(str(c) + ' | ' + str(type(c)) + ' | ' + str(isinstance(c, A))+ ' | ' + c.visivel + ' | ' + c.print_invisivel())
    print(str(d) + ' | ' + str(type(d)) + ' | ' + str(isinstance(d, A))+ ' | ' + d.visivel + ' | ' + d.print_invisivel())
    print(str(e) + ' | ' + str(type(e)) + ' | ' + str(isinstance(e, A))+ ' | ' + e.visivel + ' | ' + e.print_invisivel())
