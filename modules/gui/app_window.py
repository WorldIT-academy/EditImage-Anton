import customtkinter as ctk 

class App(ctk.CTk):
    def __init__(self, **kwargs):
        ctk.CTk.__init__(self,fg_color = "#FFFFFF",**kwargs)
        
        self.width = int(self.winfo_screenwidth() * 0.8)
        self.height = int(self.winfo_screenheight() * 0.8)
        self.title("Photoshop 2.0")
        self.geometry(f"{self.width}x{self.height}")
        
app = App()