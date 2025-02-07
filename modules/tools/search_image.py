
from ..gui.app_button import App_button
# module filedialog - з бібліотеки tkinter, дозволяє працювати з діалоговим вікном
from tkinter import filedialog
# askopenfiles - відкриває діалогове вікно, і повертає кортеж з відкритими обраними файлами
# askopenfilenames - відкриває діалогове вікно, і повертає кортеж з повними шляхами обраних файлів


def image_search(parent, ch_master):
    # параметр parent визначає поверх якого вікна буде розміщено діалогове вікно
    filepath = filedialog.askopenfilenames(
        title="Select files",
        initialdir="/",
        filetypes=[("Image files",["*.png", "*.jpg", "*.jpeg"])],
        parent = parent
    )
    # split - розбиває рядок на елементи списку по символу, який ми вказали
    for i in filepath:
        #! print(i.split("/")[-1])
        button = App_button(
            size=50,
            ch_master=ch_master,
            fg_color="#181818",
            hover_color="#373535",
            text=i.split("/")[-1] 
        )
        # pack - розміщує об'єкти по черзі.
        # підлаштовує розміри батьківського фрейму під розміри його вмісту
        button.pack(anchor="w", pady=10, padx=20)