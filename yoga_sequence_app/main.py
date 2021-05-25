from kivy.lang import Builder
from kivy.resources import resource_add_path, resource_find
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
from libs.yoga_sequence_builder import YogaSequenceBuilder
from pathlib import Path
import importlib.util
import os, sys

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["YOGA_SEQUENCE_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("yoga_sequence_app")[0])
    os.environ["YOGA_SEQUENCE_ROOT"] = str(Path(__file__).parent)
    # os.environ["KITCHEN_SINK_ROOT"] = os.path.dirname(os.path.abspath(__file__))
os.environ["YOGA_SEQUENCE_ASSETS"] = os.path.join(
    os.environ["YOGA_SEQUENCE_ROOT"], f"assets{os.sep}"
)

class Main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.screen = Builder.load_file( os.path.join(__location__, 'libs/kv/layout.kv'))

    def build(self):
        # __location__ = os.path.realpath(
        #     os.path.join(os.getcwd(), os.path.dirname(__file__)))
        # spec = importlib.util.spec_from_file_location('yoga_sequence_builder', os.path.join(__location__, 'libs/yoga_sequence_builder.py'))
        # yoga = importlib.util.module_from_spec(spec)
        # spec.loader.exec_module(yoga)
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