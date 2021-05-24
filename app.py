from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

import yoga_sequence_builder

class Main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('layout.kv')

    def build(self):
        for asana in yoga_sequence_builder.get_sequence(60):
            self.screen.ids.box_sixty_minute_sequence.add_widget(
                MDLabel(
                    text= f"{asana}",
                    halign="center",
                )
            )
        self.screen.ids.text_field_ninety_minute_sequence.text = '\n'.join(yoga_sequence_builder.get_sequence(90))
        return self.screen

Main().run()