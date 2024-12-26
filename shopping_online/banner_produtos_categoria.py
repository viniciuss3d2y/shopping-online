from kivy.uix.floatlayout import FloatLayout
from botoes import ImageButtonCustom, LabelButton
import io
from kivy.core.image import Image as coreImage
from kivy.graphics import Color,RoundedRectangle, Ellipse
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image


class BannerProdutosCategoria(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__()

        self.nome_categoria = kwargs['nome_categoria']
        self.image_bin = kwargs['byte_image']
        self.nome_produto = kwargs["nome_produto"]
        self.em_promocao = kwargs['em_promocao']
        self.porcentagem_promocao = kwargs['porcentagem_promocao']
        self.preco_normal = kwargs['preco_normal']
        self.favorito = kwargs['favorito']
        self.descricao = kwargs['descricao'].title()
        self.cores_disponiveis = kwargs['cores_disponiveis']
        self.tamanhos_disponiveis = kwargs['tamanhos_disponiveis']


        self.image = Image(pos_hint= {"center_x": 0.5, "top": 1},
                                size_hint= (1, 0.6))

        with self.image.canvas.before:
            Color(rgba=get_color_from_hex("#f4f4f4"))
            self.image_rect = RoundedRectangle(pos=self.image.pos, size= self.image.size, radius=[2])
        self.bind(pos= self.update_rect, size= self.update_rect)


    
    def update_rect(self, *args):
        self.image_rect.pos = self.image.pos
        self.image_rect.size = self.image.size

    
