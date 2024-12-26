from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color,RoundedRectangle,Ellipse, Line
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label

from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.button import MDRaisedButton





class SliderFiltroPreco(CommonElevationBehavior, FloatLayout):
    posicao_esquerda_slide = None
    posicao_direita_slide = None

    largura_slider = None

    valor_minimo = 0
    valor_maximo = 1000

    valor_max_filtrado = valor_maximo
    valor_min_filtrado = valor_minimo

    lista_inst = []

    def __init__(self, conteiner = None, funcao_botao = None, conteiner_disabled = None, **kwargs):
        super().__init__(**kwargs)

        self.elevation= 6
        self.shadow_softness = 6

        self.conteiner = conteiner
        self.funcao_botao = funcao_botao
        self.conteiner_disabled = conteiner_disabled


        self.label = Label(text="FAIXA DE PREÇO", pos_hint = {"center_x":0.5, "top": 0.9},
                                                        size_hint = (0.8, 0.1), color= get_color_from_hex("#EAEAEA"), bold=True)


        with self.canvas:
            Color(rgba=get_color_from_hex("#FFFFFF"))
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[5]) 

        # slider principal fica entre os dois circulos
        with self.canvas:
            Color(rgba=(0, 0, 1, 1))
            self.barra_slider_rect = Line(points=[(Window.width*self.pos_hint["center_x"])-(self.width*0.4), Window.height*self.pos_hint["center_y"],
                                              (Window.width*self.pos_hint["center_x"])+(self.width*0.4), Window.height*self.pos_hint["center_y"]], width=2.5)

        # cor slider diferente fica a esquerda     
        with self.canvas:
            Color(rgba=get_color_from_hex("#EAEAEA"))
            self.slider_esquerda = Line(points=[(Window.width*self.pos_hint["center_x"])-(self.width*0.4), Window.height*self.pos_hint["center_y"],
                                              (Window.width*self.pos_hint["center_x"])+(self.width*0.4), Window.height*self.pos_hint["center_y"]], width=2.5)


        # cor slider diferente fica a direita  
        with self.canvas:
            Color(rgba=get_color_from_hex("#EAEAEA"))
            self.slider_direita = Line(points=[(Window.width*self.pos_hint["center_x"])-(self.width*0.4), Window.height*self.pos_hint["center_y"],
                                              (Window.width*self.pos_hint["center_x"])+(self.width*0.4), Window.height*self.pos_hint["center_y"]], width=2.5)
            
        # informacao da posicao da ponta esquerda do slide para nao deixar que o circulo va alem
        SliderFiltroPreco.posicao_esquerda_slide = (Window.width*self.pos_hint["center_x"])-(self.width*0.4)

        SliderFiltroPreco.posicao_direita_slide = (Window.width*self.pos_hint["center_x"])+(self.width*0.4)
        

        self.circulo_deslizante_min = CirculoDeslizanteMin(pos_hint = {"x":0.1, "center_y": 0.5},
                                                           size = (7, 7)
                                                           )
        self.circulo_deslizante_min.bind(pos = self.atualizar_slider_esquerda)
                    
        

        self.circulo_deslizante_max = CirculoDeslizanteMax(pos_hint = {"right": 0.9, "center_y": 0.5},
                                                           size = (7, 7)
                                                           )
        self.circulo_deslizante_max.bind(pos= self.atualizar_slider_direita)

        self.botao_filtrar = MDRaisedButton(pos_hint = {"center_x": 0.5, "top": 0.2},
                                                            #size_hint=(0.6, 0.1),
                                                             text="MOSTRAR RESULTADOS",
                                                            text_color= get_color_from_hex("FFFFFF"),
                                                            on_release= self.callback_botao, font_style="Button")
        
        self.bind(size= self.atualizar_rects, pos= self.atualizar_rects)  

        self.add_widget(self.label)
        self.add_widget(self.botao_filtrar)
        self.add_widget(self.circulo_deslizante_min)
        self.add_widget(self.circulo_deslizante_max)

        SliderFiltroPreco.lista_inst.append(self)

    def atualizar_rects(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        
        self.barra_slider_rect.points =  [(Window.width*self.pos_hint["center_x"])-(self.width*0.4), Window.height*self.pos_hint["center_y"],
                                        (Window.width*self.pos_hint["center_x"])+(self.width*0.4), Window.height*self.pos_hint["center_y"]]

        SliderFiltroPreco.posicao_esquerda_slide = (Window.width*self.pos_hint["center_x"])-(self.width*0.4)

        SliderFiltroPreco.posicao_direita_slide = (Window.width*self.pos_hint["center_x"])+(self.width*0.4)

        SliderFiltroPreco.largura_slider = self.width*0.8

        CirculoDeslizanteMin.posicao_x_circulo_min = SliderFiltroPreco.posicao_esquerda_slide
        CirculoDeslizanteMax.posicao_x_circulo_max = SliderFiltroPreco.posicao_direita_slide

        self.circulo_deslizante_max.size_hint = (None, None)
        self.circulo_deslizante_min.size_hint = (None, None)

       # self.circulo_deslizante_min_rect.size = (self.circulo_deslizante_min.size[1]*1.2, self.circulo_deslizante_min.size[1]*1.2)
        

    def on_touch_up(self, touch):

        if not self.collide_point(*touch.pos):
            self.conteiner.remove_widget(self)
            SliderFiltroPreco.lista_inst.clear()
            SliderFiltroPreco.valor_min_filtrado = SliderFiltroPreco.valor_minimo
            SliderFiltroPreco.valor_max_filtrado = SliderFiltroPreco.valor_maximo
            self.conteiner_disabled.disabled = False


        return super().on_touch_up(touch)

    def callback_botao(self, *args):
        self.conteiner.remove_widget(self)
        SliderFiltroPreco.lista_inst.clear()
        self.funcao_botao()

        SliderFiltroPreco.valor_min_filtrado = SliderFiltroPreco.valor_minimo
        SliderFiltroPreco.valor_max_filtrado = SliderFiltroPreco.valor_maximo

        

    def atualizar_slider_esquerda(self, instancia, valor):

        self.slider_esquerda.points = [(Window.width*self.pos_hint["center_x"])-(self.width*0.4), Window.height*self.pos_hint["center_y"],
                                              valor[0], Window.height*self.pos_hint["center_y"]]
        
    def atualizar_slider_direita(self, instancia, valor):
        self.slider_direita.points = [valor[0]+self.circulo_deslizante_max.size[0], Window.height*self.pos_hint["center_y"],
                                              (Window.width*self.pos_hint["center_x"])+(self.width*0.4), Window.height*self.pos_hint["center_y"]]
        



class CirculoDeslizanteMin(Widget):
    posicao_x_circulo_min = SliderFiltroPreco.posicao_esquerda_slide

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mover_circulo = False

        with self.canvas:
            Color(rgba=(0, 0, 1, 1))
            self.rect = Ellipse(pos=self.pos, size= self.size)
        self.bind(size= self.update_rect, pos= self.update_rect)


        self.label_preco_min = Label(text=f'R${"{:.2f}".format(SliderFiltroPreco.valor_min_filtrado)}',
                                 pos= self.pos, color=get_color_from_hex("#a0a5ab"), size = (65, 15), font_size='9sp')

        self.add_widget(self.label_preco_min)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.size = (12, 12)
        self.rect.size = self.size

        self.posicao_movimento_anterior = SliderFiltroPreco.posicao_esquerda_slide

        self.label_preco_min.pos = (self.pos[0] - self.label_preco_min.texture_size[0], self.pos[1]+20)
        
    
    def on_touch_move(self, touch):

        #self.pos[0] >= SliderFiltroPreco.posicao_esquerda_slide
        if self.mover_circulo and SliderFiltroPreco.valor_min_filtrado > SliderFiltroPreco.valor_minimo or self.mover_circulo and self.posicao_movimento_anterior < touch.pos[0]:
            if (CirculoDeslizanteMax.posicao_x_circulo_max - (self.size[0]/2)) >  touch.pos[0]:
                SliderFiltroPreco.valor_min_filtrado = SliderFiltroPreco.valor_minimo + ((self.pos[0]-SliderFiltroPreco.posicao_esquerda_slide)/SliderFiltroPreco.largura_slider*(SliderFiltroPreco.valor_maximo-SliderFiltroPreco.valor_minimo))
                
                
                self.pos = (touch.pos[0], self.pos[1])
                self.posicao_movimento_anterior = touch.pos[0]
                CirculoDeslizanteMin.posicao_x_circulo_min = self.pos[0]

                if SliderFiltroPreco.valor_min_filtrado < SliderFiltroPreco.valor_minimo:
                    SliderFiltroPreco.valor_min_filtrado = SliderFiltroPreco.valor_minimo
                
                self.label_preco_min.text = f'R${"{:.2f}".format(SliderFiltroPreco.valor_min_filtrado)}'
                self.label_preco_min.pos = (self.pos[0] - self.label_preco_min.texture_size[0], self.pos[1]+20)


        elif self.collide_point(*touch.pos):
 
            self.pos_hint = {}
            self.mover_circulo = True
  
        return super().on_touch_move(touch)
    
    def on_touch_up(self, touch):
        self.mover_circulo = False
        return super().on_touch_up(touch)





class CirculoDeslizanteMax(Widget):

    posicao_x_circulo_max = SliderFiltroPreco.posicao_direita_slide
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mover_circulo = False
        

        with self.canvas:
            Color(rgba=(0, 0, 1, 1))
            self.rect = Ellipse(pos=self.pos, size= self.size)
        self.bind(size= self.update_rect, pos= self.update_rect)


        self.label_preco_max = Label(text=f'R${"{:.2f}".format(SliderFiltroPreco.valor_max_filtrado)}',
                                 pos= self.pos, color=get_color_from_hex("#a0a5ab"),size = (65, 15), font_size='9sp')


        self.add_widget(self.label_preco_max)
    
    def update_rect(self, *args):
        self.size = (12, 12)
        self.rect.pos = self.pos
        self.rect.size = self.size
        
        self.posicao_movimento_anterior = SliderFiltroPreco.posicao_direita_slide

        self.label_preco_max.pos = (self.pos[0], self.pos[1]+20)

    
    def on_touch_move(self, touch):

        
        if self.mover_circulo and SliderFiltroPreco.valor_max_filtrado < SliderFiltroPreco.valor_maximo or self.mover_circulo and self.posicao_movimento_anterior > touch.pos[0]:
            if (CirculoDeslizanteMin.posicao_x_circulo_min + (self.size[0]/2)) <  touch.pos[0]:

                SliderFiltroPreco.valor_max_filtrado = SliderFiltroPreco.valor_minimo + ((self.pos[0]-SliderFiltroPreco.posicao_esquerda_slide)/SliderFiltroPreco.largura_slider*(SliderFiltroPreco.valor_maximo-SliderFiltroPreco.valor_minimo))
                
                self.pos = (touch.pos[0], self.pos[1])
                self.posicao_movimento_anterior = touch.pos[0]
                CirculoDeslizanteMax.posicao_x_circulo_max = self.pos[0]

                if SliderFiltroPreco.valor_max_filtrado > SliderFiltroPreco.valor_maximo:
                    SliderFiltroPreco.valor_max_filtrado = SliderFiltroPreco.valor_maximo

                self.label_preco_max.text = f'R${"{:.2f}".format(SliderFiltroPreco.valor_max_filtrado)}'
                self.label_preco_max.pos = (self.pos[0], self.pos[1]+20)
                
                        

        elif self.collide_point(*touch.pos):
 
            self.pos_hint = {}
            self.mover_circulo = True
  
        return super().on_touch_move(touch)
    
    def on_touch_up(self, touch):
        self.mover_circulo = False
        return super().on_touch_up(touch)
    
