from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ListProperty
from kivy.uix.image import Image

class Pipe(Widget):
    # Numeric attributes / Числовые атрибуты
    GAP_SIZE = NumericProperty(60)              # Размер зазора
    CAP_SIZE =  NumericProperty(20)             # Размер шапки колонны / Height of column_cap.png
    pipe_center = NumericProperty(0)            # Центр колонны
    bottom_body_position = NumericProperty(0)   # Нижнее расположение корпуса
    bottom_cap_position = NumericProperty(0)    # Нижнее расположение крышки
    top_body_position = NumericProperty(0)      # Верхнее расположение корпуса
    top_cap_position = NumericProperty(0)       # Верхнее расположение крышки

    # Texture / Атрибуты текстуры
    pipe_body_texture = ObjectProperty(None)
    # Свойство списка
    lower_pipe_tex_coords = ListProperty((0, 0, 1, 0, 1, 1, 0, 1))  # low pipe / Нижняя труба, положение через список
    top_pipe_tex_coords = ListProperty((0, 0, 1, 0, 1, 1, 0, 1))    # Top pipe / Верхняя труба, коородинаты

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Создаем экземпляр текстуры корпуса
        self.pipe_body_texture = Image(source='column_body.png').texture
        self.pipe_body_texture.wrap = 'repeat'
