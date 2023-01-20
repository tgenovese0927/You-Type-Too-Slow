from tkinter import *

timer = None


def not_typing():
    user_entry.delete(1.0, END)
    user_entry.insert(END, "Too Slow!")


def start_timer(event=None):
    global timer
    if timer is not None:
        window.after_cancel(timer)

    timer = window.after(5000, not_typing)


window = Tk()
window.title('Type Before Your Text Disappears')
window.config(padx=100, pady=40)

canvas = Canvas(width=400, height=300, bg='#808080', highlightthickness=0)

title_label = Label(text="Start Typing. Stop and it's Gone!")
title_label.grid(column=1, row=0)

user_entry = Text(width=75)
user_entry.grid(column=1, row=1)

window.bind_all('<Any-KeyPress>', start_timer)
window.bind_all('<Any-ButtonPress>', start_timer)

window.mainloop()
