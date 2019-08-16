from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class FrontPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Name :"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Age :"))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)

        self.add_widget(Label(text="Sex :"))
        self.sex = TextInput(multiline=False)
        self.add_widget(self.sex)


class HelloWorld(App):
    def build(self):
        return FrontPage()


if __name__ == "__main__":
    HelloWorld().run()
