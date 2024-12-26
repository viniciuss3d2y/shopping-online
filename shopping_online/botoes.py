
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
# from kivy.animation import Animation
from kivy.properties import ObjectProperty, BooleanProperty
# from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.widget import Widget
# from kivy.app import App
# import requests
from kivy.core.window import Window
from kivy.app import App

from kivy.clock import Clock
from functools import partial
import time
from kivy.uix.image import AsyncImage
from kivymd.uix.behaviors import CircularRippleBehavior, RectangularRippleBehavior
from kivymd.uix.menu import MDDropdownMenu




class ImageButton(ButtonBehavior, Image):
    pass

class LabelButton(RectangularRippleBehavior ,ButtonBehavior, Label):
    def __init__(self, **kwargs):
        self.ripple_scale = 1
        self.ripple_duration_in_fast = 1
        self.ripple_duration_in_slow= 3
        self.ripple_alpha = 0.13
        self.ripple_color = (0, 0, 0)
        super().__init__(**kwargs)

# class LabelAjusteTela(Label):
#     posicao_y = ObjectProperty((0.47))
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         Window.bind(width= self.on_size, height= self.on_size)
        
#     def on_size(self, *args):
#         self.pos_hint = {}
#         self.size_hint = (None, None)
        
#         self.pos = (40 , Window.height * self.posicao_y)
#         self.size = (Window.width *0.2, Window.height* 0.05)


# class LabelButtonAjusteTela(ButtonBehavior, Label):
    
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         Window.bind(width= self.on_size, height= self.on_size)
        
#     def on_size(self, *args):
#         self.pos_hint = {}
#         self.size_hint = (None, None)
        
#         self.pos = (Window.width * 0.8, Window.height * 0.47)
#         self.size = (Window.width *0.2, Window.height* 0.05)

# label
class LabelCustom(Label):
    posicao_x = ObjectProperty((15))
    posicao_y = ObjectProperty((0.67))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.pos = (self.posicao_x, Window.height * self.posicao_y)
        self.font_name = "ClearSans-Bold.ttf"
        
        self.halign = 'left'
        self.valign = 'middle'
        self.padding = (0, 0)

        Window.bind(width= self.on_size, height= self.on_size)
    def on_size(self, *args):
        self.pos = (self.posicao_x, Window.height * self.posicao_y)

    def on_texture_size(self, *args):
        self.size_hint= (None, None)
        self.text_size = self.texture_size
        self.size = self.texture_size


# label button
class LabelButtonCustom(ButtonBehavior, Label):
    posicao_x = ObjectProperty((0))
    posicao_y = ObjectProperty((0))
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.pos = ((Window.width - self.size[0])- 15, Window.height * self.posicao_y)
        self.halign = 'left'
        self.valign = 'middle'
        self.padding = (0, 0)

        Window.bind(width= self.on_size,height= self.on_size)
    def on_size(self, *args):
        self.pos = ((Window.width - self.size[0])- 15, Window.height * self.posicao_y)
    
    def on_texture_size(self, *args):
        self.size_hint = (None, None)
        self.size = self.texture_size
        self.text_size = self.texture_size



# class ImageButtonCustomDois(ButtonBehavior, Image):
#     seu_numero = ObjectProperty((1))
#     visivel = ObjectProperty((False))
#     ultimo_visivel = ObjectProperty((False))
#     posicionar_parar_mover = ObjectProperty((True))
#     # usar pra ativar o movimento automatico dos banners
#     ativar_movimento_auto = ObjectProperty((False))

#     pode_mover = True
#     velocidade_movimento_original = 109
#     velocidade_movimento = 109
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         self.meu_app = App.get_running_app()
#         self.homepage = self.meu_app.root.ids["homepage"]
#         # conteiner dos banners
#         self.float_banners = self.homepage.ids["float_banners"]
#         self.mover_widget_direita = False
#         self.mover_widget_esquerda = False

#         self.pos_x_first_click = 0
        
#         self.tamnho_janela = Window.width
#         self.keep_ratio = False
#         self.allow_stretch = True
#         self.teste_chama = True
#         #self.size_hint = (None, None)
#         #self.bind(ativar_movimento_auto= self.mover_widget_automatico)
#         Window.bind(width= self.atualizar_tamanho_janela)
#         Window.bind(width= self.on_size, height= self.on_size)
    
#     def on_touch_down(self, touch):
#         self.pos_x_first_click = touch.pos[0]

#         return super().on_touch_down(touch)
#         #return True
    

