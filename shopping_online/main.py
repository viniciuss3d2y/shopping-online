from kivymd.app import MDApp
from kivy.lang import Builder
import requests
import os
from telas import*
from botoes import AsyncImageButtonCustomDois
from botoeshomepage import BotoesHomePage
from banneroupashomepg import BannerRoupasHomePage
from myfirebase import MyFirebase
from banner_cartegoriahomepg import BannerCartegoriaHomePG
import io
from kivy.core.image import Image as coreImage
from kivy.clock import Clock
from bannercores import BannerCor
from bannertamanhos import BannerTamanhos
from urllib.parse import quote
from imagecarousel import ImageCarousel
#from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
#from kivymd.uix.list import OneLineListItem
import threading
import time
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.utils import get_color_from_hex
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color,RoundedRectangle
from kivy.uix.label import Label
from sliderfiltropreco import SliderFiltroPreco
from bannercarrinho import BannerCarrinho
#from kivymd.uix.scrollview import ScrollView, StiffScrollEffect
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarActionButton
from kivymd.uix.label import MDLabel
from iconecarrinho import IconeCarrinho
from bottomnavigation import BottomNavigation
from kivy.animation import Animation
from SV_stretch_effect import MDScrollViewStretch


main_kv ="""
#: import utils kivy.utils
#: include kv/homepage.kv
#: include kv/criarcontapage.kv
#: include kv/loginpage.kv
#: include kv/detalhesprodutopage.kv
#: include kv/carrinhopage.kv
#: include kv/produtoscategoriapage.kv
#: include kv/searchpage.kv



FloatLayout:
    canvas.before:
        Color:
            rgba: utils.get_color_from_hex("#FFFFFF")
        Rectangle:
            pos: self.pos
            size: self.size

    ScreenManager:
        id: ScreenManager

        LoginPage:
            name: "loginpage"
            id: loginpage
            
        CriarContaPage:
            name: "criarcontapage"
            id: criarcontapage

            
        HomePage:
            name: "homepage"
            id : homepage
        
        DetalhesProdutoPage:
            name : "detalhesprodutopage"
            id : detalhesprodutopage
        
        CarrinhoPage:
            name: "carrinhopage"
            id : carrinhopage
        
        ProdutosCategoriaPage:
            name: "produtoscategoriapage"
            id : produtoscategoriapage


        SearchPage:
            name: "searchpage"
            id: searchpage

    FloatLayout:
        id : conteiner_navigation           

<ContentClsCustom>
    canvas:
        Color:
            rgba: 1, 0, 0, 1
        
        Rectangle:
            pos: self.pos
            size: self.size

"""

