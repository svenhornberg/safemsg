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
    pub = 'pub'
    ownpub = 'ownpub'
    ownpriv = 'ownpriv'

    #AccordionItem 1

    def savepub(self):

        input_pubkey = self.ids['input_pubkey']

        test = input_pubkey.text

        decode = base64.b64decode(test)
        self.store.put(self.pub, val=decode)
        pass

    def clipPup(self):

        input_pubkey = self.ids['input_pubkey']
        input_pubkey.text = Clipboard.get('UTF8_STRING')
        pass

    #AccordionItem 2

    def clipOwnpup(self):
        input_public = self.ids['input_public']
        Clipboard.put(input_public.text,'UTF8_STRING')
        pass

    def genkeys(self):

        key = RSA.generate(1024)

        binPrivKey = key.exportKey('DER')
        binPubKey =  key.publickey().exportKey('DER')


        input_private = self.ids['input_private']
        input_private.text = str(base64.b64encode(binPrivKey))

        input_public = self.ids['input_public']
        input_public.text = str(base64.b64encode(binPubKey))

        pass

    def safeownkeys(self):

        input_private = self.ids['input_private']
        self.store.put(self.ownpriv, val=input_private.text)

        input_public = self.ids['input_public']
        self.store.put(self.ownpub, val=input_public.text)

        pass

    def loadownkeys(self):

        if self.store.exists(self.ownpriv):

            ownpriv = self.store.get(self.ownpriv)['val']
            input_private = self.ids['input_private']
            input_private.text = str(base64.b64encode(ownpriv))
            pass

        if self.store.exists('ownpub'):

            ownpub = self.store.get(self.ownpub)['val']
            input_public = self.ids['input_public']
            input_public.text = str(base64.b64encode(ownpub))
            pass


        pass

    #AccordionItem 3


    def encryptpub(self):

        output = self.ids['output_rsa']
        input = self.ids['input_rsa']

        if self.store.exists(self.pub):

            pub = self.store.get(self.pub)['val']
            pubKeyObj =  RSA.importKey(pub)

            output.text = pubKeyObj.encrypt(input.text, 0)
            pass
        else:
            output.text = 'Kein Pubkey hinterlegt'

        '''
        privKeyObj = RSA.importKey(binPrivKey)
        pubKeyObj =  RSA.importKey(binPubKey)

        msg = "attack at dawn"
        emsg = key.encrypt(msg, 0)
        dmsg = privKeyObj.decrypt(emsg)

        '''
        pass

    def decryptpub(self):

        output = self.ids['output_rsa']
        input = self.ids['input_rsa']

        if self.store.exists(self.pub):

            pub = self.store.get(self.pub)['val']
            pubKeyObj =  RSA.importKey(pub)

            output.text = pubKeyObj.decrypt(input.text)
            pass
        else:
            output.text = 'Kein Pubkey hinterlegt'

        pass

    def decryptownpriv(self):

        output = self.ids['output_rsa']
        input = self.ids['input_rsa']

        if self.store.exists(self.ownpriv):

            key = self.store.get(self.ownpriv)['val']
            keyObj = RSA.importKey(key)

            output.text = keyObj.decrypt(input.text)
            pass
        else:
            output.text = 'Kein Privkey hinterlegt'


        pass

    def encryptownpriv(self):

        output = self.ids['output_rsa']
        input = self.ids['input_rsa']

        if self.store.exists(self.ownpriv):

            key = self.store.get(self.ownpriv)['val']
            keyObj = RSA.importKey(key)

            output.text = keyObj.encrypt(input.text, 0)
            pass
        else:
            output.text = 'Kein Privkey hinterlegt'


        pass

    def inputfromclip(self):

        input = self.ids['input_rsa']
        input.text = Clipboard.get('UTF8_STRING')

        pass

    def cliptooutput(self):

        input_public = self.ids['output_rsa']
        Clipboard.put(input_public.text,'UTF8_STRING')

        pass


    pass


class SafeMsgApp(App):

    Window.clearcolor = (.2,.2,.2, 0)

    def build(self):
        main = Mainpage()

        if main.store.exists(main.ownpriv):

            ownpriv = main.store.get(main.ownpriv)['val']
            input_private = main.ids['input_private']
            input_private.text = str(base64.b64encode(ownpriv))
            pass

        if main.store.exists('ownpub'):

            ownpub = main.store.get(main.ownpub)['val']
            input_public = main.ids['input_public']
            input_public.text = str(base64.b64encode(ownpub))
            pass

        return Mainpage()


if __name__ == '__main__':
    SafeMsgApp().run()
