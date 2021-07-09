from kivymd.app import MDApp
from kivymd.uix.card import MDCard 
from kivymd.uix.floatlayout import FloatLayout
from kivy.lang import Builder

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title:'MyApp'
            left_action_items: [['menu', lambda x: x]]
            right_action_items: [['dots-vertical', lambda x: x]]
        TelaLogin:

<SenhaCard>:
    id: card
    size_hint: .7, .7
    pos_hint: {'center_x': .5, 'center_y': .5}
    MDTextField:
        text: 'Senha antiga'

<TelaLogin>:
    MDIconButton:
        pos_hint: {'center_x': .5, 'center_y': .8}
        icon: 'language-python'
        user_font_size: '75sp'

    MDTextField:
        size_hint_x: .9
        hint_text: 'Email:'
        pos_hint: {'center_x': .5, 'center_y': .6}

    MDTextField:
        size_hint_x: .9
        hint_text: 'Senha:'
        pos_hint: {'center_x': .5, 'center_y': .5}

    MDRaisedButton:
        size_hint_x: .9
        pos_hint: {'center_x':.5, 'center_y': .4}
        text: 'Login'

    MDLabel:
        pos_hint: {'center_y': .3}
        halign: 'center'
        text: 'Esqueceu sua senha?'

    MDTextButton:
        pos_hint: {'center_x': .5, 'center_y': .2}
        text: 'Clique aqui!'
        on_release: root.abrir_card()

'''

class SenhaCard(MDCard):
    ...

class TelaLogin(FloatLayout):
    def abrir_card(self):
        self.add_widget(SenhaCard())


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()