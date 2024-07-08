class Singleton:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            print('Singleton._instance = None')
            cls.__instance = super(Singleton, cls).__new__(cls)
        else:
            print('Singleton agora tem instância')
        return cls.__instance

    def __init__(self, v1=1, v2=2, v3=3, vn='n') -> None:
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.v1 = v1
            self.v2 = v2
            self.v3 = v3
            self.vn = vn


if __name__ == '__main__':
    s2 = Singleton(2, 3, 4, 'm')
    s1 = Singleton()
    print(s1.vn)
    print(s2.vn)
    print(s1 is s2)