#     def on_size(self, *args):
#         if self.visivel:
#             self.pos = ((self.tamnho_janela/2) - (self.width / 2), Window.height * 0.73)
#         else:
#             self.pos = (self.tamnho_janela + self.width, Window.height * 0.9)
        
#         self.size_hint = (0.9, 1)

#     def atualizar_tamanho_janela(self, *args):
#         self.tamnho_janela = Window.width

#     def on_touch_move(self, touch):
#         if self.collide_point(*touch.pos):
            
#             Clock.unschedule(self.meu_app.ativar_movimento_auto)
#             self.meu_app.chamar_funcao_ativar_movimento_auto(None)

#             if touch.pos[0] > self.pos_x_first_click + 5:
    
#                 self.mover_widget_esquerda = True
#                 self.mover_widget_direita = False         
            
#             elif touch.pos[0] < self.pos_x_first_click - 5:
                
#                 self.mover_widget_direita = True
#                 self.mover_widget_esquerda = False

#             else:
#                 self.mover_widget_direita = False
#                 self.mover_widget_esquerda = False

#             #if self.pos[0] < 0:
#             if self.mover_widget_direita and self.pode_mover :    
#                 ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original  

#                 if self.seu_numero == 1:
#                     for widget in list(self.float_banners.children):

#                         if widget.seu_numero == self.seu_numero + 1:
#                             # ajustar a posicao do widget para movelo
#                             widget.pos = (self.tamnho_janela, self.pos[1])

#                             widget.visivel = True
#                             self.ultimo_visivel = True
#                             self.visivel = False
#                             #ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original
#                             Clock.schedule_interval(self.meu_app.mover_banners, 1/30)

#                 elif self.seu_numero == self.meu_app.qtd_banners:

#                     for widget in list(self.float_banners.children):

#                         if widget.seu_numero == 1:
#                             # ajustar a posicao do widget para movelo
#                             widget.pos = (self.tamnho_janela , self.pos[1])
#                             widget.visivel = True
#                             self.ultimo_visivel = True
#                             self.visivel = False
#                             #ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original
#                             Clock.schedule_interval(self.meu_app.mover_banners, 1/30)
                            


#                 elif self.seu_numero != self.meu_app.qtd_banners and self.seu_numero != 1:
#                     for widget in list(self.float_banners.children):

#                         if widget.seu_numero == self.seu_numero + 1:
#                             # ajustar a posicao do widget para movelo

#                             widget.pos = (self.tamnho_janela, self.pos[1])

#                             widget.visivel = True
#                             self.ultimo_visivel = True
#                             self.visivel = False
#                             #ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original
#                             Clock.schedule_interval(self.meu_app.mover_banners, 1/30)
                                


                  
            
#             elif self.mover_widget_esquerda and self.pode_mover:
#                 ImageButtonCustomDois.velocidade_movimento = self.velocidade_movimento_original
#                 if self.seu_numero == self.meu_app.qtd_banners:
#                     for widget in list(self.float_banners.children):
#                         if widget.seu_numero == self.seu_numero - 1:

#                             widget.pos = (-self.width, self.pos[1])

#                             widget.visivel = True
#                             self.ultimo_visivel = True
#                             self.visivel = False
#                             #ImageButtonCustomDois.velocidade_movimento = self.velocidade_movimento_original
#                             Clock.schedule_interval(self.meu_app.mover_banners, 1/30)


#                 elif self.seu_numero == 1:
#                     for widget in list(self.float_banners.children):
#                         if widget.seu_numero == self.meu_app.qtd_banners:

#                             widget.pos = (-self.width, self.pos[1])

#                             widget.visivel = True
#                             self.ultimo_visivel = True
#                             self.visivel = False
#                             #ImageButtonCustomDois.velocidade_movimento = self.velocidade_movimento_original
#                             Clock.schedule_interval(self.meu_app.mover_banners, 1/30)


#                 elif self.seu_numero != self.meu_app.qtd_banners and self.seu_numero != 1:
#                     for widget in list(self.float_banners.children):
#                         if widget.seu_numero == self.seu_numero - 1:

#                             widget.pos = (-self.width, self.pos[1])

#                             widget.visivel = True
#                             self.ultimo_visivel = True
#                             self.visivel = False
#                             #ImageButtonCustomDois.velocidade_movimento = self.velocidade_movimento_original
#                             Clock.schedule_interval(self.meu_app.mover_banners, 1/30)

    
# #, instancia, value

#     def mover_widget_automatico(self):

#         #if value == True:         

#         ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original

#         if self.seu_numero == 1:
#             for widget in list(self.float_banners.children):

