# Day 67: Guess Who
import tkinter as tk
from tkinter import Tk, ttk

from PIL import Image, ImageTk

window = Tk()
window.title('Guess Who?')
window.geometry('400x400')

label = 'Guess Who?'


def show_image():
    person = text.get('1.0', 'end')
    if person.lower().strip() == 'mo':
        canvas.itemconfig(container, image=mo)
    elif person.lower().strip() == "charlotte":
        canvas.itemconfig(container, image=charlotte)
    elif person.lower().strip() == "gerald":
        canvas.itemconfig(container, image=gerald)
    elif person.lower().strip() == "katie":
        canvas.itemconfig(container, image=katie)
    else:
        label["text"] = "Unable to find this user"


label = ttk.Label(text=label)
label.pack()
text = tk.Text(window, height=1, width=30)
text.pack()
button = ttk.Button(text='Find', command=show_image)
button.pack()
canvas = tk.Canvas(window, width=400, height=380)
canvas.pack()
charlotte = ImageTk.PhotoImage(Image.open("Guess_Who/charlotte.jpg"))
gerald = ImageTk.PhotoImage(Image.open("Guess_Who/gerald.jpg"))
katie = ImageTk.PhotoImage(Image.open("Guess_Who/katie.jpg"))
mo = ImageTk.PhotoImage(Image.open("Guess_Who/mo.jpg"))
container = canvas.create_image(150, 1, image=mo)

window.mainloop()
