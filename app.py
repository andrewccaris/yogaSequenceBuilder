from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem

from yoga_sequence_builder import YogaSequenceBuilder

#TODO: Add button to regenerate sequences
class Main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('layout.kv')

    def build(self):
        yoga = YogaSequenceBuilder()
        for asana in yoga.get_sequence(60):
            self.screen.ids.box_sixty_minute_sequence.add_widget(
                TwoLineListItem(
                    text= f"{asana[0]}",
                    secondary_text= f"{asana[1]}"
                )
            )
        for asana in yoga.get_sequence(90):
            self.screen.ids.box_ninety_minute_sequence.add_widget(
                TwoLineListItem(
                    text= f"{asana[0]}",
                    secondary_text= f"{asana[1]}"
                )
            )     
        return self.screen

Main().run()