#                 if widget.seu_numero == self.seu_numero + 1:
#                     # ajustar a posicao do widget para movelo
#                     widget.pos = (self.tamnho_janela, self.pos[1])

#                     widget.visivel = True
#                     self.ultimo_visivel = True
#                     self.visivel = False
#                     #ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original
#                     Clock.schedule_interval(self.meu_app.mover_banners, 1/30)

#         elif self.seu_numero == self.meu_app.qtd_banners:

#             for widget in list(self.float_banners.children):

#                 if widget.seu_numero == 1:
#                     # ajustar a posicao do widget para movelo
#                     widget.pos = (self.tamnho_janela , self.pos[1])
#                     widget.visivel = True
#                     self.ultimo_visivel = True
#                     self.visivel = False
#                     #ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original
#                     Clock.schedule_interval(self.meu_app.mover_banners, 1/30)
                    


#         elif self.seu_numero != self.meu_app.qtd_banners and self.seu_numero != 1:
#             for widget in list(self.float_banners.children):

#                 if widget.seu_numero == self.seu_numero + 1:
#                     # ajustar a posicao do widget para movelo

#                     widget.pos = (self.tamnho_janela, self.pos[1])

#                     widget.visivel = True
#                     self.ultimo_visivel = True
#                     self.visivel = False
#                     #ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original
#                     Clock.schedule_interval(self.meu_app.mover_banners, 1/30)
                            


#     def mover_widget_automatico_intervalo(self):
#         Clock.schedule_interval(self.mover_widget_automatico, 8)



class ImageTesteCircularAnimation(CircularRippleBehavior, ButtonBehavior, AsyncImage):
    def __init__(self, **kwargs):
        self.ripple_scale = 1
        self.ripple_duration_in_fast = 0.7
        self.ripple_duration_in_slow= 5
        self.ripple_alpha = 0.13
        self.ripple_color = (0, 0, 0)
        super().__init__(**kwargs)





