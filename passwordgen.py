import random
import string
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class PasswordGeneratorApp(App):
    def build(self):
        Window.size = (650, 200)
        Window.clearcolor = (1, 1, 1, 1)
        self.window = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Input fields and generate button
        input_button_layout = GridLayout(cols=3, size_hint=(1, 0.3), padding=10, spacing=10)
        input_button_layout.add_widget(Label(text="Password Length:", color=(0, 0, 0, 1), font_size=24))
        self.length = TextInput(multiline=False, halign="right", font_size=24, size_hint=(0.5, None), height=40)
        input_button_layout.add_widget(self.length)

        self.generate_button = Button(text="Generate Password", background_color=(0.6, 0.7, 0.8, 1), font_size=24, size_hint=(0.5, None), height=40)
        self.generate_button.bind(on_press=self.generate_password)
        input_button_layout.add_widget(self.generate_button)

        self.window.add_widget(input_button_layout)

        # Result field
        result_layout = GridLayout(cols=1, size_hint=(1, 0.3), padding=10, spacing=10)
        result_layout.add_widget(Label(text="Generated Password:", color=(0, 0, 0, 1), font_size=24))
        self.result = TextInput(text="", font_size=24, halign="center", background_color=(0, 0, 0, 1), foreground_color=(0, 1, 0, 1), multiline=False)
        result_layout.add_widget(self.result)

        self.window.add_widget(result_layout)

        return self.window

    def generate_password(self, instance):
        length = int(self.length.text)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        self.result.text = password

if __name__ == "__main__":
    PasswordGeneratorApp().run()
