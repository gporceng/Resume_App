from kivy.app import App
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView

Builder.load_string("""
<MenuScreen>:
    Screen:
        Image:
            source: "title_bg.png"
            size: self.size
            pos: self.pos
            size: root.size
            allow_stretch: True
            keep_ratio: False
            
        Image:
            source: "icon.png"
            size: self.size
            pos_hint: {'center_x':0.5, 'center_y': .7}
        MDRoundFlatButton:
            text:"Begin"
            font_size: '32sp'
            pos_hint: {'center_x':0.5,'center_y':0.3}
            on_press: root.manager.current = 'resume'
            size_hint: (.75,.3)


<ResumeScreen>:

    Image:
        source: "title_bg.png"
        size: self.size
        pos: self.pos
        size: root.size
        allow_stretch: True
        keep_ratio: False
    Screen:
        Image:
            source: "sidebar.png"
            size: self.size
            pos_hint: {'center_x':0}

        MDRoundFlatButton:
            text: "Exit"
            pos_hint: {'center_x':.125,'center_y':.9}
            size_hint: (.20,.075)
            on_press: root.manager.current = 'menu'

        MDRoundFlatButton:
            text: "Email Resume"
            pos_hint: {'center_x':.125,'center_y':.8}
            size_hint: (.20,.075)
            on_press: root.manager.current = 'email'

        ScrollView:
            size_hint: (.75,1)
            pos_hint: {'center_x':.62}
            do_scroll_x: False
            do_scroll_y: True

            GridLayout:
                rows: 2
                size_hint: (1,2)
                Button:
                    text: "Hello World"

                Button:
                    text: "Hello World"
                
                Button:
                    text: "Hello World"

<EmailScreen>:
    Image:
        source: "title_bg.png"
        size: self.size
        pos: self.pos
        size: root.size
        allow_stretch: True
        keep_ratio: False

    Screen:
        Image:
            source: "contact.png"
            size_hint: (.75,1)
            pos_hint: {'center_x':.5, 'center_y': .7}


""")

class MenuScreen(Screen):
    pass

class ResumeScreen(Screen):
    pass

class EmailScreen(Screen):
    pass


class design(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "50"
        self.title = ("Gregory Porceng Resume")
        Window.size = (1480,720)
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ResumeScreen(name='resume'))
        sm.add_widget(EmailScreen(name='email'))
        return sm



if __name__ == '__main__':
    design().run()