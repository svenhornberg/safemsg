from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.storage.jsonstore import JsonStore
from kivy.properties import StringProperty

from Crypto.PublicKey import RSA


class Mainpage(StackLayout):

    store = JsonStore('data.json')

    def encrypt(self):



        pass

    def decrypt(self):
        pass

    def genkeys(self):
        store = JsonStore('data.json')
        (pubkey, privkey) = rsa.newkeys(128)

        print('pub' + str(pubkey))
        print('priv' + str(privkey))

        input_private = self.ids['input_private']
        input_private.text = str(privkey)

        input_public = self.ids['input_public']
        input_public.text = str(pubkey)


        pass


    pass


class SafeMsgApp(App):

    Window.clearcolor = (.2,.2,.2, 0)

    def build(self):
        return Mainpage()


if __name__ == '__main__':
    SafeMsgApp().run()
