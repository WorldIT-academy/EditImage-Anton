"""
    Цей модуль створює папку media
"""
#тут ми імпортуємо модулі
import colorama
import os

colorama.init(autoreset=True) #відповідає за те , щоб колір не переносився на наступний рядок
# Робимо константи кольорів
GREEN = colorama.Fore.GREEN
RED = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW


def create_media_folder():
    """
        Ця функція створює папку media
    """
    # Намагаємося зробити дію
    try:
        # __file__ це змінна яка зберігає повний шлях до файлу
        # join об'єднує шляхи
        # abspath будує нормальний шлях
        path_media = os.path.abspath(os.path.join(__file__, "..", "..", "..", "media"))
        for dir in ["downloaded_images", "edited_images"]:
            # перевіряємо чи існує папка dir у папці media
            if os.path.exists(os.path.join(path_media, dir)) == False:
                # makedirs створює папку в папці
                # exist_ok= True робить так, щоб коли ці папки існували помилки не виникало
                os.makedirs(os.path.join(path_media, dir), exist_ok=True)
                print(f"{GREEN}{dir} в папці media було створено")
    # Якщо виникає помилка, то виконує код у except
    except Exception as exception:
        print(f"{RED}Сталася помилка при створенні директорії media: {exception}")
        print(f"{RED}Сталася помилка у рядку {exception.__traceback__.tb_lineno}")
