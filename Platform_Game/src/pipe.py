from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ListProperty
from kivy.uix.image import Image
from kivy.clock import Clock


class Pipe(Widget):
    # Numeric attributes / Числовые атрибуты
    GAP_SIZE = NumericProperty(80)              # Размер зазора
    CAP_SIZE = NumericProperty(20)              # Размер шапки колонны / Height of column_cap.png
    pipe_center = NumericProperty(0)            # Центр колонны
    bottom_body_position = NumericProperty(0)   # Нижнее расположение корпуса
    bottom_cap_position = NumericProperty(0)    # Нижнее расположение крышки
    top_body_position = NumericProperty(0)      # Верхнее расположение корпуса
    top_cap_position = NumericProperty(0)       # Верхнее расположение крышки

    # Texture / Атрибуты текстуры
    pipe_body_texture = ObjectProperty(None)
    # Свойство списка
    lower_pipe_tex_coords = ListProperty((0, 0, 1, 0, 1, 1, 0, 1))  # low pipe / Нижняя труба, положение через список
    top_pipe_tex_coords = ListProperty((0, 0, 1, 0, 1, 1, 0, 1))    # Top pipe / Верхняя труба, координаты

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Создаем экземпляр текстуры корпуса
        self.pipe_body_texture = Image(source='column_body.png').texture
        self.pipe_body_texture.wrap = 'repeat'

    def on_size(self, *args):
        lower_body_size = self.bottom_cap_position + self.bottom_body_position

        self.lower_pipe_tex_coords[5] = lower_body_size/20.
        self.lower_pipe_tex_coords[7] = lower_body_size/20.

        top_body_size = self.top - self.top_body_position   # определяем размер тела, от самого верха позиции

        # Растягиваем изображением с повторением в кол раз, на которое делим с определением точки для растяжения
        self.top_pipe_tex_coords[5] = top_body_size/20.
        self.top_pipe_tex_coords[7] = top_body_size/20.

    def on_pipe_center(self, *args):    # Каждый раз, когда изменяется центр трубы, будет перерисовывать текстуры
        Clock.schedule_once(self.on_size, 0)    # 0 - вызываем как только возможно сразу
