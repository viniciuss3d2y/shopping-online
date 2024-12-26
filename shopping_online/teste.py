import requests
import os

with open(r"c:\Users\kaio vinicius\Documents\AppVendas\icones\favorito.png", "rb")as file:
    conteu = file.read()
dados = {"2Fa3ffe697c506d64a79f52730f1012279.jpg": conteu}
cate = "neyamr"
nome = "fdddvbfgbgbgfbnhg34234324dv.jpg"
requests.post(f"https://firebasestorage.googleapis.com/v0/b/appvendas-ae071.appspot.com/o?name=categorias%2F{cate}%2F{nome}",
              data=conteu)

from kivymd.uix.chip import MDChip, MDChipText
MDChipText

hv

# requisicao = requests.get(f"https://appvendas-ae071-default-rtdb.firebaseio.com/produtos.json")
# req_dic = requisicao.json()

# for i in req_dic:
#     arquivo = req_dic[i]['imagem']
#     requi =requests.get(f"https://firebasestorage.googleapis.com/v0/b/appvendas-ae071.appspot.com/o/{arquivo}?alt=media")
#     info = {"file": requi.content}
#     o = requests.post(f"https://firebasestorage.googleapis.com/v0/b/appvendas-ae071.appspot.com/o?name=fotos_todos_produtos%2F{arquivo}",
#                   data=requi.content)
#     print(requi.content)

# nome =os.path.basename(r"C:\Users\kaio vinicius\Downloads\Design sem nome.png")

# with open(r"C:\Users\kaio vinicius\Downloads\Design sem nome.png", "rb") as file:
#     conteudo = file.read()

# requests.post(f"https://firebasestorage.googleapis.com/v0/b/appvendas-ae071.appspot.com/o?name=fotos_promocao_homepage%2F{nome}",
#               data=conteudo)

# caminho = r"C:\Users\kaio vinicius\Downloads\Design sem nome (2)\5.png"
# nome_arquivo = os.path.basename(caminho)
# with open(caminho, "rb") as file:
#     file_bin = file.read()


# requests.post(f"https://firebasestorage.googleapis.com/v0/b/appvendas-ae071.appspot.com/o?name=fotos_promocao_homepage%2F{nome_arquivo}",
#               data=file_bin)

# from kivy.app import App
# from kivy.uix.button import ButtonBehavior
# from kivy.uix.image import Image
# from kivy.graphics import Color, Ellipse
# from kivy.clock import Clock
# from kivy.utils import get_color_from_hex

# class ImageButtonCustom(ButtonBehavior, Image):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         self.raio = 0

#         with self.canvas.after:
#             Color(rgba=get_color_from_hex("#dedede"))
#             self.circulo = Ellipse(pos=(0, 0), size=(0, 0))

#     def aumentar_tamanho_ellipse(self, dt):
#         self.raio += 2
#         # Atualiza o tamanho da elipse
#         self.circulo.size = (self.raio * 2, self.raio * 2)
#         # Ajusta a posição para que a elipse cresça a partir do ponto clicado
#         self.circulo.pos = (self.center_x - self.raio, self.center_y - self.raio)

#     def diminuir_tamanho_ellipse(self, dt):
#         if self.raio > 0:
#             self.raio -= 2
#             # Garante que o tamanho da elipse nunca seja negativo
#             self.circulo.size = (self.raio * 2, self.raio * 2)
#             self.circulo.pos = (self.center_x - self.raio, self.center_y - self.raio)
#         else:
#             Clock.unschedule(self.diminuir_tamanho_ellipse)

#     def on_touch_down(self, touch):
#         if self.collide_point(*touch.pos):
#             # Inicia o crescimento da elipse no ponto do toque
#             self.circulo.pos = (touch.x - self.raio, touch.y - self.raio)
#             Clock.schedule_interval(self.aumentar_tamanho_ellipse, 1/30)

#         return super().on_touch_down(touch)

