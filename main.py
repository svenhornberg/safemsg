from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.storage.jsonstore import JsonStore
from kivy.properties import StringProperty


import rsa
import imaplib
import email



class Mainpage(StackLayout):

    store = JsonStore('data.json')
    store.put('email', email="")
    store.put('stmp', smtp="")
    store.put('imap', smtp="")


    def genkeys(self):
        store = JsonStore('data.json')
        (pubkey, privkey) = rsa.newkeys(128)

        print('pub' + str(pubkey))
        print('priv' + str(privkey))

        label_private = self.ids['label_private']
        label_private.text = str(privkey)


        pass


    pass


class SafeMsgApp(App):
    __version__ = "1.0"
    Window.clearcolor = (.2,.2,.2, 0)

    def build(self):
        return Mainpage()


if __name__ == '__main__':
    SafeMsgApp().run()
