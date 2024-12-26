import requests
import os


# url = "https://appvendas-ae071-default-rtdb.firebaseio.com/"
# req = requests.get(f"{url}categorias/moda.json")
# print(req.json())
# requ_dic = req.json()


# requests.patch(f"{url}todos_produtos.json",
#                json=requ_dic)



# from kivy.lang import Builder
# from kivymd.app import MDApp

# KV = '''
# MDScreen:
#     MDLabel:
#         text: "Hello, KivyMD!"
#         halign: "center"
#     MDRaisedButton:
#         text: "Press Me"
#         pos_hint: {"center_x": 0.5, "center_y": 0.4}
#         on_release: app.on_button_press()
# '''

# class MyApp(MDApp):
#     def build(self):
#         return Builder.load_string(KV)

#     def on_button_press(self):
#         print("Button pressed!")

# MyApp().run()


# main.py
# from kivy.app import App
# from kivy.uix.carousel import Carousel
# #from kivy.uix.image import Image
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.clock import Clock


# from kivy.lang import Builder
# from kivy.factory import Factory

# from kivymd.app import MDApp

# Builder.load_string('''
# <ExampleBanner@Screen>

#     MDBanner:
#         id: banner
#         text: ["One line string text example without actions."]
#         # The widget that is under the banner.
#         # It will be shifted down to the height of the banner.
#         over_widget: screen
#         vertical_pad: toolbar.height

#     MDTopAppBar:
#         id: toolbar
#         title: "Example Banners"
#         elevation: 4
#         pos_hint: {'top': 1}

#     MDBoxLayout:
#         id: screen
#         orientation: "vertical"
#         size_hint_y: None
#         height: Window.height - toolbar.height

#         OneLineListItem:
#             text: "Banner without actions"
#             on_release: banner.show()

#         Widget:
# ''')


# class Test(MDApp):
#     def build(self):
#         return Factory.ExampleBanner()


# Test().run()




# from kivy.lang import Builder

# from kivymd.app import MDApp

# KV = '''
# MDScreen:

#     MDSmartTile:
#         radius: 24
#         box_radius: [0, 0, 24, 24]
#         box_color: 1, 1, 1, .2
#         source: "cats.jpg"
#         pos_hint: {"center_x": .5, "center_y": .5}
#         size_hint: None, None
#         size: "320dp", "320dp"

#         MDIconButton:
#             icon: "heart-outline"
#             theme_icon_color: "Custom"
#             icon_color: 1, 0, 0, 1
#             pos_hint: {"center_y": .5}
#             on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

#         MDLabel:
#             text: "Julia and Julie"
#             bold: True
#             color: 1, 1, 1, 1
# '''


# class MyApp(MDApp):
#     def build(self):
#         return Builder.load_string(KV)


# MyApp().run()

# import os
# import sys
# import platform  # Substituto para os.uname() no Windows

# from kivy.core.window import Window
# from kivy import __version__ as kv__version__
# from kivy.lang import Builder
# from kivy.metrics import dp

# from kivymd.app import MDApp
# from kivymd import __version__
# from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
# from materialyoucolor import __version__ as mc__version__

# MAIN_KV = '''
# MDScreen:
#     md_bg_color: app.theme_cls.bg_normal  # Cor de fundo

#     MDScrollView:
#         do_scroll_x: False

#         MDBoxLayout:
#             id: main_scroll
#             orientation: "vertical"
#             adaptive_height: True

#             MDBoxLayout:
#                 adaptive_height: True

#                 MDLabel:
#                     theme_text_color: "Custom"
#                     text: "OS Info"
#                     font_size: "55sp"
#                     adaptive_height: True
#                     padding: "10dp", "20dp", 0, 0

#                 MDIconButton:
#                     icon: "menu"
#                     on_release: app.open_menu(self)
#                     pos_hint: {"center_y": .5}
# '''

# class Example(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = 'Light'
#         return Builder.load_string(MAIN_KV)

#     def on_start(self):
#         info = {
#             "Name": [
#                 os.name,
#                 (
#                     "microsoft"
#                     if os.name == "nt"
#                     else ("linux" if platform.system() != "Darwin" else "apple")
#                 ),
#             ],
#             "Architecture": [platform.machine(), "memory"],
#             "Hostname": [platform.node(), "account"],
#             "Python Version": ["v" + sys.version, "language-python"],
#             "Kivy Version": ["v" + kv__version__, "alpha-k-circle-outline"],
#             "KivyMD Version": ["v" + __version__, "material-design"],
#             "MaterialYouColor Version": ["v" + mc__version__, "invert-colors"],
#             "Pillow Version": ["Unknown", "image"],
#             "Working Directory": [os.getcwd(), "folder"],
#             "Home Directory": [os.path.expanduser("~"), "folder-account"],
#             "Environment Variables": [os.environ, "code-json"],
#         }

#         try:
#             from PIL import __version__ as pil__version_
#             info["Pillow Version"] = ["v" + pil__version_, "image"]
#         except Exception:
#             pass

#         for info_item in info:
#             item = OneLineIconListItem(text=f"{info_item}: {info[info_item][0]}")
#             icon = IconLeftWidget(icon=info[info_item][1])
#             item.add_widget(icon)
#             self.root.ids.main_scroll.add_widget(item)

#         Window.size = [dp(350), dp(600)]


# Example().



from kivy.lang import Builder
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

KV = '''
MDScreen:

    MDRaisedButton:
        id: button
        text: "PRESS ME"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.menu.open()
'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [
            {
                "text": f"Item {i}",
                "leading_icon": "web",
                "leading_icon_color":"#FF0000",
                "trailing_icon": "apple-keyboard-command",
                "trailing_text": "+Shift+X",
                "trailing_icon_color": "grey",
                "trailing_text_color": "grey",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            md_bg_color="#bdc6b0",
            caller=self.screen.ids.button,
            items=menu_items,
        )

    def menu_callback(self, text_item):
        print(text_item)

    def build(self):
        return self.screen


Test().run()




r = requests.get("https://appvendas-ae071-default-rtdb.firebaseio.com/todos_produtos.json")
r_dic = r.json()
lista_cores = []
lista_cores_sem_repe = []
for categoria in r_dic:
    for sub in r_dic[categoria]:
        for cor in r_dic[categoria][sub]['tamanhos']:
            if cor not in lista_cores:
                lista_cores.append(cor)


print(lista_cores)
['007653', '004bf1', 'abacaf', 'c20571', 'd60100', 'f9c90a', '303032', '1d59ab', 'e83250', '2d2d2d', '3c201f', '6f3e26', 'dddddd', 'f899a7']
['g', 'gg', 'p', 'pp', 'm']