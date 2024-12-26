from kivy.uix.widget import Widget
from kivy.graphics import Color,RoundedRectangle, Ellipse
from kivy.uix.button import ButtonBehavior
from kivy.utils import get_color_from_hex
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.properties import ObjectProperty


class BannerCor(ButtonBehavior, Widget):
    instancias = []
    cor_selecionada = ""
    def __init__(self, **kwargs):
        super().__init__()
        self.cols = 1
        
        self.numero = kwargs['numero']
        self.hex_cor = "#"+kwargs['cor']

        #self.image_core = kwargs['image_core']
        self.selecionado = False
        self.meu_app = App.get_running_app()


        self.detalhes_produtos_page = self.meu_app.root.ids["detalhesprodutopage"]
        conteiner_cores = self.detalhes_produtos_page.ids['conteiner_cores']

        
        self.size_hint = (0.33, 0.5)

        Window.bind(height=self.atualizar_valor_size_circulo)
        self.tamanho_circulo = (Window.height *0.1)* 0.5

        self.image =  Image(source="icones/selecionado.png")
        self.image.opacity = 0
        
        # adiciona esta instancia a lista de instancias
        

        with self.canvas.before:
            self.cor = Color(rgba= get_color_from_hex(self.hex_cor))
            self.circulo = Ellipse(pos=self.pos, size= (self.tamanho_circulo, self.tamanho_circulo), texture=None)
        self.bind(pos= self.update_rect , size=self.update_rect)

    
        self.on_press = self.on_click
        BannerCor.instancias.append(self)
        self.add_widget(self.image)


    def on_click(self, *args):

        if not self.selecionado :
            self.selecionado = True
            BannerCor.cor_selecionada = self.hex_cor

            self.image.opacity = 1
            for instancia in BannerCor.instancias:
                if instancia.numero != self.numero:
                    instancia.selecionado = False
                    instancia.image.opacity = 0

        elif self.selecionado :
            BannerCor.cor_selecionada = ""
            self.selecionado = False
            self.image.opacity = 0


    
    def update_rect(self, *args):
        self.circulo.size =  (self.tamanho_circulo, self.tamanho_circulo)
        self.circulo.pos = (self.pos[0], self.pos[1])

        # posicao imagem selecionado
        self.image.size = self.circulo.size
        self.image.pos = (self.pos[0], self.pos[1])
        


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


    

    def atualizar_valor_size_circulo(self, *args):
        self.tamanho_circulo = (Window.height *0.1)* 0.5

    
