from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.event import EventDispatcher
import os 

Builder.load_file(os.path.join(os.path.dirname(__file__),'directorysearch.kv'));

class DirectorySearch(BoxLayout):
  def __init__(self, **kwargs):
    super(DirectorySearch, self).__init__(**kwargs)
  def on_dir_change_event(self,value):
    pass
  pass
