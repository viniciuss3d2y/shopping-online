

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
from kivy.uix.image import AsyncImage


class ImageCarousel(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__()

        self.url_asyncimage = kwargs['url_asyncimage']

        self.conteiner_card = MDCard(pos_hint = {"center_x": 0.5, "center_y": 0.5},
                            size_hint = (0.9, 0.9))


        self.image_card = AsyncImage(source= self.url_asyncimage)
        #self.image_card.bind(on_load= self.desativar_loading)

        self.image_card.allow_stretch = True
        self.image_card.keep_ratio = True

        self.conteiner_card.add_widget(self.image_card)
        #self.conteiner_card.add_widget(self.loading)
        self.add_widget(self.conteiner_card)
        

    
    #def desativar_loading(self, *args):
        #self.conteiner_card.remove_widget(self.loading)