#     def on_touch_move(self, touch):
#         if self.collide_point(*touch.pos):
#             # Atualiza a posição da elipse enquanto move o toque
#             self.circulo.pos = (touch.x - self.raio, touch.y - self.raio)

#         return super().on_touch_move(touch)

#     def on_touch_up(self, touch):
#         Clock.unschedule(self.aumentar_tamanho_ellipse)
#         Clock.schedule_interval(self.diminuir_tamanho_ellipse, 1/30)

#         return super().on_touch_up(touch)

# class MyApp(App):
#     def build(self):
#         return ImageButtonCustom(source='icones/logo.png')  # Coloque a sua imagem aqui

# if __name__ == '__main__':
#     MyApp().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line

class ColorfulLineWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # Desenha o primeiro segmento da linha em vermelho
            Color(1, 0, 0)  # Vermelho
            Line(points=[100, 200, 300, 200], width=5)

            # Desenha o segundo segmento da linha em verde
            Color(0, 1, 0)  # Verde
            Line(points=[300, 200, 400, 300], width=5)

            # Desenha o terceiro segmento da linha em azul
            Color(0, 0, 1)  # Azul
            Line(points=[400, 300, 500, 200], width=5)

class MyApp(App):
    def build(self):
        return ColorfulLineWidget()

MyApp().run()



jb


nome_categoria = "homens"
sub_categoria = "jaquetas"
nome_item = "jaqueta casual"

preco_normal = 128.65
porcentagem_promocao = 0.3
em_promocao = True
tamanhos = {
        "p": "",
        "pp": "",
        "m": "",
        "g": "",
        "gg": ""
}
caminhos = {r"C:\Users\kaio vinicius\Downloads\Design sem nome (2)\17.png":"303032",
            r"C:\Users\kaio vinicius\Downloads\Design sem nome (2)\18.png":"1d59ab",
            r"C:\Users\kaio vinicius\Downloads\Design sem nome (2)\19.png":"e83250"}

uma_vez = True
for caminho in caminhos:
    # with open(caminho, 'rb') as bin_file:
    #     coteudo = bin_file.read()

    nome_arquivo = os.path.basename(caminho)

    bucket = "appvendas-ae071.appspot.com"
    #R=requests.post(f"https://firebasestorage.googleapis.com/v0/b/{bucket}/o?name=categorias%2F{nome_categoria}%2F{sub_categoria}%2F{nome_item}%2F{nome_arquivo}", 
              #  data=coteudo)
                
    #print(R.json())


    # requests.patch(f"https://appvendas-ae071-default-rtdb.firebaseio.com/categorias/{nome_categoria}/{sub_categoria}/",
    #                json=nome_item)

    if uma_vez:
        info = {
            "descricao":" camisa básica cinza é perfeita para quem procura uma peça versátil e leve.Com um tom suave e natural, ela combina com qualquer estilo casual, trazendo frescor e suavidade ao visual.",
            "em_promocao": em_promocao,
            "porcentagem_promocao": porcentagem_promocao,
            "preco_normal": preco_normal,
            "tamanhos": tamanhos
            }
        requests.patch(f"https://appvendas-ae071-default-rtdb.firebaseio.com/todos_produtos/{sub_categoria}/{nome_item}.json",
                    json=info)
        
        uma_vez = False

        # cores item

    info_cores = {caminhos[caminho]:f"{nome_categoria}/{sub_categoria}/{nome_item}/{nome_arquivo}",
      "imagem_principal": f"{nome_categoria}/{sub_categoria}/{nome_item}/{nome_arquivo}"
    }
            
    requests.patch(f"https://appvendas-ae071-default-rtdb.firebaseio.com/categorias/{nome_categoria}/{sub_categoria}/{nome_item}/cores.json",
                    json=info_cores)

    requests.patch(f"https://appvendas-ae071-default-rtdb.firebaseio.com/categorias/geral/{sub_categoria}/{nome_item}/cores.json",
                    json=info_cores)



