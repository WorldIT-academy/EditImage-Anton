"""
    Цей файл використовується для створення вікна застосунку(фотошопу)
"""
import customtkinter as ctk 
from .app_frame import App_frame
from ..tools import read_json
from .app_button import App_button

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
        
        
        # нумерований (неіменований), упорядкований
        # ("Суп", "котлета", "салат", "компот")
        
        
        # іменований варіант (неупорядкований)
        # {
        #     "сніданок": "салат",
        #     "обід": "суп",
        #     "вечеря": "котлета"
        # }
                
        
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
        self.resizable(width=False, height=False) # resizable дозволяє заборонити зміну розмірів вікна
        # 255 255 255 - rgb
        # #123546 - hex
        self.header = App_frame(
            ch_master = self,
            width= self.width,
            height = self.height * 0.05,
            fg_color = "#181818",
        )
        self.header.place(x = 0, y = 0)
        
        self.content = App_frame(
            ch_master= self,
            height = self.height * 0.95,
            width = self.width,
            fg_color = "#a1a1a1"
        )
        self.content.place(x= 0, y = self.height * 0.05 + 1)
        self.vertical_menu= App_frame(
            ch_master = self.content,
            width= self.content._current_width * 0.05,
            height = self.content._current_height,
            fg_color = "#181818",
        )
        self.vertical_menu.place(x= 0, y = 0)
        
        self.explorer = App_frame(
            ch_master=self.content,
            width= self.content._current_width * 0.15,
            height=self.content._current_height,
            fg_color = "#181818"
        )
        self.explorer.place(x=self.vertical_menu._current_width + 1, y=0)       
        self.dashboard = App_frame(
            ch_master=self.content,
            width= self.content._current_width * 0.8,
            height= self.content._current_height,
            fg_color = "#a1a1a1"
        )
        self.dashboard.place(x=self.vertical_menu._current_width + self.explorer._current_width + 3, y=0)
        self.header_dashboard = App_frame(
            ch_master = self.dashboard,
            width = self.dashboard._current_width,
            height = self.dashboard._current_height * 0.04,
            fg_color = "#181818"
        )
        self.header_dashboard.place(x = 0, y = 0)
        self.content_dashboard = App_frame(
            ch_master=self.dashboard,
            width=self.dashboard._current_width,
            height=self.dashboard._current_height * 0.96,
            fg_color="#1f1f1f"
        )
        self.content_dashboard.place(x=0, y=self.header_dashboard._current_height + 1)
        
        
        self.search_button = App_button(
            size = self.vertical_menu._current_width * 0.5,
            ch_master= self.vertical_menu,
            fg_color= "#181818",
            hover_color = "#373535",
            name_image= "explorer.png"
        )

        self.search_button.place(x=10, y=20)
        
app = App()