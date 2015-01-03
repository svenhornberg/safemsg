from base64 import b64decode
from Crypto.Cipher import PKCS1_OAEP
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.storage.jsonstore import JsonStore
from kivy.properties import StringProperty
from kivy.core.clipboard import Clipboard

from Crypto.PublicKey import RSA
import base64

class Mainpage(StackLayout):

    store = JsonStore('data.json')

    #AccordionItem 1

    def savepub(self):

        input_pubkey = self.ids['input_pubkey']
        self.store.put('pub', pub=input_pubkey.text)
        pass

    def clipPup(self):

        input_pubkey = self.ids['input_pubkey']
        input_pubkey.text = Clipboard.get('UTF8_STRING')
        pass

    #AccordionItem 2

    def clipOwnpup(self):
        print Clipboard.put('Hallo','UTF8_STRING')
        pass

    def encrypt(self):



        pass

    def decrypt(self):
        pass

    def genkeys(self):

        key = RSA.generate(1024)

        binPrivKey = key.exportKey('DER')
        binPubKey =  key.publickey().exportKey('DER')

        privKeyObj = RSA.importKey(binPrivKey)
        pubKeyObj =  RSA.importKey(binPubKey)

        msg = "attack at dawn"
        emsg = key.encrypt(msg, 0)
        dmsg = privKeyObj.decrypt(emsg)

        print(emsg)
        print(dmsg)

        print(base64.b64encode(binPrivKey))

        input_private = self.ids['input_private']
        input_private.text = str(base64.b64encode(binPrivKey))

        input_public = self.ids['input_public']
        input_public.text = str(base64.b64encode(binPubKey))


        pass


    pass


class SafeMsgApp(App):

    Window.clearcolor = (.2,.2,.2, 0)

    def build(self):
        main = Mainpage()
        input_private = main.ids['input_private']
        input_private.text = str('sss')

        input_public = main.ids['input_public']
        input_public.text = str(base64.b64encode('ssdsd'))

        return main


if __name__ == '__main__':
    SafeMsgApp().run()
