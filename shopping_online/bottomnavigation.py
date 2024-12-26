from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Line
from kivy.utils import get_color_from_hex
from kivy.app import App
from functools import partial
from kivymd.uix.button import MDIconButton, MDFlatButton, MDTextButton
from kivy.metrics import dp



class BottomNavigation(GridLayout):

    lista_paginas_conter_navigation = ["homepage", "searchpage"]
    lista_instacias = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 1

        self.meu_app = App.get_running_app()

        self.conteiner_home = FloatLayout()

        # navegar homepage
        self.home = MDFlatButton(pos_hint={"center_x": 0.5, "top": 1},
                                 size_hint = (0.8, 1))
        self.home.on_release = partial(self.mudar_tela_nav_bar, butao_clicked = self.home, pagina = "homepage")
        self.home.radius = [20]
        self.icon_home = MDIconButton(icon="home-outline", size=(dp(48), dp(48)), disabled = False,
                            theme_icon_color = "Custom", 
                               pos_hint={"center_x": 0.5, "top": 1})
        self.icon_home.ripple_scale = 0
        self.label_home = MDFlatButton(text="Home",
                                       pos_hint={"center_x": 0.5, "top": 0.5}, disabled = False)
        self.conteiner_home.add_widget(self.label_home)
        self.conteiner_home.add_widget(self.icon_home)
        
        # navegar searchpage
        self.conteiner_search = FloatLayout()
        self.search = MDFlatButton(pos_hint={"center_x": 0.5, "top": 1},
                                    size_hint = (0.8, 1))
        self.search.on_release = partial(self.mudar_tela_nav_bar, butao_clicked = self.search, pagina = "searchpage")
        self.search.radius = [20]

        self.icon_search = MDIconButton(icon="compass", size=(dp(48), dp(48)), disabled = True,
                            theme_icon_color = "Custom", 
                             pos_hint={"center_x": 0.5, "top": 1})   
        self.label_search = MDFlatButton(text="Explorar",
                                       pos_hint={"center_x": 0.5, "top": 0.5}, disabled = False
                                       ) 
        self.conteiner_search.add_widget(self.label_search)    
        self.conteiner_search.add_widget(self.icon_search)

        
        # navegar perfil
        self.conteiner_perfil = FloatLayout()
        self.perfil = MDFlatButton(pos_hint={"center_x": 0.5, "top": 1},
                                    size_hint = (0.8, 1))
        self.perfil.on_release = partial(self.mudar_tela_nav_bar, butao_clicked = self.perfil, pagina = "searchpage")
        self.perfil.radius = [20]
        self.icon_perfil = MDIconButton(icon="account", size=(dp(48), dp(48)), disabled = True,
                            theme_icon_color = "Custom", 
                             pos_hint={"center_x": 0.5, "top": 1}) 
        self.label_perfil = MDFlatButton(text="Perfil",
                                       pos_hint={"center_x": 0.5, "top": 0.5}, disabled = False,
                                       text_color = (0, 0, 0, 1))   
        #self.label_perfil.disa 
        self.conteiner_perfil.add_widget(self.label_perfil)
        self.conteiner_perfil.add_widget(self.icon_perfil)


        with self.canvas:
            Color(rgba=get_color_from_hex("#a0a5ab"))
            self.linha = Line(points = [self.pos[0], (self.pos[1]+self.height), self.pos[0] + self.width, (self.pos[1]+self.height)], width = 1)
        self.bind(pos= self.atualizar_line, size= self.atualizar_line)
        
        BottomNavigation.lista_instacias.append(self)

        self.conteiner_home.add_widget(self.home)
        self.conteiner_search.add_widget(self.search)
        self.conteiner_perfil.add_widget(self.perfil)


        self.add_widget(self.conteiner_home)
        self.add_widget(self.conteiner_search)
        self.add_widget(self.conteiner_perfil)
        
    
    def atualizar_line(self, *args):
        self.linha.points = [self.pos[0], (self.pos[1]+self.height), self.pos[0] + self.width, (self.pos[1]+self.height)]

    

    def mudar_tela_nav_bar(self, butao_clicked = None, pagina = None, *args):

        if self.home == butao_clicked:
            self.icon_home.disabled = False
            self.label_home.disabled = False

            self.icon_perfil.disabled = True
            self.label_perfil.disabled = True

            self.icon_search.disabled = True
            self.label_search.disabled = True


        elif self.search == butao_clicked:
            self.icon_home.disabled = True
            self.label_home.disabled = True

            self.icon_perfil.disabled = True
            self.label_perfil.disabled = True

            self.icon_search.disabled = False
            self.label_search.disabled = False

        elif self.perfil == butao_clicked:
            self.icon_home.disabled = True
            self.label_home.disabled = True

            self.icon_perfil.disabled = False
            self.label_perfil.disabled = False

            self.icon_search.disabled = True
            self.label_search.disabled = True
        
        
        
        self.meu_app.mudar_tela(pagina)