BannerCartegoriaHomePG
# customisa o content cls do mddialog para poder adicionar txtfioeld
class ContentClsCustom(MDGridLayout):
    def __init__(self, *args, **kwargs):#*args, **kwargs
        super().__init__()
        self.rows = 1
    
        self.text_field = MDTextField(id = "search_text_field_min", hint_text = "min",
                                    # pos_hint = {"center_x":0.5, "top": 1},
                                    # size_hint = (0.2, None),
                                                            
                                    icon_left= "minus",
                                    mode= "rectangle",
                                    line_color_normal= get_color_from_hex("#a0a5ab"),
                                    line_color_focus= get_color_from_hex("#a0a5ab"),
                                    text_color_focus= get_color_from_hex("#a0a5ab"),
                                    icon_left_color_focus= get_color_from_hex("#a0a5ab"),
                                    hint_text_color_focus = get_color_from_hex("#a0a5ab"),

                                    helper_text= "Preço minimo desejado",
                                    helper_text_mode="persistent",

                                    max_text_length= 4,

                                    font_size= '20sp'
                                    )
        self.la = Label(text="peaiod")
        self.add_widget(self.text_field)
        self.add_widget(self.la)
            	
        with self.canvas:
            Color(rgba=(1, 0, 0, 1))
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[5]) 



        self.barra_slider = MDFloatLayout(pos_hint = {"center_x":0.5, "top": 1},
                                        size_hint = (1, 1))
        with self.barra_slider.canvas:
            Color(rgba=(1, 0, 1, 1))
            self.barra_slider_rect = RoundedRectangle(pos=self.barra_slider.pos, size=self.barra_slider.size, radius=[5])

        self.circulo_deslizante_min = Widget(pos_hint = {"x": 0, "center_y": 0.5},
                                            size_hint = (self.barra_slider.size[1], self.barra_slider.size[1]))
                    
        

        self.circulo_deslizante_max = Widget(pos_hint = {"right": 1, "center_y": 0.5},
                                            size = (self.circulo_deslizante_min.size[1], self.circulo_deslizante_min.size[1]))
        self.bind(size= self.atualizar_rects, pos= self.atualizar_rects)  
    
        self.add_widget(self.barra_slider)

    def atualizar_rects(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

        self.barra_slider_rect.pos = self.barra_slider.pos
        self.barra_slider_rect.size = self.barra_slider.size


class MainApp(MDApp): 
    myfirebase = MyFirebase()
    

    def build(self):
        #return Builder.load_file("main.kv")

        return Builder.load_string(main_kv)

        
    def on_start(self):
        self.cor_selecionada = False
        self.lista_todas_categorias = []
        self.myfirebase.trocar_token()
       # self.add_botoes_homepage()
        #self.add_banner_roupas()
        self.add_banner_categoria()
        self.adicionar_banners_promo_homepg()
        Clock.schedule_once(self.chamar_funcao_ativar_movimento_auto, 45)
        self.pegar_lista_deprodutos()
        #self.adicionar_banners_search_page()
        self.adicionar_bottom_navigation()

        self.search_page = self.root.ids["searchpage"]
        # text field da pagina de pesquisa
        self.text_field = self.search_page.ids["search_text_field"]
 

        self.chamr_funcao_pesquisar = time.time()
        #self.text_field.bind(text=self.verifica_chamar_pesquisa)
        
        self.text_field.bind(text=self.search_produto_teste)
        # requisicao para pegar todas as categorias presentes no nó "todos_produtos"
        # e minimizar o tempo pra procurar produtos
        requisicao = requests.get("https://appvendas-ae071-default-rtdb.firebaseio.com/todas_categorias.json")
        for categoria in requisicao.json():
            self.lista_todas_categorias.append(categoria)

        
        self.menu_search_page = MDDropdownMenu()
        self.dialog_filtrar_preco = None

    def adicionar_bottom_navigation(self):
        self.bottom_navigation = BottomNavigation(pos_hint = {"center_x":0.5, "top": 0.1},
                                       size_hint = (1, 0.1)#, id = "bottomnavigation"
                                       )
        #self.bottom_navigation.label_search.disabled = True
        #self.bottom_navigation.label_perfil.disabled = True

        self.root.ids["conteiner_navigation"].add_widget(self.bottom_navigation)

    def remover_navigation(self, id_tela):
        if not id_tela in BottomNavigation.lista_paginas_conter_navigation:
            self.root.ids["conteiner_navigation"].remove_widget(self.bottom_navigation)
        
        else:
            if not self.bottom_navigation.parent:
                self.root.ids["conteiner_navigation"].add_widget(self.bottom_navigation)



    def verifica_chamar_pesquisa(self, instacia, value):

            if (time.time() - self.chamr_funcao_pesquisar) >= 0.5:
                
                Clock.unschedule(self.criar_banner_search_page)
                self.search_produto_thread(instacia, value)
            
                self.chamr_funcao_pesquisar = time.time()

    def adicionar_icone_carrinho(self):
        icone_carrinho_homepg = IconeCarrinho(pos_hint = {"x":0.85, "top": 1},
                                       size_hint = (0.07, 0.05))
        icone_carrinho_detalhespg = IconeCarrinho(pos_hint = {"x":0.85, "top": 1},
                                       size_hint = (0.07, 0.05))

        self.root.ids["detalhesprodutopage"].ids["conteiner_principal"].add_widget(icone_carrinho_detalhespg)
        self.root.ids["homepage"].ids["conteiner_principal"].add_widget(icone_carrinho_homepg)

    
    def mudar_tela(self, id_tela, *args, dt=0): 

        screen_manager = self.root.ids["ScreenManager"]

        if screen_manager.current == "detalhesprodutopage":
            BannerTamanhos.tamanho_selecionado = ""
            BannerCor.cor_selecionada = ""


        screen_manager.current = id_tela
        
        if id_tela == "searchpage" or id_tela == "homepage":
            with open("mudar_qual_pagina.txt", "w") as file:
                file.write(id_tela)
        
        if id_tela == "homepage":
            
            for instancia in BottomNavigation.lista_instacias:
                instancia.icon_home.disabled = False
                instancia.label_home.disabled = False

                instancia.icon_search.disabled = True
                instancia.label_search.disabled = True

                instancia.icon_perfil.disabled = True
                instancia.label_perfil.disabled = True
        
        self.remover_navigation(id_tela)

    def sair_carrinho_page(self):
        BannerCarrinho.preco_total_selecionado = 0
        self.root.ids["carrinhopage"].ids["label_total_carrinho"].text = f'SubTotal: R${BannerCarrinho.preco_total_selecionado:.2f}'
        self.mudar_tela("homepage")

        for instancia in BottomNavigation.lista_instacias:
            instancia.icon_home.disabled = False
            instancia.icon_search.disabled = True
            instancia.icon_perfil.disabled = True

    # verifica qual pagina anterior e volta pra ela
    def sair_page_detalhes_produtos(self):
        with open("mudar_qual_pagina.txt", "r")as file:
            conteudo = file.read()
        
        self.mudar_tela(conteudo)

    
    def on_tab(self,*args):
        self.mudar_tela()


    def add_botoes_homepage(self):
        homepage = self.root.ids["homepage"]
        botoes = BotoesHomePage()
        homepage.ids["conteiner_principal"].add_widget(botoes)
    
    def add_banner_roupas(self):
        bucket_name = "appvendas-ae071.appspot.com"
        homepage = self.root.ids["homepage"]
        URL_DATA_BASE = "https://appvendas-ae071-default-rtdb.firebaseio.com"

        requisicao_produtos_sele = requests.get(f"{URL_DATA_BASE}/users/{self.local_id}.json")
        requisicao_dic = requisicao_produtos_sele.json()
        # lista de produtos selecionados como favorito pelo usuario para ser usado em outras partes do codigo tambem

        self.lista_favoritos = []
        try:
           for nome_item in  requisicao_dic['favoritos']:
               self.lista_favoritos.append(nome_item)
        except:
            pass

        for caminho_produto in requisicao_dic['produtos_selecionados']:
            # converte codigo da barra "%2F"(usado no firebase storage) para a propria barra para "/" usado do real time data base
            caminho_produto_RTDB = caminho_produto.replace("%2F", "/")
            # converte espaco para o codigo "%20"
            caminho_produto_RTDB = caminho_produto_RTDB.replace(" ", "%20")
            # pega o produto
            requisicao_produto = requests.get(f"{URL_DATA_BASE}/{caminho_produto_RTDB}.json")
            requisicao_produto_dic = requisicao_produto.json()

            # nome o produto
            nome_produto = os.path.basename(caminho_produto_RTDB)
            isfavorito = nome_produto in self.lista_favoritos

            requisicao_descricao = requests.get(f"{URL_DATA_BASE}/{caminho_produto_RTDB}/descricao.json")
            descricao = requisicao_descricao.json()
            if requisicao_produto.ok:
                # codifica a barra para buscar a imagem no storage
                                                                        # .replace("/", "%2F")
                caminho_para_imagem_principal = requisicao_produto_dic['cores']['imagem_principal']
                # todas as cores diferentes do item
                caminho_para_imagem_todas_cores = requisicao_produto_dic['cores']
                #byte_imagem = requests.get(f"https://firebasestorage.googleapis.com/v0/b/{bucket_name}/o/categorias%2F{caminho_para_imagem_principal}?alt=media")

                # codificar url
                url_codificada = quote(caminho_para_imagem_principal, safe=":.?=&")

                _, extensao_arquivo = os.path.splitext(caminho_para_imagem_principal)
                Banner_roupas_homapg = BannerRoupasHomePage( 
                                                            extensao = extensao_arquivo, nome_produto = nome_produto.replace("%20", " "),
                                                            em_promocao = requisicao_produto_dic['em_promocao'],
                                                            porcentagem_promocao = requisicao_produto_dic['porcentagem_promocao'],
                                                            preco_normal = requisicao_produto_dic['preco_normal'], 
                                                             favorito = isfavorito, descricao = descricao,
                                                            #cores_disponiveis = requisicao_produto_dic['cores'],
                                                            tamanhos_disponiveis = requisicao_produto_dic['tamanhos'],
                                url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{bucket_name}/o/categorias%2F{url_codificada}?alt=media",
                                caminho_para_imagem_todas_cores = caminho_para_imagem_todas_cores)

                homepage.ids["scroll_roupas"].add_widget(Banner_roupas_homapg)
                

        
    def add_banner_categoria(self):
        URL_BUCKET_STORAGE = "appvendas-ae071.appspot.com"
        homepage = self.root.ids["homepage"]
        requisicao = requests.get(f"https://firebasestorage.googleapis.com/v0/b/{URL_BUCKET_STORAGE}/o?prefix=fotos_categoria/")
        requisicao_dic = requisicao.json()

        for item in requisicao_dic['items']:
            caminho_imagem = item['name']
            caminho_imagem_codificado = quote(caminho_imagem, safe=":.?=&")
            nome_arquivo = os.path.basename(item['name'])
            nome_categoria, _ = os.path.splitext(nome_arquivo)
        
            url_asyncimage = f"https://firebasestorage.googleapis.com/v0/b/{URL_BUCKET_STORAGE}/o/{caminho_imagem_codificado}?alt=media"
            
            

            banner_categoria = BannerCartegoriaHomePG(
                                                      url_asyncimage = url_asyncimage,
                                                      nome_categoria = nome_categoria)
            homepage.ids["scroll_cartegoria"].add_widget(banner_categoria)


    def add_imagem_promocao(self):
        homepage = self.root.ids["homepage"]
        BUCKET = "appvendas-ae071.appspot.com"
        requisicao = requests.get(f"https://firebasestorage.googleapis.com/v0/b/{BUCKET}/o/fotos_promocao_homepage%2FDesign sem nome.png?alt=media")
        
        data = io.BytesIO(requisicao.content)

        image_core = coreImage(data, ext="png")

        homepage.ids["image_promo"].texture = image_core.texture


    def adicionar_banners_promo_homepg(self):
        BUCKET = "appvendas-ae071.appspot.com"
        requisicao_fotos = requests.get(f"https://firebasestorage.googleapis.com/v0/b/{BUCKET}/o?prefix=fotos_promocao_homepage/")
        requisicao_dic = requisicao_fotos.json()
        homepage = self.root.ids["homepage"]
        self.qtd_banners = 0
        for item in requisicao_dic['items']:
            self.qtd_banners += 1
            caminho_arquivo = item['name']
            #caminho_storage = caminho_arquivo.replace("/", "%2F")
            #caminho_storage = caminho_storage.replace(" ", "%20")
            _, extensao = os.path.splitext(caminho_arquivo)

            # codificar url
            url_codificada = quote(caminho_arquivo, safe=":.?=&")


            self.image_promo = AsyncImageButtonCustomDois(size_hint=(1, 1), seu_numero= self.qtd_banners, 
                                        source=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET}/o/{url_codificada}?alt=media")
            #self.image_promo.texture = core_image.texture
             
            if self.qtd_banners == 1 :
                self.image_promo.visivel = True
            else:
                self.image_promo.visivel = False
            
            
            homepage.ids["float_banners"].add_widget(self.image_promo)



    def mover_banners(self, dt):

        homepage = self.root.ids["homepage"]
        float_banners = homepage.ids["float_banners"]

        for widget in list(float_banners.children):
            
            if widget.visivel:
                AsyncImageButtonCustomDois.pode_mover = False
                widget.pos = (widget.pos[0]+ (AsyncImageButtonCustomDois.velocidade_movimento * dt), widget.pos[1])

                if widget.pos[0] >= widget.tamnho_janela - widget.width and widget.pos[0] <= widget.tamnho_janela - widget.width + 5:
                    widget.pos = ((widget.tamnho_janela/2) - (widget.width / 2), widget.pos[1])
                
                    AsyncImageButtonCustomDois.pode_mover = True
                    Clock.unschedule(self.mover_banners)
                    for widget in list(float_banners.children):
                        widget.ultimo_visivel = False
                        widget.ativar_movimento_auto = False
                        if not widget.visivel:
                            widget.pos = (widget.tamnho_janela*1.2, widget.pos[1])
            
            elif widget.ultimo_visivel:
                widget.pos = (widget.pos[0]+ (AsyncImageButtonCustomDois.velocidade_movimento * dt), widget.pos[1])


    

    def ativar_movimento_auto(self, dt):
        homepage = self.root.ids["homepage"]
        float_banners = homepage.ids["float_banners"]

        for widget in list(float_banners.children):
            if widget.visivel:
                widget.mover_widget_automatico()
                break

    def chamar_funcao_ativar_movimento_auto(self, dt):
        Clock.schedule_interval(self.ativar_movimento_auto, 12)

    

    def ver_detalhes_produto(self, **kwargs):

        detalhes_produto_page = self.root.ids["detalhesprodutopage"]
        # excluir os widgets de cores antigos
        for widget_cor in list(detalhes_produto_page.ids['conteiner_cores'].children):
            detalhes_produto_page.ids['conteiner_cores'].remove_widget(widget_cor)
        # excluir os widgets de tamanhos antigos
        for widget_tamanho in list(detalhes_produto_page.ids['conteiner_tamanhos'].children):
            detalhes_produto_page.ids['conteiner_tamanhos'].remove_widget(widget_tamanho)
        
        # exclui as imagens anteriores no carrossel
        detalhes_produto_page.ids['carousel'].clear_widgets()
           

        # texture da imagem que aparece quando seleciona a cor 
        with open("icones/selecionado.png", "rb") as bin_file:
            bin_content = bin_file.read()

        # dicionario conntendo o caminho para a imagem de todas as cores diferentes do mesmo item
        caminhos_para_imagem_todas_cores = kwargs['caminho_para_imagem_todas_cores']
        # adiciona o banner de cores e a imagem correspondendte ao carrossel
        # bucket storage
        BUCKET_NAME = "appvendas-ae071.appspot.com"
        numero_cor = 0
        for cor in caminhos_para_imagem_todas_cores:

            if cor != 'imagem_principal':
                # numero de identificacao da cor
                numero_cor += 1
                # limitar a quantidade de cores
                if numero_cor > 6:
                    break
                banner_cor = BannerCor(cor = cor,
                                    numero = numero_cor)           
                detalhes_produto_page.ids['conteiner_cores'].add_widget(banner_cor)


                url = caminhos_para_imagem_todas_cores[cor]
                # codifica a url
                url_codificada = quote(url, safe=":.?=&")
                url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_NAME}/o/categorias%2F{url_codificada}?alt=media"
                # cria a imagem no carrossel
                image_carousel = ImageCarousel(url_asyncimage = url_AsyncImage)
                # adiciona
                detalhes_produto_page.ids['carousel'].add_widget(image_carousel)
            

        nome_produto = kwargs['nome_produto']
        detalhes_produto_page.ids['nome_produto'].text = nome_produto
        detalhes_produto_page.ids['descricao_produto'].text = kwargs['descricao']


        if kwargs['empromocao']:
            preco_normal = kwargs['preco_produto_normal']
            preco_promocao = kwargs['preco_produto_promocao']
            preco_produto = f"[color=#f25c77]{preco_promocao}[/color] [size=10 sp][color=#8b8f92]{preco_normal}[/color][/size]"
            detalhes_produto_page.ids['preco_produto'].text = preco_produto
        
        else:
            detalhes_produto_page.ids['preco_produto'].text = kwargs['preco_produto_normal']

        numero_tamanho = 0
        for tamanho in kwargs['tamanhos_disponiveis']:
            numero_tamanho += 1
            banner_tamanho = BannerTamanhos(tamanho = tamanho,
                                            numero = numero_tamanho)

            detalhes_produto_page.ids['conteiner_tamanhos'].add_widget(banner_tamanho)

        self.mudar_tela("detalhesprodutopage")


    def adicionar_produto_carrinho(self):
        detalhes_page = self.root.ids["detalhesprodutopage"]
        nome_produto = detalhes_page.ids["nome_produto"].text.lower()

        if BannerTamanhos.tamanho_selecionado != "" and BannerCor.cor_selecionada != "" and nome_produto != "":
            
            # salva o produto no bd
            info = {f"{nome_produto}":
                    {"cor":BannerCor.cor_selecionada,
                     "tamanho": BannerTamanhos.tamanho_selecionado}}
            requests.post(f"https://appvendas-ae071-default-rtdb.firebaseio.com/users/{self.local_id}/carrinho.json",
                           json=info)
            Clock.schedule_once(lambda dt:self.mostrar_snackbar_carrinho())

            for produto in IconeCarrinho.lista_instancia:
                produto.badge.text = str(int(produto.badge.text) + 1)

        
        if  not BannerTamanhos.tamanho_selecionado:
            anim = Animation(md_bg_color = (1, 0, 0, 0.1)) + Animation(md_bg_color = (1, 0, 0, 0), duration=0.09)
            anim.start(detalhes_page.ids["conteiner_tamanhos"])

        if not BannerCor.cor_selecionada:
            anim = Animation(md_bg_color = (1, 0, 0, 0.1)) + Animation(md_bg_color = (1, 0, 0, 0), duration=0.09)
            anim.start(detalhes_page.ids["conteiner_cores"])


    
    def adicionar_produto_carrinho_thread(self):
        thread = threading.Thread(target=self.adicionar_produto_carrinho)
        thread.start()


    def mostrar_snackbar_carrinho(self):
        label = MDLabel(
            text="Item adicionado ao carrinho!",
            font_style="Overline",  # Ajuste o tamanho da fonte aqui
            text_color = get_color_from_hex("#737bbb")
        )
        snackbar = MDSnackbar(
            label,
            MDSnackbarActionButton(
            text="Fechar",
            on_release= lambda x: snackbar.dismiss(),
            ),
            pos_hint={"center_x": 0.5, "y": 0.04},
            md_bg_color="#FFFFFF",
            duration = 1.5

        )

        snackbar.open()        


    # busca todos produtos salvos no carrinho do usuario
    def quantidade_produtos_no_carrinho(self):
        requisicao_produtos_carrinho = requests.get(f"https://appvendas-ae071-default-rtdb.firebaseio.com/users/{self.local_id}/carrinho.json")
        dict_todos_produtos_carrinho = requisicao_produtos_carrinho.json()

        quantidade_produtos = 0
        if dict_todos_produtos_carrinho:
            for produto in dict_todos_produtos_carrinho:
                quantidade_produtos += 1
        
        for icone_carrinho in IconeCarrinho.lista_instancia:
            icone_carrinho.badge.text = str(quantidade_produtos)


        

       
    def ver_produtos_carrinho(self, *args):

        requisicao_peodutos_carrinho = requests.get(f"https://appvendas-ae071-default-rtdb.firebaseio.com/users/{self.local_id}/carrinho.json") 
        todos_produtos_carrinho_dict = requisicao_peodutos_carrinho.json() 

        if not todos_produtos_carrinho_dict:
            todos_produtos_carrinho_dict = {}

        BUCKET_NAME = "appvendas-ae071.appspot.com"

       # if BannerTamanhos.tamanho_selecionado != "" and BannerCor.cor_selecionada != "" and nome_produto != "":
        carrinho_page = self.root.ids["carrinhopage"]

        carrinho_page.ids["scroll_carrinho"].clear_widgets()
        # se o usuario nao tiver nenhum produto no carrinho mostra uma imagem 
        adicionar_imagem_carrinho_vazio = True

        requisicao = requests.get("https://appvendas-ae071-default-rtdb.firebaseio.com/todos_produtos.json")
        requisicao_dict = requisicao.json()
        # codigo hex da cor do produto seleciodo pelo usuario

        #if nome_produto in self.lista_todos_produtos:
        
        for id_produto in todos_produtos_carrinho_dict:
            for produto in todos_produtos_carrinho_dict[id_produto]:
                nome_produto = produto.lower()
                hex_cor_sele = todos_produtos_carrinho_dict[id_produto][produto]["cor"].lstrip("#")
                tamanho_sele = todos_produtos_carrinho_dict[id_produto][produto]["tamanho"].lower()

                for categoria in requisicao_dict:
                    if nome_produto in requisicao_dict[categoria]:

                        carrinho_page.ids["botao_finalizar_compra"].opacity = 1
                        carrinho_page.ids["label_total_carrinho"].opacity = 1
                        carrinho_page.ids["carrinho_vazio"].opacity = 0
                        adicionar_imagem_carrinho_vazio = False
                        # imagem da cor escolhida pelo usuario
                        url_para_imagem = requisicao_dict[categoria][nome_produto]['cores'][hex_cor_sele]  
                        # codifica a url para image para um formatro que o storage aceita
                        url_para_imagem_codificada = quote(url_para_imagem, safe=":.?=&")
                            

                        isfavorito = nome_produto in self.lista_favoritos
        
                        banner_carrinho = BannerCarrinho(nome_produto = nome_produto.replace("%20", " "),
                                                                        tamanho_produto = tamanho_sele,
                                                                        cor_produto = hex_cor_sele,
                                                                        em_promocao = requisicao_dict[categoria][nome_produto]['em_promocao'],
                                                                        porcentagem_promocao = requisicao_dict[categoria][nome_produto]['porcentagem_promocao'],
                                                                        preco_normal = requisicao_dict[categoria][nome_produto]['preco_normal'], 
                                                                        favorito = isfavorito, descricao = requisicao_dict[categoria][nome_produto]["descricao"],
                                                                        #cores_disponiveis = requisicao_produto_dic['cores'],
                                                                        tamanhos_disponiveis = requisicao_dict[categoria][nome_produto]['tamanhos'],
                                                                        
                                            url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_NAME}/o/categorias%2F{url_para_imagem_codificada}?alt=media")

                        carrinho_page.ids["scroll_carrinho"].add_widget(banner_carrinho)

                        break

        if adicionar_imagem_carrinho_vazio:
            
            carrinho_page.ids["carrinho_vazio"].source = "https://firebasestorage.googleapis.com/v0/b/appvendas-ae071.appspot.com/o/icones%2Fcarrinho-vazio.png?alt=media"
            carrinho_page.ids["carrinho_vazio"].opacity = 1

            carrinho_page.ids["botao_finalizar_compra"].opacity = 0
            carrinho_page.ids["label_total_carrinho"].opacity = 0
            

        self.mudar_tela("carrinhopage")

    def remover_produto_carrinho(self, *args, nome_produto=None, cor_produto = None, tamanho_produto=None):
        carrinho_page = self.root.ids["carrinhopage"]

        nome_produto = nome_produto.lower()
        cor_produto = "#"+ cor_produto

        requisicao = requests.get(f"https://appvendas-ae071-default-rtdb.firebaseio.com/users/{self.local_id}/carrinho.json")
        requisicao_dic = requisicao.json()
        for id_produto in requisicao_dic:
            if nome_produto in requisicao_dic[id_produto]:
                if cor_produto == requisicao_dic[id_produto][nome_produto]["cor"]:
                    if tamanho_produto.lower() == requisicao_dic[id_produto][nome_produto]["tamanho"]:
                    
                        requests.delete(f"https://appvendas-ae071-default-rtdb.firebaseio.com/users/{self.local_id}/carrinho/{id_produto}/{nome_produto}.json")    
                        break
                    
        
        for widget in list(carrinho_page.ids["scroll_carrinho"].children):
            if widget.nome_produto.lower() == nome_produto and widget.cor_produto.lstrip('#') == cor_produto.lstrip('#') and widget.tamanho_produto.lower() == tamanho_produto.lower():
                carrinho_page.ids["scroll_carrinho"].remove_widget(widget)
                break

        quantidade_produtos_no_carrinho = 0
        # apos remover porduto do carrinho ve quantos iten tem no carrinho    
        for widget in list(carrinho_page.ids["scroll_carrinho"].children):
            quantidade_produtos_no_carrinho += 1
        
        # mostra a quantidade de produtos no carrinho 
        for icone in IconeCarrinho.lista_instancia:
            icone.badge.text = str(quantidade_produtos_no_carrinho)

        # recalcula o preco de todos produtos selecionados
        total_preco_produtos = 0
        for instancia in list(carrinho_page.ids["scroll_carrinho"].children):
            
            total_preco_produtos += instancia.total_preco_produto

        BannerCarrinho.preco_total_selecionado = total_preco_produtos
        self.root.ids["carrinhopage"].ids["label_total_carrinho"].text =  f'SubTotal: R${BannerCarrinho.preco_total_selecionado:.2f}'



        label = MDLabel(
            text="Produto Removido Com Sucesso!",
            font_style="Overline",  # Ajuste o tamanho da fonte aqui
            text_color = get_color_from_hex("#737bbb")
        )
        snackbar = MDSnackbar(
            label,
            MDSnackbarActionButton(
            text="Fechar",
            on_release= lambda x: snackbar.dismiss(),
            ),
            pos_hint={"center_x": 0.5, "y": 0.04},
            md_bg_color="#FFFFFF",
            duration = 1.5
        )


        snackbar.open()

    # daesativa para evitar de duplicar os produtos com double click
    def desativar_homepage(self):
        self.root.ids["homepage"].disabled = True
    def ativar_homepage(self):
        self.root.ids["homepage"].disabled = False

    def ver_produtos_categoria(self, *args, **kwargs):
        
        
        Clock.schedule_once(lambda dt:self.desativar_homepage())

        produtos_categoria_page = self.root.ids["produtoscategoriapage"]
        nome_categoria = kwargs['nome_categoria']
        requisicao = requests.get(f"https://appvendas-ae071-default-rtdb.firebaseio.com/categorias/{nome_categoria}.json")
        requisicao_dic = requisicao.json()

        # excluir widgets anteriores
        Clock.schedule_once(lambda dt:produtos_categoria_page.ids["scroll_produtos"].clear_widgets())
        
        BUCKET_NAME = "appvendas-ae071.appspot.com"
        if requisicao.ok:
            for sub_categoria in requisicao_dic:
                for produto in requisicao_dic[sub_categoria]:
                    nome_produto = produto
                    isfavorito = nome_produto in self.lista_favoritos
                    referencia = requisicao_dic[sub_categoria][produto]['referencia'].replace("%2F", "/")
                    
                    requisicao_produto = requests.get(f"https://appvendas-ae071-default-rtdb.firebaseio.com/{referencia}.json")
                    requisicao_produto_dic = requisicao_produto.json()

                    _,extensao = os.path.splitext(requisicao_produto_dic['cores']['imagem_principal'])
                    caminho_byte_image = requisicao_produto_dic['cores']['imagem_principal']#.replace("/", "%2F")
                    # codificar caminho para imagem no storage
                    caminho_byte_image_codificado = quote(caminho_byte_image, safe=".=&:?")
                    #caminho_byte_image = caminho_byte_image.replace(" ", "%20")
    
                    # banner = BannerRoupasHomePage( 
                    #                             extensao = extensao, nome_produto = nome_produto.replace("%20", " "),
                    #                             em_promocao = requisicao_produto_dic['em_promocao'],
                    #                             porcentagem_promocao = requisicao_produto_dic['porcentagem_promocao'],
                    #                             preco_normal = requisicao_produto_dic['preco_normal'], 
                    #                             favorito = isfavorito, descricao = requisicao_produto_dic['descricao'],
                    #                             caminho_para_imagem_todas_cores = requisicao_produto_dic['cores'],
                    #                             tamanhos_disponiveis = requisicao_produto_dic['tamanhos'],
                    #         url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_NAME}/o/categorias%2F{caminho_byte_image_codificado}?alt=media"
                    #                             )
                    
                    # produtos_categoria_page.ids["scroll_produtos"].add_widget(banner)
                    Clock.schedule_once(lambda dt:self.adicionar_banner( extensao = extensao, nome_produto = nome_produto.replace("%20", " "),
                                                em_promocao = requisicao_produto_dic['em_promocao'],
                                                porcentagem_promocao = requisicao_produto_dic['porcentagem_promocao'],
                                                preco_normal = requisicao_produto_dic['preco_normal'], 
                                                favorito = isfavorito, descricao = requisicao_produto_dic['descricao'],
                                                caminho_para_imagem_todas_cores = requisicao_produto_dic['cores'],
                                                tamanhos_disponiveis = requisicao_produto_dic['tamanhos'],
                            url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_NAME}/o/categorias%2F{caminho_byte_image_codificado}?alt=media"),0)
                
            Clock.schedule_once(lambda dt: self.mudar_tela("produtoscategoriapage"))
        Clock.schedule_once(lambda dt: self.ativar_homepage())

    def ver_produtos_categoria_thread(self, *args, **kwargs):
        thread = threading.Thread(target= self.ver_produtos_categoria, args=args, kwargs=kwargs)
        thread.start()
    # funcao para adicionar o banner dos produtos na categoria pq so e possivel add pela thread principal
    def adicionar_banner(self, dt=0, **kwargs):
        produtos_categoria_page = self.root.ids["produtoscategoriapage"]

        BUCKET_NAME = "appvendas-ae071.appspot.com"
        extensao = kwargs["extensao"]
        nome_produto = kwargs["nome_produto"]
        em_promocao = kwargs['em_promocao']
        porcentagem_promocao = kwargs['porcentagem_promocao']
        preco_normal = kwargs['preco_normal']
        favorito = kwargs['favorito']
        descricao = kwargs['descricao']
        caminho_para_imagem_todas_cores = kwargs['caminho_para_imagem_todas_cores']
        tamanhos_disponiveis = kwargs['tamanhos_disponiveis']
        url_AsyncImage= kwargs['url_AsyncImage']
        #caminho_byte_image_codificado = kwargs["caminho_byte_image_codificado"]

        banner = BannerRoupasHomePage( 
                                    extensao = extensao, nome_produto = nome_produto.replace("%20", " "),
                                    em_promocao = em_promocao,
                                    porcentagem_promocao = porcentagem_promocao,
                                    preco_normal = preco_normal, 
                                    favorito = favorito, descricao = descricao,
                                    caminho_para_imagem_todas_cores = caminho_para_imagem_todas_cores,
                                    tamanhos_disponiveis = tamanhos_disponiveis,
                url_AsyncImage=url_AsyncImage
                                    )
        produtos_categoria_page.ids["scroll_produtos"].add_widget(banner)


    def pegar_lista_deprodutos(self):

        # pega o nome de todos produtos listados 
        requisicao = requests.get("https://appvendas-ae071-default-rtdb.firebaseio.com/search_todos_produtos.json")
        requisicao_dic = requisicao.json()
        self.lista_todos_produtos = []
        for produto in requisicao_dic:
            self.lista_todos_produtos.append(produto)




    def adicionar_banners_search_page(self):

        # quando entrar na pagina carrega todos os produtos
        URL_RTDB = "https://appvendas-ae071-default-rtdb.firebaseio.com"
        requisicao_todos_itens = requests.get(f"{URL_RTDB}/todos_produtos.json")
        requisicao_todos_itens_dic = requisicao_todos_itens.json()
        for categoria in requisicao_todos_itens_dic:
            for item in requisicao_todos_itens_dic[categoria]:
                dic_item = requisicao_todos_itens_dic[categoria][item]
                #print(dic_item)
                # parametros
                nome_produto = item.replace("%20", " ")
                # verifica se o produto pertence a lista de favoritos
                isfavorito = nome_produto in self.lista_favoritos
                # caminho para a imagem no storage
                caminho_byte_image = dic_item['cores']['imagem_principal']
                # codifica o caminho
                caminho_byte_image_codificado = quote(caminho_byte_image, safe="?:.&=")
                BUCKET_STORAGE_NAME = "appvendas-ae071.appspot.com"
                # extensao do arquivo
                _, extensao = os.path.splitext(dic_item['imagem_principal'])
                # criando o banner 
                banner = BannerRoupasHomePage( 
                                                extensao = extensao, nome_produto = nome_produto,
                                                em_promocao = dic_item['em_promocao'],
                                                porcentagem_promocao = dic_item['porcentagem_promocao'],
                                                preco_normal = dic_item['preco_normal'], 
                                                favorito = isfavorito, descricao = dic_item['descricao'],
                                                caminho_para_imagem_todas_cores = dic_item['cores'],
                                                tamanhos_disponiveis = dic_item['tamanhos'],
                            url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_STORAGE_NAME}/o/categorias%2F{caminho_byte_image_codificado}?alt=media"
                                                )
                self.search_page.ids["scroll_produtos"].add_widget(banner)


    def search_produto(self, nome_produto):
        

        Clock.schedule_once(lambda dt: self.search_page.ids["scroll_produtos"].clear_widgets(), 0)
        Clock.unschedule(self.criar_banner_search_page)
        self.search_page.ids["search_text_field"].text = ""
        #self.search_page.ids["scroll_produtos"].clear_widgets()
        url = "https://appvendas-ae071-default-rtdb.firebaseio.com"
        for categoria in self.lista_todas_categorias:
            nome_produto = nome_produto.lower()
            query = f'{url}/todos_produtos/{categoria}.json?orderBy="index_search"&equalTo="{nome_produto}"'
            requisicao_indexon = requests.get(query)
            requisicao_indexon_dict = requisicao_indexon.json()
            if requisicao_indexon_dict != {}:

                self.search_page.ids["conteiner_cor_nao_encontrada"].opacity = 0
                # definindo os parametros
                nome_produto = nome_produto.replace("%20", " ")
                isfavorito = nome_produto in self.lista_favoritos
                caminho_byte_image = requisicao_indexon_dict[nome_produto]['cores']['imagem_principal']#.replace("/", "%2F")
                # codificar caminho para imagem no storage
                caminho_byte_image_codificado = quote(caminho_byte_image, safe=".=&:?")
                BUCKET_STORAGE_NAME = "appvendas-ae071.appspot.com"
                _,extensao = os.path.splitext(requisicao_indexon_dict[nome_produto]['cores']['imagem_principal'])

                Clock.schedule_once(lambda dt:self.criar_banner_search_page(caminho_byte_image_codificado = caminho_byte_image_codificado,
                                            extensao = extensao, nome_produto = nome_produto.replace("%20", " "),
                                                em_promocao = requisicao_indexon_dict[nome_produto]['em_promocao'],
                                            porcentagem_promocao = requisicao_indexon_dict[nome_produto]['porcentagem_promocao'],
                                            preco_normal = requisicao_indexon_dict[nome_produto]['preco_normal'], 
                                            favorito = isfavorito, descricao = requisicao_indexon_dict[nome_produto]['descricao'],
                                            caminho_para_imagem_todas_cores = requisicao_indexon_dict[nome_produto]['cores'],
                                            tamanhos_disponiveis = requisicao_indexon_dict[nome_produto]['tamanhos'],
                        url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_STORAGE_NAME}/o/categorias%2F{caminho_byte_image_codificado}?alt=media"), 0)

                        # self.criar_banner_search_page(caminho_byte_image_codificado = caminho_byte_image_codificado,
                        #                             extensao = extensao, nome_produto = nome_produto.replace("%20", " "),
                        #                                 em_promocao = requisicao_indexon_dict[nome_produto]['em_promocao'],
                        #                             porcentagem_promocao = requisicao_indexon_dict[nome_produto]['porcentagem_promocao'],
                        #                             preco_normal = requisicao_indexon_dict[nome_produto]['preco_normal'], 
                        #                             favorito = isfavorito, descricao = requisicao_indexon_dict[nome_produto]['descricao'],
                        #                             caminho_para_imagem_todas_cores = requisicao_indexon_dict[nome_produto]['cores'],
                        #                             tamanhos_disponiveis = requisicao_indexon_dict[nome_produto]['tamanhos'],
                        #         url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_STORAGE_NAME}/o/categorias%2F{caminho_byte_image_codificado}?alt=media")
                        # banner = BannerRoupasHomePage( 
                        #                                 extensao = extensao, nome_produto = nome_produto.replace("%20", " "),
                        #                                 em_promocao = requisicao_indexon_dict[nome_produto]['em_promocao'],
                        #                             porcentagem_promocao = requisicao_indexon_dict[nome_produto]['porcentagem_promocao'],
                        #                             preco_normal = requisicao_indexon_dict[nome_produto]['preco_normal'], 
                        #                             favorito = isfavorito, descricao = requisicao_indexon_dict[nome_produto]['descricao'],
                        #                             caminho_para_imagem_todas_cores = requisicao_indexon_dict[nome_produto]['cores'],
                        #                             tamanhos_disponiveis = requisicao_indexon_dict[nome_produto]['tamanhos'],
                        #         url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_STORAGE_NAME}/o/categorias%2F{caminho_byte_image_codificado}?alt=media"
                        #                             )
                    #self.search_page.ids["scroll_produtos"].add_widget(banner)
                break

    def search_produto_thread(self, instancia, valor, dt=0.5):
        thread = threading.Thread(target=self.search_produto, args=(instancia, valor))
        thread.start()


    def criar_banner_search_page(self,dt = 0, **kwargs):
        

        extensao = kwargs['extensao']
        nome_produto = kwargs['nome_produto']
        em_promocao = kwargs['em_promocao']
        porcentagem_promocao = kwargs['porcentagem_promocao']
        preco_normal = kwargs['preco_normal']
        favorito = kwargs['favorito']
        descricao = kwargs['descricao']
        caminho_para_imagem_todas_cores = kwargs['caminho_para_imagem_todas_cores']
        tamanhos_disponiveis = kwargs['tamanhos_disponiveis']
        BUCKET_STORAGE_NAME = "appvendas-ae071.appspot.com"
        caminho_byte_image_codificado = kwargs['caminho_byte_image_codificado']


        banner = BannerRoupasHomePage( 
                                extensao = extensao, nome_produto = nome_produto.replace("%20", " "),
                                em_promocao = em_promocao,
                            porcentagem_promocao = porcentagem_promocao,
                            preco_normal = preco_normal, 
                            favorito = favorito, descricao = descricao,
                            caminho_para_imagem_todas_cores = caminho_para_imagem_todas_cores,
                            tamanhos_disponiveis = tamanhos_disponiveis,
        url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_STORAGE_NAME}/o/categorias%2F{caminho_byte_image_codificado}?alt=media"
                            )
        
        self.search_page.ids["scroll_produtos"].add_widget(banner)
        self.search_page.disabled = False



    
    def search_produto_teste(self, instancia, valor):
        
        self.menu_search_page.dismiss()
        self.menu_search_page = None
        self.menu_search_page = MDDropdownMenu()

        Clock.schedule_once(lambda dt: self.search_page.ids["scroll_produtos"].clear_widgets(), 0)
        Clock.unschedule(self.criar_banner_search_page)
        #self.search_page.ids["scroll_produtos"].clear_widgets()
        url = "https://appvendas-ae071-default-rtdb.firebaseio.com"

        lista_produtos_encontrados = []
                
        for produto in self.lista_todos_produtos:
            if valor.lower() in produto.lower() and valor != "":
                #produto = str(produto).replace(" ", "%20")
                lista_produtos_encontrados.append(produto)
                

        menu_itens = [

            {"text": f"{i.title()}","font_style": "Overline",
            "on_release": lambda x=f"{i}": self.search_produto(x)}for i in lista_produtos_encontrados
                    ]
            

        #"Caption"
        #"Overline"

        self.menu_search_page.items=menu_itens
        self.menu_search_page.width_mult=4
        
        button = self.search_page.ids["search_text_field"]
        self.menu_search_page.caller = button

        self.menu_search_page.position = 'bottom'

        self.menu_search_page.open()


    def add_cores_disponiveis(self):

        self.menu_cores = MDDropdownMenu()

        cores_disponiveis = {
                "Vermelho": "#FF0000",
                "Laranja": "#FFA500",
                "Amarelo": "#FFFF00",
                "Verde": "#008000",
                "Azul": "#0000FF",
                "Anil": "#4B0082",
                "Violeta": "#9400D3",
                "Preto": "#000000",
                "Branco": "#FFFFFF",
                "Cinza": "#808080",
                "Marrom": "#A52A2A",
                "Rosa": "#FFC0CB"
            }
                    
        menu_items = [
            {   
                "text": f"{cor}",
                "leading_icon": "circle",
                "leading_icon_color": f"{cores_disponiveis[cor]}",
                #"width": dp(200),
                "height": dp(37),
                #"trailing_icon": "apple-keyboard-command",
                #"trailing_text": "+Shift+X",
                #"trailing_icon_color": f"{cor}",
                #"trailing_text_color": "grey",
                "on_release": lambda x=f"{cores_disponiveis[cor]}": self.busca_produto_filtro_cor(x),
            } for cor in cores_disponiveis
                ]
        button = self.search_page.ids["drop_down_item_cores"]
        self.menu_cores.items = menu_items
        self.menu_cores.caller = button
        self.menu_cores.width=dp(130)
        self.menu_cores.position = 'bottom'
        self.menu_cores.open()
    
    # pega os produtos de acordo com o filtro cor ou tamanho
    def busca_produto_filtro_cor(self, cor):

        self.search_page.ids["scroll_produtos"].clear_widgets()
        self.search_page.disabled = True
        self.menu_cores.dismiss()

        requisicao = requests.get("https://appvendas-ae071-default-rtdb.firebaseio.com/todos_produtos.json")
        requisicao_dict = requisicao.json()
        cor = cor.lstrip('#')

        add_image_cor_nao_encontrada = True

        for categoria in requisicao_dict:
            for produto in requisicao_dict[categoria]:

    	        for cor_disponivel in  requisicao_dict[categoria][produto]["cores"]:

                    if cor_disponivel != "imagem_principal":
                        cor_pesquisada = cor
                        cor_analise = cor_disponivel
                    
                        cor_parecida = self.color_similarity(cor_pesquisada, cor_analise)
                        if cor_parecida <= 90:

                            self.search_page.ids["conteiner_cor_nao_encontrada"].opacity = 0
                            add_image_cor_nao_encontrada = False

                            nome_produto = produto.replace("%20", " ")
                            isfavorito = nome_produto in self.lista_favoritos
                            caminho_byte_image = requisicao_dict[categoria][produto]['cores']['imagem_principal']#.replace("/", "%2F")
                            # codificar caminho para imagem no storage
                            caminho_byte_image_codificado = quote(caminho_byte_image, safe=".=&:?")
            
                            BUCKET_STORAGE_NAME = "appvendas-ae071.appspot.com"
                            _,extensao = os.path.splitext(requisicao_dict[categoria][produto]['cores']['imagem_principal'])
                            self.criar_banner_search_page(caminho_byte_image_codificado = caminho_byte_image_codificado,
                                                        extensao = extensao, nome_produto = nome_produto,
                                                        em_promocao = requisicao_dict[categoria][produto]['em_promocao'],
                                                        porcentagem_promocao = requisicao_dict[categoria][produto]['porcentagem_promocao'],
                                                        preco_normal = requisicao_dict[categoria][produto]['preco_normal'], 
                                                        favorito = isfavorito, descricao = requisicao_dict[categoria][produto]['descricao'],
                                                        caminho_para_imagem_todas_cores = requisicao_dict[categoria][produto]['cores'],
                                                        tamanhos_disponiveis = requisicao_dict[categoria][produto]['tamanhos'],
                                    url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_STORAGE_NAME}/o/categorias%2F{caminho_byte_image_codificado}?alt=media")
                            break 

        if add_image_cor_nao_encontrada:
            self.search_page.disabled = False
            self.search_page.ids["conteiner_cor_nao_encontrada"].source = "https://firebasestorage.googleapis.com/v0/b/appvendas-ae071.appspot.com/o/icones%2Fproduto_cor_nao_encontrado?alt=media"
            self.search_page.ids["conteiner_cor_nao_encontrada"].opacity = 1



    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    def color_similarity(self, color1, color2):
        r1, g1, b1 = self.hex_to_rgb(color1)
        r2, g2, b2 = self.hex_to_rgb(color2)

        return ((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2) ** 0.5
    









    def add_tamanhos_disponiveis(self):

        self.menu_tamanhos = MDDropdownMenu()

        tamanhos_disponiveis = ["p", "pp", "g", "gg", "xgg", "m", "rn",]
        menu_items = [
            {   
                "text": f"{tamanho.upper()}",
                #"leading_icon": "circle",
                #"leading_icon_color": f"{cores_disponiveis[cor]}",
                #"width": dp(200),
                "height": dp(37),
                #"trailing_icon": "apple-keyboard-command",
                #"trailing_text": "+Shift+X",
                #"trailing_icon_color": f"{cor}",
                #"trailing_text_color": "grey",
                "on_release": lambda x=f"{tamanho}": self.busca_produto_filtro_tamanho(x),
            } for tamanho in tamanhos_disponiveis
                ]
        button = self.search_page.ids["drop_down_item_tamanhos"]
        self.menu_tamanhos.items = menu_items
        self.menu_tamanhos.caller = button
        self.menu_tamanhos.width=dp(130)
        self.menu_tamanhos.position = 'bottom'
        self.menu_tamanhos.open()
    



    def busca_produto_filtro_tamanho(self, tamanho):

        self.search_page.ids["scroll_produtos"].clear_widgets()
        self.search_page.disabled = True
        self.menu_tamanhos.dismiss()

        requisicao = requests.get("https://appvendas-ae071-default-rtdb.firebaseio.com/todos_produtos.json")
        requisicao_dict = requisicao.json()

        tamanho = tamanho.lower()

        add_image_tamanho_nao_encontrado = True

        for categoria in requisicao_dict:
            for produto in requisicao_dict[categoria]:

    	        if tamanho in  requisicao_dict[categoria][produto]["tamanhos"]:

                    self.search_page.ids["conteiner_cor_nao_encontrada"].opacity = 0
                    add_image_tamanho_nao_encontrado = False

                    nome_produto = produto.replace("%20", " ")
                    isfavorito = nome_produto in self.lista_favoritos
                    caminho_byte_image = requisicao_dict[categoria][produto]['cores']['imagem_principal']#.replace("/", "%2F")
                    # codificar caminho para imagem no storage
                    caminho_byte_image_codificado = quote(caminho_byte_image, safe=".=&:?")
              
                    BUCKET_STORAGE_NAME = "appvendas-ae071.appspot.com"
                    _,extensao = os.path.splitext(requisicao_dict[categoria][produto]['cores']['imagem_principal'])
                    self.criar_banner_search_page(caminho_byte_image_codificado = caminho_byte_image_codificado,
                                                extensao = extensao, nome_produto = nome_produto,
                                                em_promocao = requisicao_dict[categoria][produto]['em_promocao'],
                                                porcentagem_promocao = requisicao_dict[categoria][produto]['porcentagem_promocao'],
                                                preco_normal = requisicao_dict[categoria][produto]['preco_normal'], 
                                                favorito = isfavorito, descricao = requisicao_dict[categoria][produto]['descricao'],
                                                caminho_para_imagem_todas_cores = requisicao_dict[categoria][produto]['cores'],
                                                tamanhos_disponiveis = requisicao_dict[categoria][produto]['tamanhos'],
                            url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_STORAGE_NAME}/o/categorias%2F{caminho_byte_image_codificado}?alt=media")
                 

        if add_image_tamanho_nao_encontrado:
            self.search_page.disabled = False
            self.search_page.ids["conteiner_cor_nao_encontrada"].source = "https://firebasestorage.googleapis.com/v0/b/appvendas-ae071.appspot.com/o/icones%2Fproduto_tamanho_nao_encontrado?alt=media"
            self.search_page.ids["conteiner_cor_nao_encontrada"].opacity = 1




    def add_dialog_filtrar_preco(self):

        content = ContentClsCustom()
        self.dialog_filtrar_preco = MDDialog(
                content_cls = content,
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="CANCELAR",
                        #on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="confirmar"
                    )
                    
                ],
            )
        
        self.dialog_filtrar_preco.open()

    
    def slider_filtrar_preco(self):
        slider_preco = SliderFiltroPreco(pos_hint = {"center_x": 0.5, "center_y": 0.5},
                                            size_hint = (0.8, 0.4), conteiner= self.search_page.ids["conteiner_principal"],
                                            funcao_botao=self.busca_produto_filtro_preco,
                                            conteiner_disabled= self.search_page.ids["scroll_produtos"])

        self.search_page.ids["scroll_produtos"].disabled = True
        self.search_page.ids["conteiner_principal"].add_widget(slider_preco)



    def busca_produto_filtro_preco(self):

        self.search_page.ids["scroll_produtos"].clear_widgets()
        self.search_page.disabled = True

        preco_minimo = SliderFiltroPreco.valor_min_filtrado
        preco_maximo = SliderFiltroPreco.valor_max_filtrado

        requisicao = requests.get("https://appvendas-ae071-default-rtdb.firebaseio.com/todos_produtos.json")
        requisicao_dict = requisicao.json()



        add_image_tamanho_nao_encontrado = True

        for categoria in requisicao_dict:
            for produto in requisicao_dict[categoria]:

                if requisicao_dict[categoria][produto]["em_promocao"]:
                    if (float(requisicao_dict[categoria][produto]["preco_normal"]) * float(requisicao_dict[categoria][produto]["porcentagem_promocao"])) >= preco_minimo and (float(requisicao_dict[categoria][produto]["preco_normal"]) * float(requisicao_dict[categoria][produto]["porcentagem_promocao"])) <= preco_maximo:

                        self.search_page.ids["conteiner_cor_nao_encontrada"].opacity = 0
                        add_image_tamanho_nao_encontrado = False

                        nome_produto = produto.replace("%20", " ")
                        isfavorito = nome_produto in self.lista_favoritos
                        caminho_byte_image = requisicao_dict[categoria][produto]['cores']['imagem_principal']#.replace("/", "%2F")
                        # codificar caminho para imagem no storage
                        caminho_byte_image_codificado = quote(caminho_byte_image, safe=".=&:?")
                
                        BUCKET_STORAGE_NAME = "appvendas-ae071.appspot.com"
                        _,extensao = os.path.splitext(requisicao_dict[categoria][produto]['cores']['imagem_principal'])
                        self.criar_banner_search_page(caminho_byte_image_codificado = caminho_byte_image_codificado,
                                                    extensao = extensao, nome_produto = nome_produto,
                                                    em_promocao = requisicao_dict[categoria][produto]['em_promocao'],
                                                    porcentagem_promocao = requisicao_dict[categoria][produto]['porcentagem_promocao'],
                                                    preco_normal = requisicao_dict[categoria][produto]['preco_normal'], 
                                                    favorito = isfavorito, descricao = requisicao_dict[categoria][produto]['descricao'],
                                                    caminho_para_imagem_todas_cores = requisicao_dict[categoria][produto]['cores'],
                                                    tamanhos_disponiveis = requisicao_dict[categoria][produto]['tamanhos'],
                                                    url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_STORAGE_NAME}/o/categorias%2F{caminho_byte_image_codificado}?alt=media")

                        
                else:
                    if requisicao_dict[categoria][produto]["preco_normal"] >= preco_minimo and requisicao_dict[categoria][produto]["preco_normal"] <= preco_maximo:


                        self.search_page.ids["conteiner_cor_nao_encontrada"].opacity = 0
                        add_image_tamanho_nao_encontrado = False

                        nome_produto = produto.replace("%20", " ")
                        isfavorito = nome_produto in self.lista_favoritos
                        caminho_byte_image = requisicao_dict[categoria][produto]['cores']['imagem_principal']#.replace("/", "%2F")
                        # codificar caminho para imagem no storage
                        caminho_byte_image_codificado = quote(caminho_byte_image, safe=".=&:?")
                
                        BUCKET_STORAGE_NAME = "appvendas-ae071.appspot.com"
                        _,extensao = os.path.splitext(requisicao_dict[categoria][produto]['cores']['imagem_principal'])
                        self.criar_banner_search_page(caminho_byte_image_codificado = caminho_byte_image_codificado,
                                                    extensao = extensao, nome_produto = nome_produto,
                                                    em_promocao = requisicao_dict[categoria][produto]['em_promocao'],
                                                    porcentagem_promocao = requisicao_dict[categoria][produto]['porcentagem_promocao'],
                                                    preco_normal = requisicao_dict[categoria][produto]['preco_normal'], 
                                                    favorito = isfavorito, descricao = requisicao_dict[categoria][produto]['descricao'],
                                                    caminho_para_imagem_todas_cores = requisicao_dict[categoria][produto]['cores'],
                                                    tamanhos_disponiveis = requisicao_dict[categoria][produto]['tamanhos'],
                                url_AsyncImage=f"https://firebasestorage.googleapis.com/v0/b/{BUCKET_STORAGE_NAME}/o/categorias%2F{caminho_byte_image_codificado}?alt=media")
                


        if add_image_tamanho_nao_encontrado:
            self.search_page.disabled = False
            self.search_page.ids["conteiner_cor_nao_encontrada"].source = "https://firebasestorage.googleapis.com/v0/b/appvendas-ae071.appspot.com/o/icones%2Fproduto_preco_nao_encontrado?alt=media"
            self.search_page.ids["conteiner_cor_nao_encontrada"].opacity = 1

        self.search_page.ids["scroll_produtos"].disabled = False




MainApp().run()