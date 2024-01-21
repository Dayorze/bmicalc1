from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class BMILayout(BoxLayout):
    def __init__(self, **kwargs):
        super(BMILayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.grid = GridLayout(cols=2, row_default_height=50, row_force_default=True)
        self.add_widget(self.grid)

        self.grid.add_widget(Label(text='Height (cm):', size_hint_x=None, width=120))
        self.height_input = TextInput(multiline=False, size_hint_x=None, width=120)
        self.grid.add_widget(self.height_input)

        self.grid.add_widget(Label(text='Weight (kg):', size_hint_x=None, width=120))
        self.weight_input = TextInput(multiline=False, size_hint_x=None, width=120)
        self.grid.add_widget(self.weight_input)

        self.result_label = Label(text='', size_hint=(1, None), height=50)
        self.add_widget(self.result_label)

        self.calc_button = Button(text='Calculate', size_hint=(1, None), height=50)
        self.calc_button.bind(on_press=self.calculate_bmi)
        self.add_widget(self.calc_button)

    def calculate_bmi(self, instance):
        try:
            height = float(self.height_input.text)
            weight = float(self.weight_input.text)
        except ValueError:
            self.result_label.text = 'Please enter a valid number for both height and weight.'
            return

        bmi = weight / ((height / 100) ** 2)

        self.result_label.text = f'Your BMI is {bmi:.2f}'

        if bmi <= 18.4:
            self.result_label.text += '\nYou are underweight.'
        elif bmi <= 24.9:
            self.result_label.text += '\nYou are healthy.'
        elif bmi <= 29.9:
            self.result_label.text += '\nYou are overweight.'
        elif bmi <= 34.9:
            self.result_label.text += '\nYou are severely overweight.'
        elif bmi <= 39.9:
            self.result_label.text += '\nYou are obese.'
        else:
            self.result_label.text += '\nYou are severely obese.'

class BMIApp(App):
    def build(self):
        return BMILayout()

if __name__ == '__main__':
    BMIApp().run()
