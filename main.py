from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.core.clipboard import Clipboard

from Crypto.PublicKey import RSA
import myrsa
import primenum


class Mainpage(StackLayout):

    store = JsonStore('data.json')
    pub = 'pub'
    ownpub = 'ownpub'
    ownpriv = 'ownpriv'

    #AccordionItem 1

    def savepub(self):

        input_pubkey = self.ids['input_pubkey']
        test = input_pubkey.text
        self.store.put(self.pub, val=test)
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

        (privkey, pubKey) = primenum.getTwoRandomPrimes()

        (publickey, privatekey) = myrsa.generateRSAKeys(privkey, pubKey)


        input_private = self.ids['input_private']
        input_private.text = str(publickey)

        input_public = self.ids['input_public']
        input_public.text = str(privatekey)

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
            input_private.text = str(ownpriv)
            pass

        if self.store.exists('ownpub'):

            ownpub = self.store.get(self.ownpub)['val']
            input_public = self.ids['input_public']
            input_public.text = str(ownpub)
            pass


        pass

    #AccordionItem 3


    def encryptpub(self):

        output = self.ids['output_rsa']
        input = self.ids['input_rsa']

        if self.store.exists(self.pub):

            pub = self.store.get(self.pub)['val']
            values = pub.strip().replace(")", "").replace("(", "").split(',')
            pubKey = []
            for x in values:
                pubKey.append(int(x))
                pass

            encode = self.encode(pubKey, input.text)
            output.text = encode
            pass
        else:
            output.text = 'Kein Pubkey hinterlegt'


        pass

    def decryptpub(self):

        output = self.ids['output_rsa']
        input = self.ids['input_rsa']

        if self.store.exists(self.pub):

            pub = self.store.get(self.pub)['val']
            values = pub.strip().replace(")", "").replace("(", "").split(',')
            pubKey = []
            for x in values:
                pubKey.append(int(x))
                pass

            decodeval = self.decode(pubKey, input.text)
            output.text = decodeval

            pass
        else:
            output.text = 'Kein Pubkey hinterlegt'

        pass

    def decryptownpriv(self):

        output = self.ids['output_rsa']
        input = self.ids['input_rsa']

        if self.store.exists(self.ownpriv):

            key = self.store.get(self.ownpriv)['val']

            values = key.strip().replace(")", "").replace("(", "").split(',')
            pubKey = []
            for x in values:
                pubKey.append(int(x))
                pass

            decodeval = self.decode(pubKey, input.text)
            output.text = decodeval

        else:
            output.text = 'Kein Privkey hinterlegt'


        pass

    def encryptownpriv(self):

        output = self.ids['output_rsa']
        input = self.ids['input_rsa']

        if self.store.exists(self.ownpriv):

            key = self.store.get(self.ownpriv)['val']
            values = key.strip().replace(")", "").replace("(", "").split(',')
            pubKey = []
            for x in values:
                pubKey.append(int(x))
                pass

            encode = self.encode(pubKey, input.text)
            output.text = encode
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

    def encode(self, publickey, message):

        #each char in message rsa  + liste
        #-> liste return

        n, e = publickey
        values = []

        for chrx in message:

            oVal = ord(chrx)
            encrypted_num = (oVal ** e) % n
            values.append(encrypted_num)
            pass

        return  ','.join(map(str, values))


    def decode(self, privatekey, message):

        values = message.split(',')
        n, d = privatekey
        message = ""

        for chrx in values:
            number = int(chrx)
            decrypted_num = number ** d % n
            message += chr(decrypted_num)
            pass

        return message


class SafeMsgApp(App):

    Window.clearcolor = (.2,.2,.2, 0)

    def build(self):
        main = Mainpage()

        if main.store.exists(main.ownpriv):

            ownpriv = main.store.get(main.ownpriv)['val']
            input_private = main.ids['input_private']
            input_private.text = str(ownpriv)
            pass

        if main.store.exists('ownpub'):

            ownpub = main.store.get(main.ownpub)['val']
            input_public = main.ids['input_public']
            input_public.text = str(ownpub)
            pass

        return Mainpage()


if __name__ == '__main__':
    SafeMsgApp().run()
