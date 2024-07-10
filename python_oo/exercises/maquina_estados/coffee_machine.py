from transitions import Machine
from enum import Enum
from time import sleep


class States(Enum):
    IDLE = 'idle'
    SELECTING = 'selecting'
    PAYING = 'paying'
    BREWING = 'brewing'
    DISPENSING = 'dispensing'
    OUT_OF_ORDER = 'out of order'


class CoffeMachine:

    @property
    def __menu_options(self) -> dict[int, str]:
        return {
            1: 'Select Coffee',
            0: 'Exit',
        }

    def __init__(self) -> None:
        self.coffee = None
        transitions = [
            {
                'trigger': 'start',
                'source': States.IDLE,
                'dest': States.SELECTING,
            },
            {
                'trigger': 'select_coffee',
                'source': States.SELECTING,
                'dest': States.PAYING,
            },
            {
                'trigger': 'pay',
                'source': States.PAYING,
                'dest': States.BREWING,
                'after': self.on_enter_brewing,
            },
            {
                'trigger': 'brew_complete',
                'source': States.BREWING,
                'dest': States.DISPENSING,
                'after': self.on_enter_dispensing,
            },
            {
                'trigger': 'dispense_complete',
                'source': States.DISPENSING,
                'dest': States.IDLE,
            },
            {
                'trigger': 'error',
                'source': '*',
                'dest': States.OUT_OF_ORDER,
                'after': self.on_enter_out_of_order,
            },
            {
                'trigger': 'reset',
                'source': States.OUT_OF_ORDER,
                'dest': States.IDLE,
            },
        ]
        self._machine = Machine(
            model=self,
            states=States,
            initial=States.IDLE,
            transitions=transitions,
        )

    def on_enter_brewing(self) -> None:
        # inicia a preparacao de cafe
        print(f'Preparando um café brabo: {self.coffee}')
        print('Segura aí um pouco...')
        sleep(3)
        self.brew_complete()

    def on_enter_dispensing(self) -> None:
        # dispensa o cafe
        print(f'Café {self.coffee} na caneca.')
        sleep(2)
        self.dispense_complete()

    def __menu_display(self, options_dict: dict[int, str]) -> None:
        menuopts = ''
        for key, value in options_dict.items():
            menuopts = menuopts + f'[{key}] - {value}\n'
        print(menuopts)

    def __get_option(self, options_dict: dict[int, str]) -> int:
        self.__menu_display(options_dict)
        option = None
        while option not in options_dict.keys():
            try:
                option = int(input('>> '))
            except TypeError:
                print('Invalid Option')
        return option

    def __select_coffee(self):
        self.select_coffee()
        coffee_options = {
            10: 'Robusta Brasileiro',
            11: 'Arábica Brasileiro',
            12: 'Arábica Colombiano',
            13: 'Arábica Taiwan',
            14: 'Blend Brasil',
            15: 'Melitão das Massas',
            16: 'Nescalixo',
        }
        opt = self.__get_option(coffee_options)
        return coffee_options[opt]

    def on_enter_out_of_order(self) -> None:
        # trata a condicao de erro
        self.reset()
        self.start()
        coffee = self.__select_coffee()
        if coffee == 'Nescalixo':
            self.on_enter_out_of_order()
        self.coffee = coffee

    def main(self) -> None:
        menuexit = False
        while menuexit is False:
            print('== Coffee Machine ==')
            self.start()
            option = self.__get_option(self.__menu_options)
            if option == 0:
                menuexit = True
            if option == 1:
                coffee = self.__select_coffee()
                if coffee == 'Nescalixo':
                    print('A gente não serve esse negócio podre aqui.')
                    self.error()
                if coffee == 'Melitão das Massas':
                    print(' '*16, 'Humilde Demais!')
                self.coffee = coffee
                print('Por hora tá de graça!')
                self.pay()

    def __str__(self) -> str:
        return f'CoffeeMachine: (state: {self.state}, coffee: {self.coffee})'


if __name__ == "__main__":
    cm = CoffeMachine()
    print(cm)
    cm.main()
    print(cm)
