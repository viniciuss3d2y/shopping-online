from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from botoes import ImageButtonCustom, LabelButton, ImageButton
import io
from kivy.core.image import Image as coreImage
from kivy.graphics import Color,RoundedRectangle, Ellipse
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.image import AsyncImage


class Banner_carrinho(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__()

        # imagem em formato binario
        self.url_async_image = kwargs['byte_image']
        self.quantidade = 0

        # layout quantidade
        self.conteiner_quantidade = GridLayout(
                        pos_hint = {"x": 0.9, "center_y": 0.5},
                         size_hint= (0.05, 0.9))
        self.label_quantidade = Label(text=str(self.quantidade))
        # aumenta a quantidade de intens
        self.image_mais = ImageButton(source="icones/mais.png")
        with self.image_mais.canvas.before:
            Color(rgba= get_color_from_hex("#f4f4f4"))
            self.image_mais_rect = Ellipse(pos= self.image_mais.pos, size= (self.image_mais.size[1], self.image_mais.size[1]))

        # diminui a quantidade de intens
        self.image_menos = ImageButton(source="icones/menos.png")
        with self.image_menos.canvas.before:
            Color(rgba= get_color_from_hex("#f4f4f4"))
            self.image_menos_rect = Ellipse(pos= self.image_menos.pos, size= (self.image_menos.size[1], self.image_menos.size[1]))
        # ajusta a posicao dos canvas de quantidade quando o conteiner deles mudar de tamanho
        self.conteiner_quantidade.bind(pos= self.atualizar_rect_quantidade, size= self.atualizar_rect_quantidade)
        

        with self.canvas.before:
            Color(rgba=get_color_from_hex("#FFFFFF"))
            self.rect = RoundedRectangle(pos= self.pos, size= self.size, radius= [15])
        self.bind(pos= self.atualizar_rect, size= self.atualizar_rect)

        # imagem do produto
        self.image = AsyncImage(source=self.url_async_image,
                                pos_hint = {"x": 0, "center_y": 0.5},
                                size_hint= (0.3, 0.85),
                                keep_ratio = False,
                                allow_stretch = True)

        self.conteiner_quantidade.add_widget(self.image_mais)
        self.conteiner_quantidade.add_widget(self.label_quantidade)

        self.add_widget(self.image)
        self.add_widget(self.conteiner_quantidade)



    def atualizar_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def atualizar_rect_quantidade(self, *args):
        self.image_mais_rect.pos = self.image_mais.pos
        self.image_mais_rect.size = (self.image_mais.size[1], self.image_mais.size[1])

        self.image_menos_rect.pos = self.image_menos.pos
        self.image_menos_rect.size = (self.image_menos.size[1], self.image_menos.size[1])


    def aumentar_quantidade(self, *args):
        self.quantidade += 1
        self.label_quantidade.text = str(self.quantidade)
    
    def diminuir_quantidade(self, *args):
        if self.quantidade > 0:
            self.quantidade -= 1
            self.label_quantidade.text = str(self.quantidade)