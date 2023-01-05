from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image



class Background(Widget):
    cloud_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create textures / Создание тексутр
        self.cloud_texture = Image(source="cloud.png").texture


    pass


class MainApp(App):
    pass


MainApp().run()
