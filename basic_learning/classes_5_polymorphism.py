from abc import ABC, abstractmethod


# good practice but not needed because of duck typing
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print('TextBox')


class DropDownList(UIControl):
    def draw(self):
        print('DropDownList')


def draw(controls):
    for control in controls:
        # here as long as control has a method called draw it works
        control.draw()


ddl = DropDownList()
tb = TextBox()
draw([tb, ddl, tb])
