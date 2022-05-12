from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from components.ImageButton import ImageButton
from kivy.properties import ObjectProperty
from core.Recognition import Recognition
from kivy.factory import Factory 
import os

class ResultPopup(Popup):
  pass

class GuiApp(App):
  resultview = ObjectProperty()
  def __init__(self, **kwargs):
    super(GuiApp, self).__init__(**kwargs)
    self.awsrecog = Recognition()
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
      imgbtn.bind(on_release= lambda x: Factory.ResultPopup().open())
      stacklayout.add_widget(imgbtn)
  pass
  
  def build(self):
    root = self.root
    dircomp = root.ids.boxid.children[1]
    dircomp.on_dir_change_event= self.change_dir_event
    return root

if __name__ == '__main__':
  GuiApp().run()