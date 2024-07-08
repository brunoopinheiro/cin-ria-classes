from abc import ABC, abstractmethod
from enum import Enum


class Button(ABC):
    @abstractmethod
    def render(self):
        raise NotImplementedError


class TextButton(Button):

    def __init__(self, text: str) -> None:
        self.text = text

    def render(self):
        return f'Renderizando botão textual: {self.text}'


class ImageButton(Button):

    def __init__(self, imgsrc: str) -> None:
        self.imgsrc = imgsrc

    def render(self):
        return f'Renderizando botão de imagem: {self.imgsrc}'


class ButtonTypes(Enum):
    Text = 1
    Image = 2


class ButtonFactory:

    @staticmethod
    def create_button(t_button: ButtonTypes, *args, **kwargs) -> Button:
        if t_button == ButtonTypes.Image:
            return ImageButton(*args, **kwargs)
        elif t_button == ButtonTypes.Text:
            return TextButton(*args, **kwargs)
        else:
            raise TypeError('Unknown button type')


if __name__ == '__main__':
    print('Factory Implementation')

    b = ButtonFactory.create_button(ButtonTypes.Text, text='Meu Botão Maneiro')
    print(b.render())
    b2 = ButtonFactory.create_button(ButtonTypes.Image, 'imgsrc/img.png')
    print(b2.render())
