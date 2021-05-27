import os

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
from libs.yoga_sequence_builder import YogaSequenceBuilder

os.environ["YOGA_SEQUENCE_ROOT"] = os.path.dirname(os.path.abspath(__file__))
os.environ["YOGA_SEQUENCE_LIBS"] = os.path.join(
    os.environ["YOGA_SEQUENCE_ROOT"], f"libs{os.sep}"
)
os.environ["YOGA_SEQUENCE_ASSETS"] = os.path.join(
    os.environ["YOGA_SEQUENCE_ROOT"], f"assets{os.sep}"
)

class Main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.screen = Builder.load_file( os.path.join(os.environ["YOGA_SEQUENCE_ROOT"], "libs", "kv", "layout.kv"))

    def build(self):
        self.yoga = YogaSequenceBuilder()
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