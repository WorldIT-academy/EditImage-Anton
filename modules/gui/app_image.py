"""
У цьому файлі створили клас для відображення зображень🤗🙄😚

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
        
        self.width = int(ch_master._current_width * 0.9)
        self.height = int(ch_master._current_height * 0.9)
        
        ctk.CTkLabel.__init__(
            self,
            master=ch_master,
            text="",
            image=self.image_load(),
            **kwargs
        )
        
    def image_load(self): 
        """
            Цей метод використовується для завантаження зображення😏
        """

        try:
            pillow_image = PIL.Image.open(fp = self.image_path)
            image = ctk.CTkImage(
                light_image= pillow_image,
                size=self.size_image(pillow_image)
            )

            return image
        except Exception as exception:
            print(exception)
            return None
        
    def size_image(self, image):
        """
            Цей метод підлаштовує розмір картинки під розмір батьківського фрейму
        """
        
        if image.width == image.height:
            if image.width >= self.width or image.height >= self.height:
                return (self.height, self.height)
            else:
                return (image.width, image.height)
        
        
        if image.width >= self.width or image.height >= self.height:
            return (self.width, self.height)
        else:
            return (image.width, image.height)
        