"""
    Цей файл відповідіє за відкриття діалогового вікна з вибором файлів
"""
import customtkinter as ctk
from ..gui.app_button import App_button
# module filedialog - з бібліотеки tkinter, дозволяє працювати з діалоговим вікном
from tkinter import filedialog
from ..gui.app_image import Image_label

image_list = []

def show_image(frame: ctk.CTkFrame, name_image:str):
    print(name_image)
    # frame.winfo_children() - повертає список всіх дочерніх віджетів, які знаходяться у frame
    children = frame.winfo_children()
    for child in children:
        # isinstance(object, class) - перевіряє, чи є object екземпляром класу class. Повертає True або False
        if isinstance(child, Image_label):
            # widget.pack_forget() - приховує widget, який було розміщено за допомогою pack()
            child.pack_forget()
    for image in image_list:
        if image.image_path.split("/")[-1] == name_image:
            image.pack(pady=30)

# askopenfiles - відкриває діалогове вікно, і повертає кортеж з відкритими обраними файлами
# askopenfilenames - відкриває діалогове вікно, і повертає кортеж з повними шляхами обраних файлів

def image_search(parent, ch_master, dashboard):
    """
        Ця функція відповіє за пошук картинки в діалоговому вікні
    """
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
            text=i.split("/")[-1],
            command = lambda name=i.split("/")[-1]: show_image(frame=dashboard, name_image=name)
        )

        # pack - розміщує об'єкти по черзі.
        # підлаштовує розміри батьківського фрейму під розміри його вмісту
        button.pack(anchor="w", pady=10, padx=20)
        picture = Image_label(
            ch_master= dashboard,
            image_path = i
        )
        image_list.append(picture)
        # picture.pack()
    