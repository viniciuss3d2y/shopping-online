from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
# from botoes import LabelButtonCustomizado
# from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
# from kivy.animation import Animation
from botoes import ImageButton, LabelButton
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Line
from functools import partial



class BotoesHomePage(GridLayout):

    def __init__(self, **kwargs):
        super().__init__()
        
        self.rows = 1
        self.pos_hint = {"center_x": 0.5, "top": 0.15}
        self.size_hint = (1, 0.1)
        self.meu_app = App.get_running_app()

        with self.canvas:
            Color(rgba = (0, 0, 0, 0.2))
            Line(points=[0, Window.height * 0.15, Window.width , Window.height * 0.15], width=1)

        
        self.float_botao_home = FloatLayout()
        self.home = ImageButton(source = "icones/home.png", pos_hint= {"center_x": 0.5, "center_y": 0.5},
                                size_hint= (0.5, 0.5))
        self.label_home = LabelButton(text = "Home", color = (0, 0, 0, 1), pos_hint= {"center_x": 0.5, "center_y": 0.1},
                                size_hint= (1, 0.05))

        self.float_botao_lupa = FloatLayout()
        self.lupa = ImageButton(source = "icones/lupa.png", pos_hint= {"center_x": 0.5, "center_y": 0.5},
                                size_hint= (1, 0.5))
        self.label_lupa = LabelButton(text = "proucurar", color = (0, 0, 0, 1), pos_hint= {"center_x": 0.5, "center_y": 0.1},
                                size_hint= (1, 0.05),
                                on_release=partial(self.meu_app.mudar_tela, "searchpage"))

        self.float_botao_perfil = FloatLayout()
        self.perfil = ImageButton(source = "icones/perfil.png", pos_hint= {"center_x": 0.5, "center_y": 0.5},
                                size_hint= (1, 0.5))
        self.label_perfil = LabelButton(text = "perfil", color = (0, 0, 0, 1), pos_hint= {"center_x": 0.5, "center_y": 0.1},
                                size_hint= (1, 0.05))

        
        self.float_botao_home.add_widget(self.home)
        self.float_botao_home.add_widget(self.label_home)

        
        

        self.float_botao_lupa.add_widget(self.lupa)
        self.float_botao_lupa.add_widget(self.label_lupa)

        self.float_botao_perfil.add_widget(self.perfil)
        self.float_botao_perfil.add_widget(self.label_perfil)

        self.add_widget(self.float_botao_home)
        self.add_widget(self.float_botao_lupa)
        self.add_widget(self.float_botao_perfil)

        