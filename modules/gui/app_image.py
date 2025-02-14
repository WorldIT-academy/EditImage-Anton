"""
У цьому файлі створили клас для відображення зображень

"""

import PIL.Image
import customtkinter as ctk
import PIL
class Image_label(ctk.CTkLabel):
    def __init__(self, ch_master, image_path, **kwargs):      
        """
            Цей клас використовуєтся для створення зображень
            
            Нижче вказані параметри конструктору класу
            - `ch_master` - параметр який відповідає за те, на чому буде намальовано зображення
            - `image_path` - параметр відповідаючий за шлях до картинки
            
            Властивості класу:
            - `self.image_path` - ця влстивість відповідає за шлях до картинки
        """   


        self.image_path = image_path
        
        ctk.CTkLabel.__init__(
            self,
            master=ch_master,
            text="",
            image=self.image_load(),
            **kwargs
        )
        
    def image_load(self): 
        """
            Цей метод використовується для завантаження зображення
        """

        try:
            pillow_image = PIL.Image.open(fp = self.image_path)
            image = ctk.CTkImage(
                light_image= pillow_image,
                size=(pillow_image.width, pillow_image.height)
            )
            return image
        except Exception as exception:
            print(exception)
            return None

