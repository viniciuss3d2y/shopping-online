from kivy.uix.floatlayout import FloatLayout
from botoes import ImageButton, ImageButtonCustom, AsyncImageButtonCustom
import io
from kivy.core.image import Image as coreImage
from kivy.graphics import Color,RoundedRectangle,Ellipse
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
import requests
import threading
from kivy.app import App
from functools import partial
from kivy.loader import Loader
#from loading import Loading

Loader.loading_image = "icones/placeholder2.png"


class BannerRoupasHomePage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__()

        self.extensao = kwargs["extensao"]
        #self.Byte_imagem_roupa = kwargs['byte_imagem_roupa']
        self.nome_produto = kwargs["nome_produto"]
        self.em_promocao = kwargs['em_promocao']
        self.porcentagem_promocao = kwargs['porcentagem_promocao']
        self.preco_normal = kwargs['preco_normal']
        self.favorito = kwargs['favorito']
        self.descricao = kwargs['descricao'].title()
        self.tamanhos_disponiveis = kwargs['tamanhos_disponiveis']
        self.url_AsyncImage = kwargs['url_AsyncImage']
        self.caminho_para_imagem_todas_cores = kwargs['caminho_para_imagem_todas_cores']

        self.meu_app = App.get_running_app()
        
        self.image = AsyncImageButtonCustom(pos_hint= {"center_x": 0.5, "top": 1},
                                size_hint= (1, 0.6), source = self.url_AsyncImage)

        with self.image.canvas.before:
            Color(rgba=get_color_from_hex("#f4f4f4"))
            self.rect = RoundedRectangle(pos = self.image.pos, size= self.image.size, radius=[2])
        self.bind(pos= self.atualizar_rect, size=self.atualizar_rect)        


        # label nome do produto
        self.texto_nome_produto = self.nome_produto.replace("_", " ").title()
        self.label_nome_produto = Label(text = "a",
                                         pos_hint= {"x": 0, "top": 0.35}, size_hint = (None, None),
                                         bold = True, font_size = '11sp',
                                        halign='left',  # Alinhamento horizontal do texto
                                        valign='middle',  # Alinhamento vertical do texto
                                        #text_size=(self.width, None)
                                        font_name = "sanchez/Sanchezregular.otf")
        self.label_nome_produto.color = get_color_from_hex("#34353a")
        self.label_nome_produto.max_lines= 1
        self.label_nome_produto.texture_update()
        # tamanho em pixel que cada letra ocupara
        self.tamanho_caractere= self.label_nome_produto.texture_size

        self.label_nome_produto.bind(size= self.update_text_size)


        self.image_coracao = ImageButton(source = "icones/favorito.png" if self.favorito else "icones/coracao.png",
                                         pos_hint= {"right": 0.9, "top": 0.97},
                                           size_hint = (None, None))
        self.image_coracao.on_press = self.on_click

        with self.image_coracao.canvas.before:
            Color(rgba=get_color_from_hex("#b3b2b2"))
            self.coracao_fundo = Ellipse(pos=self.image_coracao.pos, size=(self.image_coracao.size[0], self.image_coracao.size[0]))
        self.image_coracao.bind(pos=self.update_coracao_fundo , size= self.update_coracao_fundo)
        
        if self.em_promocao:
            # label preco promocao do produto
            self.texto_preco_promocao = float(self.preco_normal) * float(self.porcentagem_promocao)
            self.label_preco_promocao = Label(text = f'R${self.texto_preco_promocao:.2f}', 
                                     pos_hint= {"x": 0, "top": 0.22}, size_hint = (1, 0.1),
                                        bold = True, font_size = '14sp',
                                        halign='left',  # Alinhamento horizontal do texto
                                        valign='middle',  # Alinhamento vertical do texto
                                        color = get_color_from_hex("#f25c77"),
                                        font_name = "sanchez/Sanchezregular.otf")
            
            # label preco normal do produto  Texto rascunhado
            self.label_preco_normal = Label(text = f'[s]R${float(self.preco_normal):.2f}[/s]', 
                                        pos_hint= {"x": 0.65, "top": 0.22}, size_hint = (0.2, 0.1),
                                        bold = True, font_size = '11sp',
                                        halign='left',  # Alinhamento horizontal do texto
                                        valign='middle',  # Alinhamento vertical do texto
                                        color = get_color_from_hex("#8b8f92"), markup = True,
                                        font_name = "sanchez/Sanchezregular.otf")
            # funcao para quando a imagem é clicada
            self.image.on_release = partial(self.meu_app.ver_detalhes_produto,empromocao = True ,nome_produto= self.texto_nome_produto,
                                            preco_produto_normal = self.label_preco_normal.text,
                                            preco_produto_promocao = self.label_preco_promocao.text,
                                            #byte_image = self.Byte_imagem_roupa, extensao = self.extensao,
                                            descricao = self.descricao,
                                            tamanhos_disponiveis = self.tamanhos_disponiveis,
                                            #cores_disponiveis = self.cores_disponiveis,
                                            url_AsyncImage=self.url_AsyncImage,
                                            caminho_para_imagem_todas_cores= self.caminho_para_imagem_todas_cores)
            
            self.add_widget(self.label_preco_promocao)

        else:
            self.label_preco_normal = Label(text = f'R${self.preco_normal:.2f}', 
                            pos_hint= {"x": 0, "top": 0.22}, size_hint = (1, 0.1),
                            bold = True, font_size = '14sp',
                            halign='left',  # Alinhamento horizontal do texto
                            valign='middle',  # Alinhamento vertical do texto
                            color = get_color_from_hex("#424147"), markup = True,
                            font_name = "sanchez/Sanchezregular.otf")

            # funcao para quando a imagem é clicada
            self.image.on_release = partial(self.meu_app.ver_detalhes_produto,empromocao = False, nome_produto = self.texto_nome_produto,
                                    preco_produto_normal = self.label_preco_normal.text,
                                    #byte_image = self.Byte_imagem_roupa, extensao = self.extensao,
                                    descricao = self.descricao,
                                    tamanhos_disponiveis = self.tamanhos_disponiveis,
                                    #cores_disponiveis = self.cores_disponiveis,
                                    url_AsyncImage=self.url_AsyncImage,
                                    caminho_para_imagem_todas_cores= self.caminho_para_imagem_todas_cores)



        self.add_widget(self.label_preco_normal)
        self.add_widget(self.label_nome_produto)
        self.add_widget(self.image)
        self.add_widget(self.image_coracao)

    def atualizar_rect(self, *args):
        #self.label_nome_produto.pos_hint = {"x": 0, "top": 0.4}
        
        self.rect.size = (self.size[0], self.size[1]*0.6)
        self.rect.pos = (self.pos[0], self.pos[1] + self.size[1] - self.rect.size[1])

        self.image_coracao.size = (self.size[1]*0.1, self.size[1]*0.1)


        self.label_nome_produto.size = (self.rect.size[0], self.rect.size[1]*0.1)
        self.label_nome_produto.text_size = self.label_nome_produto.size 
        self.max_letras_texto()



    def max_letras_texto(self):
        max_caracteres = int(self.label_nome_produto.width/self.tamanho_caractere[0])

        if len(self.texto_nome_produto)> max_caracteres:
            nome_produto = self.texto_nome_produto[:max_caracteres-1]+"..."
            self.label_nome_produto.text = nome_produto

        else:
            self.label_nome_produto.text = self.texto_nome_produto
        
        
    
    def update_text_size(self, instance, value):

        self.label_nome_produto.text_size = value
        if self.em_promocao:
            self.label_preco_promocao.text_size = value
        else:
            self.label_preco_normal.text_size = value

    
    def update_coracao_fundo(self, *args):
        
        self.coracao_fundo.size = (self.image_coracao.size[0]*1.3, self.image_coracao.size[0]*1.3)
        self.coracao_fundo.pos = (self.image_coracao.pos[0]-(self.coracao_fundo.size[0]*0.1)
                                  , self.image_coracao.pos[1]-(self.coracao_fundo.size[0]*0.1))


    
    def on_click(self, *args):
        print(self.tamanho_caractere)
        if self.favorito:
            self.image_coracao.source = "icones/coracao.png"
            thread = threading.Thread(target=self.remover_favoritos_thread)
            thread.start()
            self.favorito = False

        else:
            self.favorito = True
            self.image_coracao.source = "icones/favorito.png"
            thread = threading.Thread(target=self.adicionar_favoritos_thread)
            thread.start()
  
    

    def remover_favoritos_thread(self):
        nome_produto_format = self.nome_produto.lower()
        requests.delete(f"https://appvendas-ae071-default-rtdb.firebaseio.com/users/{self.meu_app.local_id}/favoritos/{nome_produto_format}.json")       
    
    def adicionar_favoritos_thread(self):

        data = {self.nome_produto: ""}
        requests.patch(f"https://appvendas-ae071-default-rtdb.firebaseio.com/users/{self.meu_app.local_id}/favoritos.json",
                       json=data)  
    

    def desativar_loading(self, *args):
        self.remove_widget(self.loading)
    
    