class ImageButtonCustom(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.incremento = 0
        self.incremento_original = 0
        self.raio = 0
        self.centro = (0, 0)
        self.tempo_click = time.time()

        with self.canvas.after:
            
            self.cor = Color(rgba= (0, 0, 0, 0.07))
            self.circulo = Ellipse(pos=(self.centro[0]- self.raio, self.centro[1]- self.raio), size=(0, 0))


    def aumentar_tamanho_ellipse(self, dt): 
        if self.circulo.size[0] < (self.size[1] * 0.7):
            self.raio += self.incremento * dt
            self.incremento += 11.52
            
            self.circulo.size = (self.raio * 2, self.raio * 2)
            self.circulo.pos = (self.centro[0]- self.raio, self.centro[1]- self.raio)
    

    def chamar_diminuir_tamanho_ellipse(self, dt):
        Clock.schedule_interval(self.diminuir_tamanho_ellipse, 1/60)

    def diminuir_tamanho_ellipse(self, dt):
        
        if self.raio > 0:
            self.raio -= self.incremento * dt
            self.incremento += 11.52
        self.circulo.size = (self.raio * -2, self.raio * -2)
        self.cor.rgba[3] = 0.05

        if self.raio <= 0:
            Clock.unschedule(self.diminuir_tamanho_ellipse)
            self.circulo.size = (0, 0)
            self.cor.rgba[3] = 0
        
        self.circulo.pos = (self.centro[0]+ self.raio, self.centro[1]+ self.raio)


    def on_touch_down(self, touch):

        if self.collide_point(*touch.pos):
            self.centro = touch.pos
            self.cor.rgba[3] = 0.1

            Clock.schedule_interval(self.aumentar_tamanho_ellipse, 1/60)

        return super().on_touch_down(touch)

    
    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.centro = touch.pos
            self.circulo.pos = (touch.x - self.raio, touch.y - self.raio)
        

        return super().on_touch_move(touch)
        

    def on_touch_up(self, touch):
        self.incremento = self.incremento_original
        Clock.schedule_once(self.desativar_aumento, 0.2)

        return super().on_touch_up(touch)

    def desativar_aumento(self, dt):
        Clock.unschedule(self.aumentar_tamanho_ellipse)

        Clock.schedule_once(self.chamar_diminuir_tamanho_ellipse, 0.2)



class LabelDescricao(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
        self.bind(size= self.setter('text_size'))







class AsyncImageButtonCustom(ButtonBehavior, AsyncImage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.incremento = 0
        self.incremento_original = 0
        self.raio = 0
        self.centro = (0, 0)
        self.tempo_click = time.time()

        with self.canvas.after:
            
            self.cor = Color(rgba= (0, 0, 0, 0.07))
            self.circulo = Ellipse(pos=(self.centro[0]- self.raio, self.centro[1]- self.raio), size=(0, 0))


    def aumentar_tamanho_ellipse(self, dt): 
        if self.circulo.size[0] < (self.size[1] * 0.7):
            self.raio += self.incremento * dt
            self.incremento += 11.52
            
            self.circulo.size = (self.raio * 2, self.raio * 2)
            self.circulo.pos = (self.centro[0]- self.raio, self.centro[1]- self.raio)
    

    def chamar_diminuir_tamanho_ellipse(self, dt):
        Clock.schedule_interval(self.diminuir_tamanho_ellipse, 1/60)

    def diminuir_tamanho_ellipse(self, dt):
        
        if self.raio > 0:
            self.raio -= self.incremento * dt
            self.incremento += 11.52
        self.circulo.size = (self.raio * -2, self.raio * -2)
        self.cor.rgba[3] = 0.05

        if self.raio <= 0:
            Clock.unschedule(self.diminuir_tamanho_ellipse)
            self.circulo.size = (0, 0)
            self.cor.rgba[3] = 0
        
        self.circulo.pos = (self.centro[0]+ self.raio, self.centro[1]+ self.raio)


    def on_touch_down(self, touch):

        if self.collide_point(*touch.pos):
            self.centro = touch.pos
            self.cor.rgba[3] = 0.1

            Clock.schedule_interval(self.aumentar_tamanho_ellipse, 1/60)

        return super().on_touch_down(touch)

    
    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.centro = touch.pos
            self.circulo.pos = (touch.x - self.raio, touch.y - self.raio)
        

        return super().on_touch_move(touch)
        

    def on_touch_up(self, touch):
        self.incremento = self.incremento_original
        Clock.schedule_once(self.desativar_aumento, 0.2)

        return super().on_touch_up(touch)

    def desativar_aumento(self, dt):
        Clock.unschedule(self.aumentar_tamanho_ellipse)

        Clock.schedule_once(self.chamar_diminuir_tamanho_ellipse, 0.2)
















class  AsyncImageButtonCustomDois(ButtonBehavior, AsyncImage):
    seu_numero = ObjectProperty((1))
    visivel = ObjectProperty((False))
    ultimo_visivel = ObjectProperty((False))
    posicionar_parar_mover = ObjectProperty((True))
    # usar pra ativar o movimento automatico dos banners
    ativar_movimento_auto = ObjectProperty((False))

    pode_mover = True
    velocidade_movimento_original = 109
    velocidade_movimento = 109
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.meu_app = App.get_running_app()
        self.homepage = self.meu_app.root.ids["homepage"]
        # conteiner dos banners
        self.float_banners = self.homepage.ids["float_banners"]
        self.mover_widget_direita = False
        self.mover_widget_esquerda = False

        self.pos_x_first_click = 0
        
        self.tamnho_janela = Window.width
        self.keep_ratio = False
        self.allow_stretch = True
        self.teste_chama = True
        #self.size_hint = (None, None)
        #self.bind(ativar_movimento_auto= self.mover_widget_automatico)
        Window.bind(width= self.atualizar_tamanho_janela)
        Window.bind(width= self.on_size, height= self.on_size)
    
    def on_touch_down(self, touch):
        self.pos_x_first_click = touch.pos[0]

        return super().on_touch_down(touch)
        #return True
    

    def on_size(self, *args):
        if self.visivel:
            self.pos = ((self.tamnho_janela/2) - (self.width / 2), Window.height * 0.73)
        else:
            self.pos = (self.tamnho_janela + self.width, Window.height * 0.9)
        
        self.size_hint = (0.9, 1)

    def atualizar_tamanho_janela(self, *args):
        self.tamnho_janela = Window.width

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            
            Clock.unschedule(self.meu_app.ativar_movimento_auto)
            self.meu_app.chamar_funcao_ativar_movimento_auto(None)

            if touch.pos[0] > self.pos_x_first_click + 5:
    
                self.mover_widget_esquerda = True
                self.mover_widget_direita = False         
            
            elif touch.pos[0] < self.pos_x_first_click - 5:
                
                self.mover_widget_direita = True
                self.mover_widget_esquerda = False

            else:
                self.mover_widget_direita = False
                self.mover_widget_esquerda = False

            #if self.pos[0] < 0:
            if self.mover_widget_direita and self.pode_mover :    
                AsyncImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original  

                if self.seu_numero == 1:
                    for widget in list(self.float_banners.children):

                        if widget.seu_numero == self.seu_numero + 1:
                            # ajustar a posicao do widget para movelo
                            widget.pos = (self.tamnho_janela, self.pos[1])

                            widget.visivel = True
                            self.ultimo_visivel = True
                            self.visivel = False
                            #ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original
                            Clock.schedule_interval(self.meu_app.mover_banners, 1/30)

                elif self.seu_numero == self.meu_app.qtd_banners:

                    for widget in list(self.float_banners.children):

                        if widget.seu_numero == 1:
                            # ajustar a posicao do widget para movelo
                            widget.pos = (self.tamnho_janela , self.pos[1])
                            widget.visivel = True
                            self.ultimo_visivel = True
                            self.visivel = False
                            #ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original
                            Clock.schedule_interval(self.meu_app.mover_banners, 1/30)
                            


                elif self.seu_numero != self.meu_app.qtd_banners and self.seu_numero != 1:
                    for widget in list(self.float_banners.children):

                        if widget.seu_numero == self.seu_numero + 1:
                            # ajustar a posicao do widget para movelo

                            widget.pos = (self.tamnho_janela, self.pos[1])

                            widget.visivel = True
                            self.ultimo_visivel = True
                            self.visivel = False
                            #ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original
                            Clock.schedule_interval(self.meu_app.mover_banners, 1/30)
                                


                  
            
            elif self.mover_widget_esquerda and self.pode_mover:
                AsyncImageButtonCustomDois.velocidade_movimento = self.velocidade_movimento_original
                if self.seu_numero == self.meu_app.qtd_banners:
                    for widget in list(self.float_banners.children):
                        if widget.seu_numero == self.seu_numero - 1:

                            widget.pos = (-self.width, self.pos[1])

                            widget.visivel = True
                            self.ultimo_visivel = True
                            self.visivel = False
                            #ImageButtonCustomDois.velocidade_movimento = self.velocidade_movimento_original
                            Clock.schedule_interval(self.meu_app.mover_banners, 1/30)


                elif self.seu_numero == 1:
                    for widget in list(self.float_banners.children):
                        if widget.seu_numero == self.meu_app.qtd_banners:

                            widget.pos = (-self.width, self.pos[1])

                            widget.visivel = True
                            self.ultimo_visivel = True
                            self.visivel = False
                            #ImageButtonCustomDois.velocidade_movimento = self.velocidade_movimento_original
                            Clock.schedule_interval(self.meu_app.mover_banners, 1/30)


                elif self.seu_numero != self.meu_app.qtd_banners and self.seu_numero != 1:
                    for widget in list(self.float_banners.children):
                        if widget.seu_numero == self.seu_numero - 1:

                            widget.pos = (-self.width, self.pos[1])

                            widget.visivel = True
                            self.ultimo_visivel = True
                            self.visivel = False
                            #ImageButtonCustomDois.velocidade_movimento = self.velocidade_movimento_original
                            Clock.schedule_interval(self.meu_app.mover_banners, 1/30)



    def mover_widget_automatico(self):

        #if value == True:         

        AsyncImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original

        if self.seu_numero == 1:
            for widget in list(self.float_banners.children):

                if widget.seu_numero == self.seu_numero + 1:
                    # ajustar a posicao do widget para movelo
                    widget.pos = (self.tamnho_janela, self.pos[1])

                    widget.visivel = True
                    self.ultimo_visivel = True
                    self.visivel = False
                    #ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original
                    Clock.schedule_interval(self.meu_app.mover_banners, 1/30)

        elif self.seu_numero == self.meu_app.qtd_banners:

            for widget in list(self.float_banners.children):

                if widget.seu_numero == 1:
                    # ajustar a posicao do widget para movelo
                    widget.pos = (self.tamnho_janela , self.pos[1])
                    widget.visivel = True
                    self.ultimo_visivel = True
                    self.visivel = False
                    #ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original
                    Clock.schedule_interval(self.meu_app.mover_banners, 1/30)
                    


        elif self.seu_numero != self.meu_app.qtd_banners and self.seu_numero != 1:
            for widget in list(self.float_banners.children):

                if widget.seu_numero == self.seu_numero + 1:
                    # ajustar a posicao do widget para movelo

                    widget.pos = (self.tamnho_janela, self.pos[1])

                    widget.visivel = True
                    self.ultimo_visivel = True
                    self.visivel = False
                    #ImageButtonCustomDois.velocidade_movimento = -self.velocidade_movimento_original
                    Clock.schedule_interval(self.meu_app.mover_banners, 1/30)
                            


    def mover_widget_automatico_intervalo(self):
        Clock.schedule_interval(self.mover_widget_automatico, 8)



