from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.storage.jsonstore import JsonStore

import rsa




class Mainpage(StackLayout):



    store = JsonStore('data.json')
    store.put('email', email="fuubah@gmail.com")
    store.put('stmp', smtp="")
    store.put('imap', smtp="")


    pass

class ClickMeButton(Button):
    def test(self):
        store = JsonStore('data.json')
        print('email:', store.get('email')['email'])


        pass

class RsaButton(Button):
    def test(self):
        store = JsonStore('data.json')
        (pubkey, privkey) = rsa.newkeys(128)

        print('pub' + str(pubkey))
        print('priv' + str(privkey))
        pass


class Password(TextInput):
    mail = "fet"

    pass

class SafeMsgApp(App):

    Window.clearcolor = (.2,.2,.2, 0)

    def build(self):
        return Mainpage()


if __name__ == '__main__':
    SafeMsgApp().run()
