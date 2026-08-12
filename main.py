from kivy.app import App
from kivy.uix.label import Label

class VoiceAssistantApp(App):
    def build(self):
        return Label(text='Namaste! Mera AI Assistant taiyar ho raha hai.')

if __name__ == '__main__':
    VoiceAssistantApp().run()

# Trigger build
