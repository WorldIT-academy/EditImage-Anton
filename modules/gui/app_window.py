"""
    Цей файл використовується для створення вікна застосунку(фотошопу)
"""
import customtkinter as ctk 
from ..tools import read_json

class App(ctk.CTk):
    """
        Цей клас використовуємо для створення вікна додатку
    """
    def __init__(self, **kwargs):
        """
            Це конструктор класу *може бути тільки 1*
        """
        # app = App(name = "Michael")
        # {"name": "Michael"}
        
        # name_of_dict["name_of_key"]
        # rgb - 255, 255, 255
        json_data = read_json(name_json="settings.json")
        # Наслідуємо від класу CTk його __init__ (конструктор класу)
        ctk.CTk.__init__(self,fg_color = json_data["app_fg_color"],**kwargs)
        
        #* створюємо властивість ширини (поле)
        #~ winfo_screenwidth - функція яка отримуєх ширину екрана користувача
        #! множемо на 0,8 щоб отримати 80% від ширини 
        #& робемо цілим чослом щоб працював geometry
        self.width = int(self.winfo_screenwidth() * json_data["app_width"])
        
        self.height = int(self.winfo_screenheight() * json_data["app_height"]) # winfo_screenheight() отримує висоту екрану користувача
        
        self.title(json_data["app_title"]) # title задає назву вікна
        self.geometry(f"{self.width}x{self.height}") # geometry задає розмір вікна
        
app = App()