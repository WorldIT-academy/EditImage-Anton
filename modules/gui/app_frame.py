'''
    ### У цьому модулі створили клас для фрейму
    
    #### [Посилання на GitHub](https://github.com/WorldIT-academy/EditImage-Anton/blob/master/modules/gui/app_frame.py)
    
    #### Приклад використаня класу:
    ```python
        self.explorer = App_frame(
            ch_master=self.content,
            width= self.content._current_width * 0.15,
            height=self.content._current_height,
            fg_color = "#181818"
        )
    ```
'''

# ```python 
# ``` - дозволяє написати багаторядковий python код

# [текст](посилання) - створює текст, який відкриває сайт по посиланню

import customtkinter as ctk

# Сирий рядок (r"" - дозволяє використовувати спеціальні символи як текст)
# print(r"Hello\nworld")

# # - змінює розмір тексту у багаторядковому коментарі (Всього існує 6 рівнів).
# чим більше решіток тим менше текст

# - - робить маркований список

# `` - дозволяє написати однорядковий код

# fg_color - колір фону
class App_frame(ctk.CTkFrame):
    """
        ### Цей клас дозволяє створити фрейм

        #### Конструктор класу :
        - `ch_master` - віджет , до якого будемо кріпити frame 
        - `width` - ширина фрейму
        - `height` - висота фрейму
        - `fg_color` - колір заднього фону фрейму
        - `**kwargs` - словник додаткових іменованих аргументів
    """
    # master - Відповідає за те на чому буде розміщуватись фрейм
    def __init__(self, ch_master, width, height, fg_color, **kwargs):
        ctk.CTkFrame.__init__(
            self,
            master=ch_master,
            width=width,
            height=height,
            fg_color=fg_color,
            corner_radius=0,
            **kwargs
        )