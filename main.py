from kivy.app import App
from kivy.uix.label import Label

class KIApp(App):
    def build(self):
        return Label(text='Hello K.I')

if __name__ == '__main__':
    KIApp().run()
    
