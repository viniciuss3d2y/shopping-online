from botoes import ImageButtonCustom
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.metrics import dp
from kivy.graphics import Color,RoundedRectangle,Ellipse


class IconeCarrinho(FloatLayout):
    lista_instancia = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.meu_app = App.get_running_app()

        self.icone = ImageButtonCustom(pos_hint = {"center_x":0.5, "center_y": 0.5},
                                       size_hint = (1, 1),
                                       source = "icones\carrinho.png",
                                       on_release = self.meu_app.ver_produtos_carrinho)
        
        self.badge = Label(pos_hint = {"center_x":0.75, "top": 1},
                            size_hint = (None, None),
                            size = (dp(16), dp(16)),
                            text = "5",
                            font_size = "12sp",
                            bold=True)
        
        with self.badge.canvas.before:
            Color(rgba=(1, 0, 0, 1))
            self.rect_badge = Ellipse(size = self.badge.size, pos= self.badge.pos)
        self.badge.bind(pos= self.atualizar_rect_badge, size= self.atualizar_rect_badge)

        IconeCarrinho.lista_instancia.append(self)

        self.add_widget(self.icone)
        self.add_widget(self.badge)

    def atualizar_rect_badge(self, *args):
        self.rect_badge.pos = self.badge.pos
        self.rect_badge.size = self.badge.size
                    

"""
        Label:
            pos_hint: {"x": 0.8, "top": 1}
            size_hint : None, None
            size : dp(20), dp(20)
            text: "5"
            canvas.before:
                Color:
                    rgba: 1, 0,0, 0.2
                Ellipse:
                    size: self.size
                    pos: self.pos

"""