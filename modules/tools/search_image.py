# module filedialog - з бібліотеки tkinter, дозволяє працювати з діалоговим вікном
from tkinter import filedialog
# askopenfiles - відкриває діалогове вікно, і повертає кортеж з відкритими обраними файлами
# askopenfilenames - відкриває діалогове вікно, і повертає кортеж з повними шляхами обраних файлів


def image_search(parent):
    # параметр parent визначає поверх якого вікна буде розміщено діалогове вікно
    filepath = filedialog.askopenfilenames(
        title="Select files",
        initialdir="/",
        filetypes=[("Image files",["*.png", "*.jpg", "*.jpeg"])],
        parent = parent 
    )
    
    print(filepath)