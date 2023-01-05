from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Background(Widget):
    cloud_texture = ObjectProperty(None)


    pass


class MainApp(App):
    pass


MainApp().run()
