from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock


class Background(Widget):
    cloud_texture = ObjectProperty(None)
    cloud_texture_2 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create textures / Создание тексутр
        self.cloud_texture = Image(source="cloud.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)   # Создание повторения картинки
        # ", -1" в конце указывается для инвертирования изображения, т.к. оно загружается верх ногами

        self.cloud_texture_2 = Image(source="cloud_2.png").texture
        self.cloud_texture_2.wrap = 'repeat'
        self.cloud_texture_2.uvsize = (Window.width / self.cloud_texture_2.width, -1)

    def scroll_textures(self, time_passed):
        # Update the uvpos of the texture / обновление uvpos текстуры
        self.cloud_texture.uvpos = (
            (self.cloud_texture.uvpos[0] + time_passed / 16.0) % Window.width, self.cloud_texture.uvpos[1])
        # cloud_texture.uvpos[0] + time_passed - берем исходную позицию и с помощью
        # знака "+" или "-" указываем направление движения, далее указываем интенсивность обновления
        self.cloud_texture_2.uvpos = (
            (self.cloud_texture_2.uvpos[0] - time_passed / 2.0) % Window.width, self.cloud_texture_2.uvpos[1])


        # Redraw the texture / перерисовка текстуры
        texture = self.property('cloud_texture')
        texture.dispatch(self)

        texture = self.property('cloud_texture_2')
        texture.dispatch(self)


class MainApp(App):
    def on_start(self):
        # id: background в main.kv - явл.идетнитфикатором фона, к которому обращаемся self.root.ids.background
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/60.)    # 1/60. - по сути кадры в секунды

    pass


MainApp().run()
