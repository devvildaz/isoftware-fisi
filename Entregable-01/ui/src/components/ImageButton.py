from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.config import Config
Config.set('graphics', 'resizable', True)
import os

Builder.load_file(os.path.join(os.path.dirname(__file__),'imagebutton.kv'));

class ImageButton(Button):
  filepath = StringProperty("")
  pass
