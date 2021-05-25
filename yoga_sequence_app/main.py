from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem

import importlib

class Main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('layout.kv')

    def build(self):
        yoga = importlib.import_module('yoga_sequence_builder')
        self.yoga = yoga.YogaSequenceBuilder()
        self.build_asanas()     
        return self.screen

    def build_asanas(self):
        for asana in self.yoga.get_sequence(60):
            self.screen.ids.box_sixty_minute_sequence.add_widget(
                TwoLineListItem(
                    text= f"{asana[0]}",
                    secondary_text= f"{asana[1]}"
                )
            )
        for asana in self.yoga.get_sequence(90):
            self.screen.ids.box_ninety_minute_sequence.add_widget(
                TwoLineListItem(
                    text= f"{asana[0]}",
                    secondary_text= f"{asana[1]}"
                )
            )

    def callback_refresh_asanas(self):
        self.screen.ids.box_sixty_minute_sequence.clear_widgets()
        self.screen.ids.box_ninety_minute_sequence.clear_widgets()
        self.build_asanas()

Main().run()