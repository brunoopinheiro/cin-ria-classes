class Pessoa(object):
    def __init__(self, n='sem nome', a = 0):
        self.nome = n
        self.idade = a
    
    def aniversario(self):
        self.idade = self.idade + 1
        
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos'


class Estudante(Pessoa):
    def __init__(self, nome = 'sem nome', idade = 0, disciplinas = [], orientador = None):
        super().__init__(nome,idade)
        self.disciplinasCursadas = disciplinas
        self.orientador = orientador

    def __str__(self):
        return f'Estudante {super().__str__()}, cursou as disciplinas {self.disciplinasCursadas} e tem como orientador(a) {self.orientador}'


class Professor(Pessoa):
    def __init__(self, nome = 'sem nome', idade = 0, disciplinas = [], orientandos = []):
        super().__init__(nome,idade)
        self.disciplinasMinistradas = disciplinas
        self.orientandos = orientandos

    def __str__(self):
        return f'Professor {super().__str__()}, ministrou as disciplinas {self.disciplinasMinistradas} e (des)orienta {self.orientador}'


class Monitor(Professor, Estudante):
    def __init__(
            self,
            nome='sem nome',
            idade=0,
            disciplinas=[],
            orientador=None,
            orientandos=[],
            ):
        Professor.__init__(self, nome, idade, disciplinas, orientandos)
        Estudante.__init__(self, nome, idade, disciplinas, orientador)
        self.particularidadeX = 'Coisa nova'


if __name__ == '__main__':
    x = Monitor(
        disciplinas=['Python', 'Android']
    )
    print(x)
    print(Monitor.mro())
    print(x.particularidadeX)
