# from kivy.lang import Builder
# from kivy.metrics import dp

# from kivymd.app import MDApp
# from kivymd.uix.menu import MDDropdownMenu

# KV = '''
# MDScreen:

#     MDRaisedButton:
#         id: button
#         text: "Press me"
#         pos_hint: {"center_x": .5, "center_y": .5}
#         on_release: app.menu_open()
# '''


# class Test(MDApp):
#     def menu_open(self):
#         menu_items = [
#             {
#                 "text": f"Item {i}",
#                 "on_release": lambda x=f"Item {i}": self.menu_callback(x),
#             } for i in range(5)
#         ]
#         MDDropdownMenu(
#             caller=self.root.ids.button, items=menu_items
#         ).open()

#     def menu_callback(self, text_item):
#         print(text_item)

#     def build(self):
#         self.theme_cls.primary_palette = "Orange"
#         self.theme_cls.theme_style = "Dark"
#         return Builder.load_string(KV)


# Test().run()
# from kivy.lang import Builder

# from kivymd.app import MDApp
# from kivymd.uix.behaviors import StencilBehavior
# from kivymd.uix.fitimage import FitImage

# KV = '''
# #:import os os
# #:import images_path kivymd.images_path


# Carousel:

#     StencilImage:
#         size_hint: .9, .8
#         pos_hint: {"center_x": .5, "center_y": .5}
#         source: os.path.join(images_path, "logo", "kivymd-icon-512.png")
# '''


# class StencilImage(FitImage, StencilBehavior):
#     pass


# class Test(MDApp):
#     def build(self):
#         return Builder.load_string(KV)


# Test().run()
# from kivy.lang import Builder
# from kivy.properties import StringProperty

# from kivymd.uix.button import MDBu
# from kivymd.uix.tooltip import MDTooltip
# from kivymd.app import MDApp

# KV = '''
# <YourTooltipClass>

#     MDTooltipPlain:
#         text:
#             "Grant value is calculated using the closing stock price \\n" \
#             "from the day before the grant date. Amounts do not \\n" \
#             "reflect tax witholdings."


# <TooltipMDIconButton>

#     MDButtonText:
#         text: root.text


# MDScreen:
#     md_bg_color: self.theme_cls.backgroundColor

#     TooltipMDIconButton:
#         text: "Tooltip button"
#         pos_hint: {"center_x": .5, "center_y": .5}
# '''


# class YourTooltipClass(MDTooltip):
#     '''Implements your tooltip base class.'''


# class TooltipMDIconButton(YourTooltipClass, MDButton):
#     '''Implements a button with tooltip behavior.'''

#     text = StringProperty()


# class Example(MDApp):
#     def build(self):
#         self.theme_cls.primary_palette = "Olive"
#         return Builder.load_string(KV)


# Example().run()




# import os

# from kivy.core.window import Window
# from kivy.lang import Builder
# from kivy.metrics import dp

# from kivymd.app import MDApp
# from kivymd.uix.filemanager import MDFileManager
# from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText

# KV = '''
# MDScreen:
#     md_bg_color: self.theme_cls.backgroundColor

#     MDButton:
#         pos_hint: {"center_x": .5, "center_y": .5}
#         on_release: app.file_manager_open()

#         MDButtonText:
#             text: "Open manager"
# '''


# class Example(MDApp):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         Window.bind(on_keyboard=self.events)
#         self.manager_open = False
#         self.file_manager = MDFileManager(
#             exit_manager=self.exit_manager, select_path=self.select_path
#         )

#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         return Builder.load_string(KV)

#     def file_manager_open(self):
#         self.file_manager.show(
#             os.path.expanduser("~"))  # output manager to the screen
#         self.manager_open = True

#     def select_path(self, path: str):
#         '''
#         It will be called when you click on the file name
#         or the catalog selection button.

#         :param path: path to the selected directory or file;
#         '''

#         self.exit_manager()
#         MDSnackbar(
#             MDSnackbarText(
#                 text=path,
#             ),
#             y=dp(24),
#             pos_hint={"center_x": 0.5},
#             size_hint_x=0.8,
#         ).open()

#     def exit_manager(self, *args):
#         '''Called when the user reaches the root of the directory tree.'''

#         self.manager_open = False
#         self.file_manager.close()

#     def events(self, instance, keyboard, keycode, text, modifiers):
#         '''Called when buttons are pressed on the mobile device.'''

#         if keyboard in (1001, 27):
#             if self.manager_open:
#                 self.file_manager.back()
#         return True


# Example().run()



# When resizing the application window, the direction of change will be
# printed - 'left' or 'right'.
# from kivy.lang import Builder

# from kivymd.app import MDApp


# class Example(MDApp):
#     def build(self):
#         return Builder.load_string(
#             '''
# MDScreen:

#     MDBottomNavigation:

#         MDBottomNavigationItem:
#             name: 'screen 1'
#             text: 'Mail'
#             icon: 'gmail'
#             badge_icon: "numeric-10"
                

#         MDBottomNavigationItem:
#             name: 'screen 2'
#             text: 'Twitter'
#             icon: 'twitter'

#             MDLabel:
#                 text: 'Screen 2'
#                 halign: 'center'
# '''
#         )


#Example().run()


from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivy.uix.screenmanager import ScreenManager, Screen

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class MainScreen(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name

class ExampleApp(MDApp):
    def build(self):
        return Builder.load_string('''
ScreenManager:
    MainScreen:
        name: 'main'

    ScreenOne:
        name: 'screen1'
        
    ScreenTwo:
        name: 'screen2'

<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDBottomNavigation:
            MDBottomNavigationItem:
                name: 'screen1'
                text: 'Screen 1'
                icon: 'home'
                on_tab_press: root.change_screen('screen1')
                
                MDLabel:
                    text: 'This is Screen 1'
                    halign: 'center'

            MDBottomNavigationItem:
                name: 'screen2'
                text: 'Screen 2'
                icon: 'settings'
                on_tab_press: root.change_screen('screen2')

                MDLabel:
                    text: 'This is Screen 2'
                    halign: 'center'

<ScreenOne>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Welcome to Screen 1'
            halign: 'center'

<ScreenTwo>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Welcome to Screen 2'
            halign: 'center'
''')

ExampleApp().run()
