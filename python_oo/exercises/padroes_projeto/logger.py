from __future__ import annotations


class Logger:

    __instance = None

    def __new__(cls, *args, **kwargs) -> Logger:
        if not cls.__instance:
            cls.__instance = super(Logger, cls).__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        if not hasattr(self, 'initialized'):
            self.initialized = True

    def log(self, message: str):
        print(f'LOG: {message}')


if __name__ == '__main__':
    logger1 = Logger()
    logger1.log('Logger1 - Primeiro Log')
    logger2 = Logger()
    logger2.log('Logger2 - Segundo Log')
    print(logger1 is logger2)
