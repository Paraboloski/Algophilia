import flet as ft
from Frontend.src.views import DiceRoller

class App:
    def __init__(self, page: ft.Page):
        self.page = page

    def setup(self):
        self.page.title = "Algophilia"
        self.page.bgcolor = "#181818"
        self.page.padding = 0
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.fonts = {"Cinzel": "fonts/Cinzel-Regular.ttf"}
        self.page.theme = ft.Theme(font_family="Cinzel")

    def build(self): self.page.add(DiceRoller())

    def run(self):
        self.setup()
        self.build()
        self.page.update()