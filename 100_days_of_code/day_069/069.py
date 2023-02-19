# Day 69: Visual Novel
from tkinter import ttk, Tk, PhotoImage, Canvas

window = Tk()
window.title('Visual Novel')
window.geometry('400x300')

story = 'You meet a woman on the way to a Replit meetup IRL'


def code_act():
    global story
    canvas.itemconfig(container, image=codes)
    story = 'She tries to pull out her laptop and drops it on the floor'
    story_label['text'] = story
    button.pack_forget()
    button_2.pack_forget()
    button_3.pack()
    button_4.pack()


def replit_act():
    global story
    canvas.itemconfig(container, image=replit)
    story = 'Why I use Replit of course, like every sane individual!'
    story_label['text'] = story
    button.pack_forget()
    button_2.pack_forget()
    button_5.pack()
    button_6.pack()


def edit_act():
    global story
    canvas.itemconfig(container, image=vs)
    story = 'She spends two hours loading up a code editor\n' \
            'and getting it working, you wait politely'
    story_label['text'] = story
    button_3.pack_forget()
    button_4.pack_forget()
    restart_button.pack()


def use_act():
    global story
    canvas.itemconfig(container, image=amazing)
    story = 'You both celebrate using the best\n ' \
            'coding platform on your way to the meetup'
    story_label['text'] = story
    button_3.pack_forget()
    button_4.pack_forget()
    restart_button.pack()


def alike_act():
    global story
    canvas.itemconfig(container, image=days)
    story = 'She tells you all about 100 days of code!'
    story_label['text'] = story
    button_5.pack_forget()
    button_6.pack_forget()
    restart_button.pack()


def celebrate_act():
    global story
    canvas.itemconfig(container, image=amazing)
    story = 'You both celebrate using the best\n ' \
            'coding platform on your way to the meetup\n' \
            'and talk about 100 days of code'
    story_label['text'] = story
    button_5.pack_forget()
    button_6.pack_forget()
    restart_button.pack()


def restart():
    global story
    canvas.itemconfig(container, image=start)
    story = 'You meet a woman on the way to a Replit meetup IRL'
    story_label['text'] = story
    restart_button.pack_forget()
    button.pack()
    button_2.pack()


start = PhotoImage(file='visual_novel/1.png')
start = start.subsample(4)
replit = PhotoImage(file='visual_novel/2.png')
replit = replit.subsample(4)
codes = PhotoImage(file='visual_novel/3.png')
codes = codes.subsample(4)
days = PhotoImage(file='visual_novel/4.png')
days = days.subsample(4)
amazing = PhotoImage(file='visual_novel/5.png')
amazing = amazing.subsample(4)
vs = PhotoImage(file='visual_novel/6.png')
vs = vs.subsample(4)

canvas = Canvas(window, width=300, height=200)
canvas.pack()
container = canvas.create_image(150, 150, image=start)
story_label = ttk.Label(text=story)
story_label.pack()
button = ttk.Button(text='Ask her how she codes?', command=code_act)
button.pack()
button_2 = ttk.Button(text='Tell her about Replit', command=replit_act)
button_2.pack()
button_3 = ttk.Button(text="She says 'I use a local editor'", command=edit_act)
button_4 = ttk.Button(text="She says 'I use Replit'", command=use_act)
button_5 = ttk.Button(text="You say 'I use Replit too'", command=alike_act)
button_6 = ttk.Button(
    text="You say 'I am actually going through 100 days of code right now'",
    command=celebrate_act
)
restart_button = ttk.Button(text='Restart', command=restart)

window.mainloop()
