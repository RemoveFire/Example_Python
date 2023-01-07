from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock


from pipe import Pipe
from random import randint


class Background(Widget):
    cloud_texture = ObjectProperty(None)
    cloud_texture_2 = ObjectProperty(None)
    floor_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create textures / Создание текстур
        self.cloud_texture = Image(source="cloud.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)   # Создание повторения картинки
        # ", -1" в конце указывается для инвертирования изображения, т.к. оно загружается верх ногами

        self.cloud_texture_2 = Image(source="cloud_2.png").texture
        self.cloud_texture_2.wrap = 'repeat'
        self.cloud_texture_2.uvsize = (Window.width / self.cloud_texture_2.width, -1)

        self.floor_texture = Image(source="floor.png").texture
        self.floor_texture.wrap = 'repeat'
        self.floor_texture.uvsize = (Window.width / self.floor_texture.width, -1)

    def on_size(self, *args):
        self.cloud_texture.uvsize = (self.width / self.cloud_texture.width, -1)
        self.cloud_texture_2.uvsize = (self.width / self.cloud_texture.width, -1)
        self.floor_texture.uvsize = (self.width / self.floor_texture.width, -1)

    def scroll_textures(self, time_passed):
        # Update the uvpos of the texture / обновление uvpos текстуры
        self.cloud_texture.uvpos = (
            (self.cloud_texture.uvpos[0] + time_passed / 16.0) % Window.width, self.cloud_texture.uvpos[1])
        # cloud_texture.uvpos[0] + time_passed - берем исходную позицию и с помощью
        # знака "+" или "-" указываем направление движения, далее указываем интенсивность обновления
        self.cloud_texture_2.uvpos = (
            (self.cloud_texture_2.uvpos[0] + time_passed / 6.0) % Window.width, self.cloud_texture_2.uvpos[1])
        # Добавляем движение текстуры пола
        self.floor_texture.uvpos = (
            (self.floor_texture.uvpos[0] + time_passed / 6.0) % Window.width, self.floor_texture.uvpos[1])

        # Redraw the texture / перерисовка текстуры
        texture = self.property('cloud_texture')
        texture.dispatch(self)

        texture = self.property('cloud_texture_2')
        texture.dispatch(self)

        texture = self.property('floor_texture')
        texture.dispatch(self)


class MainApp(App):
    pipes = []  # Создаем пустой список, в который будем добавлять каждую свою трубу

    def on_start(self):
        # id: background в main.kv - явл.идентификатором фона, к которому обращаемся self.root.ids.background
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/60.)    # 1/60. - по сути кадры в секунды

    def start_game(self):
        # Создаем текстуры труб / Create the pipes
        num_pipes = 5   # Задаем для начала параметр числа труб
        # Расстояние между трубами, которое рассчитывается из ширины окна
        distance_between_pipes = Window.width / (num_pipes - 1)
        for i in range(num_pipes):
            pipe = Pipe()
            # Установим центр трубу (расчет из зазора верха и низа),
            # при этом будет случайным. Задаем исходя из высоты нашего пола,
            # который равен 50 со смещением, к примеру 100. И зазор сверху должен быть ограничен высотой
            pipe.pipe_center = randint(50 + 100, self.root.height - 100)
            pipe.size_hint = (None, None)
            # Делаем, где хотим чтоб труба располагалась, когда создаем (за пределами экрана справа) и делаем смещение
            pipe.pos = ( i * distance_between_pipes, 50)
            # Ширина трубы должна быть равна ширине cap_pipe (верхушки трубы).
            # 64 - потому что размер картинки, далее высота трубы с вычетом пола
            pipe.size = (64, self.root.height - 50)
            # Добавим трубы при нажатии на кнопку старт
            self.pipes.append(pipe)
            self.root.add_widget(pipe)

        # Перенос трубы раз в 60 кадров в секунду / Move the pipes
        Clock.schedule_interval(self.move_pipes, 1/60.)

    def move_pipes(self, time_passed):
        # Перенесли все трубы, задали движение на лево
        for pipe in self.pipes:
            pipe.x -= time_passed * 100

        # Проверка, не нужно ли поставить трубу справой стороны
        # Check if we need to reposition the pipe at the right side

        # Создаем текстуры труб / Create the pipes
        num_pipes = 5  # Задаем для начала параметр числа труб
        # Расстояние между трубами, которое рассчитывается из ширины окна
        distance_between_pipes = Window.width / (num_pipes - 1)

        pipe_xs = list(map(lambda pipe: pipe.x, self.pipes))  # Массив прохождения по каждому элементу трубы, помещаем x
        right_most_x = max(pipe_xs)  # Проверяем крайнее правое - просто максимальное значение трубы
        if right_most_x <= Window.width - distance_between_pipes:
            # Если условие верно, то нам нужно получить левый x (самую левую трубу)
            most_left_pipe = self.pipes[pipe_xs.index(min(pipe_xs))]
            most_left_pipe.x = Window.width


MainApp().run()
