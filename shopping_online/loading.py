from kivy.uix.floatlayout import FloatLayout
from botoes import ImageButton, ImageButtonCustom, AsyncImageButtonCustom
import io
from kivy.core.image import Image as coreImage
from kivy.graphics import Color,RoundedRectangle,Ellipse
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
import requests
import threading
from kivy.app import App
from functools import partial
from kivy.loader import Loader

from kivymd.uix.bottomnavigation import MDBottomNavigationItem, MDBottomNavigation

from kivymd.uix.textfield import MDTextField
from kivy.uix.textinput import TextInput


MDTextField.on_text_validate



class Loading(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.source = "Camisa.gif"
        self.anim_delay = 0.1



dic = {"tata":2, "gay": "camaleao"}


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

def color_similarity(color1, color2):
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    print(r1)
    return ((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2) ** 0.5

color1 = '#d60100'
color2 = '#e83250'
similarity = color_similarity(color1, color2)

print(f'Distância entre as cores: {similarity}')

print(int('d6', 16))