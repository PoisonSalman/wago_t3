import threading

from kivy.properties import ObjectProperty,StringProperty
from kivymd.toast import toast
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from pyModbusTCP.client import ModbusClient
import time
import kivy
import  threading
import time
import  random


kivy.require('1.0.7')
from kivy.app import App
kv=Builder.load_file('main.kv')
c = ModbusClient()

def build():
    return kv

class MyScreen(Screen):
    container = ObjectProperty(None)
    data = StringProperty('')



    def save_data(self):
        print("waiting connection")
        self.data = self.container.text
        print(self.data)
        return self.data

    def baglan(self):

        SERVER_HOST = self.data
        SERVER_PORT = 502
        toggle = True
        c.host(SERVER_HOST)
        c.port(SERVER_PORT)
        toast("connection is OK")
        if not c.is_open():
            if not c.open():
                toast("connection fail")
                print("connection fail")


    def li_on(self):
        if c.open():
            c.write_single_coil(32768, True)
            time.sleep(0.5)
            bits = c.read_coils(32768)
            print("bits #0 to 3: " + str(bits))
        else:
            toast("connection lost")


    def li_of(self):

        if c.open():

            c.write_single_coil(32768, False)
            bits = c.read_coils(32768)
            print("bits #0 to 3: " + str(bits))
            toast("sent_coil")

        else:
            toast("connection lost")

    def statu(self):
        while True:
            c.open()
            bits = c.read_coils(32768)
            print("bits #0 to 3: " + str(bits))

    def disconnect(self):
        c.close()
        print("disconnected")
        self.disconnect()


'''class işlem(threading.Thread):
    def __init__(self):
        # Sınıfı örneklerken almak istediğimiz argümanları burada atıyoruz, init fonksiyonuna da parametreleri ekliyoruz.
        threading.Thread.__init__(self)

    def run(self):

        while True:
            SERVER_HOST = "192.168.1.4"
            SERVER_PORT = 502
            toggle = True
            c.host(SERVER_HOST)
            c.port(SERVER_PORT)
            if c.is_open():
                print("connection ok")
            else:
                print("baglantı yok")
                break
        return True
calistir = işlem()
while True:

    try:
        if not c.is_open():
            if not c.open():
                calistir.start()
                break

    except:
        print("böyle bir değer yok")'''


class TestApp(App):

    def build(self):

        return MyScreen()

if __name__ == "__main__":

    TestApp().run()