from kivy.uix.widget import Widget
from kivy.graphics import Color,Line, Ellipse
from kivy.uix.button import ButtonBehavior
from kivy.utils import get_color_from_hex
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window


class BannerTamanhos(ButtonBehavior, Widget):
    instancias = []
    tamanho_selecionado = ""
    def __init__(self, **kwargs):
        super().__init__()

        self.tamanho = kwargs['tamanho']
        #self.raio = 12.5
        self.selecionado = False
        self.meu_app = App.get_running_app()
        self.numero = kwargs['numero']
        self.size_hint = (0.33, 0.5)

        self.raio = ((Window.height*0.1)*0.5) / 2
        Window.bind(height= self.atualizar_tamanho_raio)
        
        # adiciona esta istancia a lista de instancias
        

        self.on_press = self.on_click

        self.label = Label(text= self.tamanho.upper(),
                           color = (0, 0, 0, 1))                         
        self.label.pos = self.pos
        self.label.font_size = '10sp'

        with self.canvas.before:
            Color(rgba= (0, 0, 0, 1))
            self.circulo = Line(circle=(self.pos[0] + self.raio, self.pos[1]+ self.raio, self.raio), width=1)

        with self.canvas.before:
           self.cor = Color(rgba=(0, 0, 0, 0))
           self.circulo_click = Ellipse(pos=self.pos, size=(self.raio*2, self.raio*2))

        self.bind(size= self.atualizar_rect, pos= self.atualizar_rect)    

        BannerTamanhos.instancias.append(self)
        self.add_widget(self.label)

        

    def atualizar_rect(self, *args):#self.pos[0]+self.raio/2, self.pos[1]+self.raio/2
        self.circulo.circle = (self.pos[0]+self.raio, self.pos[1]+self.raio, self.raio)

        self.label.center_x = self.pos[0]+self.raio
        self.label.center_y = self.pos[1]+self.raio
        self.circulo_click.pos= self.pos
        self.circulo_click.size = (self.raio*2, self.raio*2)

    
    def on_click(self, *args):

        if not self.selecionado:
            self.cor.rgba = (0, 0, 0, 1)
            self.label.color = (1, 1, 1, 1)
            self.selecionado = True
            BannerTamanhos.tamanho_selecionado = self.tamanho
            for instancia in BannerTamanhos.instancias:
                if instancia.numero != self.numero:
                    instancia.cor.rgba = (0, 0, 0, 0)
                    instancia.selecionado = False 
                    instancia.label.color = (0, 0, 0, 1)
                         
        elif self.selecionado:
            BannerTamanhos.tamanho_selecionado = ""
            self.cor.rgba = (0, 0, 0, 0)
            self.label.color = (0, 0, 0, 1)
            self.selecionado = False


    def on_parent(self, *args):
        self.size_hint = (0.33, 0.5)
        
        if self.parent:

            if self.numero == 1:
                self.pos_hint = {"x":0, "top": 1}

            elif self.numero == 2:
                self.pos_hint = {"x":0.33, "top": 1}

            elif self.numero == 3:
                self.pos_hint = {"x":0.66, "top": 1}

            elif self.numero == 4:
                self.pos_hint = {"x":0, "top": 0.5}

            elif self.numero == 5:
                self.pos_hint = {"x":0.33, "top": 0.5}

            elif self.numero == 6:
                self.pos_hint = {"x":0.66, "top": 0.5}
    

    def atualizar_tamanho_raio(self, *args):
        self.raio = ((Window.height*0.1)*0.5) / 2
        #self.circulo.circle = (self.pos[0] + self.raio, self.pos[1]+ self.raio, self.raio/2)