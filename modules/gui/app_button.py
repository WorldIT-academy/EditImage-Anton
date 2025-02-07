'''
    В цьому модулі створили клас для кнопки
'''

import PIL.Image
import customtkinter as ctk
import os
import PIL

# hover_color - колір кнопки, коли ми наводимося на неї мишею
class App_button(ctk.CTkButton):

    '''
        Цей клас використовуется для створення кнопки
        
        конструктор класу:
        - size - розміри
        - ch_master - до чого кріпиться кнопка
        - fg_color - колір фону кнопки
        - hover_color - коли наводимося на кнопку - змінює колір
        - name_image - назва картинки
    '''
    
    # Ми створюємо властивість (свойство) "мозку" класу (методу-конструктору),
    # а використовуємо у інших методах через self
    def __init__(self, size, ch_master, fg_color, hover_color, name_image=None, command=None, text='', **kwargs):
        self.name_image = name_image
        self.size = size

        ctk.CTkButton.__init__(
            self,
            master=ch_master,
            width=int(size),
            height=int(size),
            fg_color=fg_color,
            hover_color=hover_color,
            text=text,
            image=self.load_image(),
            command=command,
            **kwargs
        )
        

    def load_image(self):
        """
            Завантажує картинку по ім'я картинки
        """
        try:
            path_image = os.path.abspath(os.path.join(__file__, "..", "..", "..", "static", "icons", self.name_image))
            picture = ctk.CTkImage(
                light_image = PIL.Image.open(fp= path_image),
                size = (self.size, self.size)
            )
            return picture
        except:
            return None