import PIL.Image
import customtkinter as ctk
import PIL
class Image_label(ctk.CTkLabel):
    def __init__(self, ch_master, image_path, **kwargs):
        self.image_path = image_path
        ctk.CTkLabel.__init__(
            self,
            master=ch_master,
            text="",
            image=self.image_load(),
            **kwargs
        )
    def image_load(self):
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
