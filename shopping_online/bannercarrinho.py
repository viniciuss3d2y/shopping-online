from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.gridlayout import MDGridLayout
from botoes import ImageButton, AsyncImageButtonCustom, LabelButton
from kivy.graphics import Color,RoundedRectangle
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label
from kivy.app import App
from functools import partial
from kivy.loader import Loader
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.button import MDTextButton
from kivy.metrics import dp


#from loading import Loading

Loader.loading_image = "icones/placeholder2.png"


class BannerCarrinho(FloatLayout, TouchBehavior):
    # preco total de somando todos produtos que o usuario selecionou

    preco_total_selecionado = 0
    def __init__(self, **kwargs):
        super().__init__()

        self.cor_produto = kwargs['cor_produto']
        self.tamanho_produto = kwargs['tamanho_produto']
        #self.Byte_imagem_roupa = kwargs['byte_imagem_roupa']
        self.nome_produto = kwargs["nome_produto"]
        self.em_promocao = kwargs['em_promocao']
        self.porcentagem_promocao = kwargs['porcentagem_promocao']
        self.preco_normal = kwargs['preco_normal']
        self.favorito = kwargs['favorito']
        self.descricao = kwargs['descricao'].title()
        self.tamanhos_disponiveis = kwargs['tamanhos_disponiveis']
        self.url_AsyncImage = kwargs['url_AsyncImage']
        # preco do produto 
        self.preco_produto = 0

        self.total_preco_produto = 0


        self.meu_app = App.get_running_app()
        
        self.image = AsyncImageButtonCustom(pos_hint= {"x": 0.1, "center_y": 0.5},
                                size_hint= (0.2, 0.75), source = self.url_AsyncImage)
        
        # quantidade do produto padrao
        self.quantidade = 0

        # label nome do produto
        self.texto_nome_produto = self.nome_produto.replace("_", " ").title()
        self.label_nome_produto = Label(text = "a",
                                        pos_hint= {"x": 0.35, "top": 0.8}, size_hint = (None, None),
                                        bold = True, font_size = '9sp',
                                        halign='left',  # Alinhamento horizontal do texto
                                        valign='middle',  # Alinhamento vertical do texto
                                        #text_size=(self.width, None)
                                        font_name = "sanchez/Sanchezregular.otf")
        self.label_nome_produto.color = get_color_from_hex("#34353a")
        self.label_nome_produto.max_lines= 1
        self.label_nome_produto.texture_update()
        # tamanho em pixel que cada letra ocupara
        self.tamanho_caractere= self.label_nome_produto.texture_size

        self.layout_tamanho = MDGridLayout(pos_hint= {"x": 0.7, "top": 0.6},
                                           size_hint=(None, None),
                                           size=(dp(18), dp(18)), cols=1)
        self.layout_tamanho.md_bg_color = get_color_from_hex("#9188e5")
        self.layout_tamanho.radius = [20, 20, 20, 20]
        self.label_tamanho = Label(text=self.tamanho_produto.upper(),  pos_hint= {"x": 0.55, "top": 0.35},
                                        color= (1, 1, 1, 1), font_size = '11sp')
        self.layout_tamanho.add_widget(self.label_tamanho)

        
        if self.em_promocao:
            # label preco promocao do produto
            self.texto_preco_promocao = float(self.preco_normal) * float(self.porcentagem_promocao)
            self.label_preco_promocao = Label(text = f"R${self.texto_preco_promocao:.2f}  [size=9sp][color=#8b8f92][s]R${self.preco_normal}[/s][/color][/size]", 
                                     pos_hint= {"x": 0.35, "top": 0.35}, size_hint = (None, None),
                                        bold = True, font_size = '11sp',
                                        halign='left',  # Alinhamento horizontal do texto
                                        valign='middle',  # Alinhamento vertical do texto
                                        color = get_color_from_hex("#f25c77"),
                                        font_name = "sanchez/Sanchezregular.otf",
                                        markup=True)
            
            self.preco_produto = self.texto_preco_promocao

            
            #preco_produto = f"[color=#f25c77]{preco_promocao}[/color] [size=10 sp][color=#8b8f92]{preco_normal}[/color][/size]"
            self.add_widget(self.label_preco_promocao)

        else:
            self.label_preco_normal = Label(text = f'R${self.preco_normal:.2f}', 
                            pos_hint= {"x": 0.35, "top": 0.35}, size_hint = (None, None),
                            bold = True, font_size = '11sp',
                            halign='left',  # Alinhamento horizontal do texto
                            valign='middle',  # Alinhamento vertical do texto
                            color = get_color_from_hex("#424147"), markup = True,
                            font_name = "sanchez/Sanchezregular.otf")
            
            self.preco_produto = self.preco_normal

            self.add_widget(self.label_preco_normal)



        # layout quantidade pra o usuario escolhge a quantidade
        self.conteiner_quantidade = GridLayout(
                        pos_hint = {"x": 0.9, "center_y": 0.5},
                         size_hint= (0.07, 0.9), cols = 1)
        with self.conteiner_quantidade.canvas.before:
            Color(rgba=get_color_from_hex("#9188e5"))
            self.rect_conteiner_quantidade = RoundedRectangle(pos=self.conteiner_quantidade.pos, size= self.conteiner_quantidade.size, radius=[5])
        self.conteiner_quantidade.bind(pos= self.atualizar_rect_quantidade, size= self.atualizar_rect_quantidade)
            


        self.label_quantidade = Label(text=str(self.quantidade), color=(0, 0, 0, 1))

        # aumenta a quantidade de intens
        self.image_mais = ImageButton(source="icones/mais.png", on_release = self.aumentar_quantidade)
        # with self.image_mais.canvas.before:
        #     Color(rgba= get_color_from_hex("#EAEAEA"))
        #     self.image_mais_rect = Rectangle(pos= self.image_mais.pos, size= self.size)

        # diminui a quantidade de intens
        
        self.image_menos = ImageButton(source="icones/menos.png", on_release=self.diminuir_quantidade)
        # with self.image_menos.canvas.before:
        #     Color(rgba= get_color_from_hex("#EAEAEA"))
        #     self.image_menos_rect = Rectangle(pos= self.image_menos.pos, size= self.size)
        # # ajusta a posicao dos canvas de quantidade quando o conteiner deles mudar de tamanho
        

        with self.canvas.before:
            Color(rgba=get_color_from_hex("#ffffff"))
            self.rect = RoundedRectangle(pos= self.pos, size= self.size, radius= [15])
        self.bind(pos= self.atualizar_rect, size= self.atualizar_rect)

        # selecionar os produtos no carrinho
        self.caixa_selecao = MDCheckbox(pos_hint = {"x":0 , "center_y": 0.8},
                                        size_hint = (None, None),
                                        size = ("45dp", "45dp"),
                                        on_release= self.on_click_caixa_selecao,
                                        )

        self.label_remover = LabelButton(text="Remover", font_size = '9sp',
                                            size_hint = (None, None),
                                            size = (dp(60), dp(10)),
                                          pos_hint = {"x":0.6 , "y": 1},
                                          color= get_color_from_hex("#f25c77"),
                                          halign = "center",
                                          valign = "middle",
                                          on_release= partial(self.meu_app.remover_produto_carrinho, nome_produto = self.nome_produto, cor_produto = self.cor_produto,
                                                              tamanho_produto = self.tamanho_produto))


        self.conteiner_quantidade.add_widget(self.image_mais)
        self.conteiner_quantidade.add_widget(self.label_quantidade)
        self.conteiner_quantidade.add_widget(self.image_menos)

        self.add_widget(self.layout_tamanho)
        self.add_widget(self.label_remover)
        self.add_widget(self.caixa_selecao)
        self.add_widget(self.conteiner_quantidade)
        self.add_widget(self.label_nome_produto)
        self.add_widget(self.image)




    def on_click_caixa_selecao(self, *args):

        if self.caixa_selecao.active:
            if self.quantidade <= 0:
                self.quantidade = 1
                self.label_quantidade.text = str(self.quantidade)

            self.total_preco_produto += self.preco_produto * self.quantidade
            #self.meu_app.root.ids["carrinhopage"].ids["label_total_carrinho"].text =  f'SubTotal: R${BannerCarrinho.preco_total_selecionado:.2f}'
            self.calcular_preco_produtos()
        
        else:
            self.quantidade = 0
            self.label_quantidade.text = str(self.quantidade)

            self.total_preco_produto = 0

            if BannerCarrinho.preco_total_selecionado < 0:
                BannerCarrinho.preco_total_selecionado = 0
            #self.meu_app.root.ids["carrinhopage"].ids["label_total_carrinho"].text =  f'SubTotal: R${BannerCarrinho.preco_total_selecionado:.2f}'
            self.calcular_preco_produtos()



    def calcular_preco_produtos(self):
        carrinho_page = self.meu_app.root.ids["carrinhopage"]
        total_preco_produtos = 0
        
        for instancia in list(carrinho_page.ids["scroll_carrinho"].children):
            total_preco_produtos += instancia.total_preco_produto

        BannerCarrinho.preco_total_selecionado= total_preco_produtos
        self.meu_app.root.ids["carrinhopage"].ids["label_total_carrinho"].text =  f'SubTotal: R${BannerCarrinho.preco_total_selecionado:.2f}'


    def atualizar_rect(self, *args):

        self.rect.pos = self.pos
        self.rect.size = self.size

        self.label_nome_produto.size = (self.size[0]*0.45, self.size[1]*0.15)
        self.label_nome_produto.text_size = self.label_nome_produto.size 
        self.max_letras_texto()
        self.update_text_size()



    def max_letras_texto(self):
        max_caracteres = int(self.label_nome_produto.width/self.tamanho_caractere[0])

        if len(self.texto_nome_produto)> max_caracteres:
            nome_produto = self.texto_nome_produto[:max_caracteres-1]+"..."
            self.label_nome_produto.text = nome_produto

        else:
            self.label_nome_produto.text = self.texto_nome_produto
        
        
    
    def update_text_size(self):


        self.label_nome_produto.text_size = self.label_nome_produto.size
        if self.em_promocao:
            self.label_preco_promocao.size = (self.size[0]*0.45, self.size[1]*0.15)
            self.label_preco_promocao.text_size = self.label_preco_promocao.size
        else:
            self.label_preco_normal.size = (self.size[0]*0.45, self.size[1]*0.15)
            self.label_preco_normal.text_size = self.label_preco_normal.size

 
    

    def desativar_loading(self, *args):
        self.remove_widget(self.loading)


    
    def atualizar_rect_quantidade(self, *args):

        self.rect_conteiner_quantidade.pos = self.conteiner_quantidade.pos
        self.rect_conteiner_quantidade.size = self.conteiner_quantidade.size


    def aumentar_quantidade(self, *args):

        quantidade_anterior = self.quantidade
        self.quantidade += 1
        self.label_quantidade.text = str(self.quantidade)

        if self.caixa_selecao.active:
            self.total_preco_produto -= self.preco_produto * quantidade_anterior
            self.total_preco_produto += self.preco_produto * self.quantidade
            #self.meu_app.root.ids["carrinhopage"].ids["label_total_carrinho"].text =  f'SubTotal: R${BannerCarrinho.preco_total_selecionado:.2f}'
            self.calcular_preco_produtos()

    def diminuir_quantidade(self, *args):
        if self.quantidade > 0:
            self.quantidade -= 1
            self.label_quantidade.text = str(self.quantidade)

            if self.caixa_selecao.active:
                self.total_preco_produto -= self.preco_produto
                #self.meu_app.root.ids["carrinhopage"].ids["label_total_carrinho"].text =  f'SubTotal: R${BannerCarrinho.preco_total_selecionado:.2f}'
                self.calcular_preco_produtos()