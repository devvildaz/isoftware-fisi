from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button 
from components.ImageButton import ImageButton
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty 
from core.Recognition import ProcessFoo 
from kivy.factory import Factory 
import json
import os

class ResultPopup(Popup):
  photodir = StringProperty("")

  def load_file(self):
    response = ProcessFoo(self.photodir)
    box = self.ids.resultbox
    
    for item in response:
      box.add_widget(Button(size_hint_y=None,text=str(type(item['image']))))
      for label in item['labels']:
        box.add_widget(Button(text=str(type(label)), size_hint_y=None))
  pass

class GuiApp(App):
  resultview = ObjectProperty()
  def __init__(self, **kwargs):
    super(GuiApp, self).__init__(**kwargs)
  def change_dir_event(self, dirpath):
    root = self.root
    stacklayout = root.ids.boxid.children[0]
    stacklayout.clear_widgets()
    files = [
      os.path.join(dirpath, f) 
      for f in os.listdir(dirpath) 
      if os.path.isfile(os.path.join(dirpath, f))
        and f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))
    ]
    
    for i, v in enumerate(files):
      imgbtn = ImageButton(
        size_hint=(None,None), 
        size=(125,125),
        filepath=v
      )
      imgbtn.id = i
      imgbtn.bind(on_release=lambda x : Factory.ResultPopup(photodir=v).open()) 
      stacklayout.add_widget(imgbtn)
  pass
  
  def build(self):
    root = self.root
    dircomp = root.ids.boxid.children[1]
    dircomp.on_dir_change_event= self.change_dir_event
    return root

if __name__ == '__main__':
  GuiApp().run()
