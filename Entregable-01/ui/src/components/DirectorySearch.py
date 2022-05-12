from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
import os 

Builder.load_file(os.path.join(os.path.dirname(__file__),'directorysearch.kv'));

class DirectorySearch(BoxLayout):
  pass
