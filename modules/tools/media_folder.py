"""
    Цей модуль створює папку media
"""

import colorama
import os
colorama.init(autoreset=True)

GREEN = colorama.Fore.GREEN
RED = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW

def create_media_folder():
    """
        Ця функція створює папку media
    """
    
    try:
        
        path_media = os.path.abspath(os.path.join(__file__, "..", "..", "..", "media"))
        for dir in ["downloaded_images", "edited_images"]:
            if os.path.exists(os.path.join(path_media, dir)) == False:
                os.makedirs(os.path.join(path_media, dir), exist_ok=True)
                print(f"{GREEN}{dir} в папці media було створено")
        
    except Exception as exception:
        print(f"{RED}Сталася помилка при створенні директорії media: {exception}")
        

create_media_folder()