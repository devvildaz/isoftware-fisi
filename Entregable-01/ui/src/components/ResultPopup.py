import os 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.lang.builder import Builder
from core.Recognition import ProcessFoo

Builder.load_file(os.path.join(os.path.dirname(__file__),'resultpopup.kv'));

class ResultPopup(Popup):
  photodir = StringProperty("")

  def load_file(self):
    response = ProcessFoo(self.photodir)
    box = self.ids.resultbox
    for item in response:
      imagebuf = item['image']
      imagecomp = Image(
        size_hint_y=None,
        height=160,
        texture=imagebuf.texture, 
        keep_ratio=True
      )
      box.add_widget(imagecomp)
      labelbox = BoxLayout(orientation='vertical', size_hint_y=0)
      for labelitm in item['labels']:  
        labelbox.add_widget(Label(text=str(labelitm), size_hint=(1,None), height=20))
      box.add_widget(labelbox)
  pass