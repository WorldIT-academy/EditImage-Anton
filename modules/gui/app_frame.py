'''
У цьому модули створили клас для фрейму
'''
import customtkinter as ctk

# fg_color - колір фону
class App_frame(ctk.CTkFrame):
    """
    Цей клас дозволяе створити фрейм
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