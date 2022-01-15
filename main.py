from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = (720, 640)

class Container(Widget):
    def clear_button(self):
        self.ids.calc_input.text = '0'
        
    def button_press(self, button):
        beg = self.ids.calc_input.text
        if 'Ошибка' in beg:
            beg = ''
        if beg == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{beg}{button}'
        
    def choose_of_sign(self, sign):
        beg = self.ids.calc_input.text
        
        self.ids.calc_input.text = f'{beg}{sign}'
    
    
    def equalf(self):
        beg = self.ids.calc_input.text
        try:
            result = eval(beg)
            self.ids.calc_input.text = str(result)
        except Exception:
            self.ids.calc_input.text = 'Ошибка'
            
        
    def dot(self):
        beg = self.ids.calc_input.text
        num_li = beg.split('+')
        num_li[-1]
        if '+' in beg and '.' not in num_li[-1]:
            beg = f'{beg}.'
            self.ids.calc_input.text = beg
        elif '-' in beg and '.' not in num_li[-1]:
            beg = f'{beg}.'
            self.ids.calc_input.text = beg
        elif '*' in beg and '.' not in num_li[-1]:
            beg = f'{beg}.'
            self.ids.calc_input.text = beg
        elif '/' in beg and '.' not in num_li[-1]:
            beg = f'{beg}.'
            self.ids.calc_input.text = beg
        if '.' in beg:
            pass
        else:
            beg = f'{beg}.'
            self.ids.calc_input.text = beg
            
    def remove(self):
        beg = self.ids.calc_input.text
        beg = beg[:-1]
        self.ids.calc_input.text = beg
        
    def pos_sign(self):
        beg = self.ids.calc_input.text
        if '-' in beg:
            self.ids.calc_input.text = beg.replace('-', '')
        else:
            self.ids.calc_input.text = f'-{beg}'
            
            
class CalculatorApp(App):
    def build(self):
        return Container()
    
    

if __name__ == "__main__":
    CalculatorApp().run()
    
