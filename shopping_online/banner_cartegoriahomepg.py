from kivy.uix.floatlayout import FloatLayout
from botoes import  LabelButton, ImageTesteCircularAnimation
import io
from kivy.core.image import Image as coreImage

from kivy.utils import get_color_from_hex
from kivy.app import App
from functools import partial
from kivymd.uix.behaviors import CircularRippleBehavior
from kivy.uix.image import AsyncImage


class BannerCartegoriaHomePG(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__()

        self.url_asyncimage = kwargs['url_asyncimage']
        self.nome_categoria = kwargs['nome_categoria']
        self.meu_app = App.get_running_app()



        self.image = ImageTesteCircularAnimation(pos_hint= {"center_x": 0.5, "top": 1},
                                size_hint= (0.8, 0.8), source = self.url_asyncimage)

        self.image.on_release = partial(self.meu_app.ver_produtos_categoria_thread, nome_categoria = self.nome_categoria)

        self.label_nome_categoria = LabelButton(text = self.nome_categoria.capitalize(),pos_hint= {"center_x": 0.5, "top": 0.24},
                                size_hint= (1, 0.1), font_size = '9sp',
                                color = get_color_from_hex("#34353a"), font_name = "sanchez/Sanchezregular.otf")
        

        self.add_widget(self.label_nome_categoria)
        self.add_widget(self.image)

