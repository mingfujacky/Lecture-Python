import tkinter as tk
import random

#define the action when clicking button
def change_fg_color():
    color = random.choice(['red', 'orange', 'yellow', 'blue', 'indigo', 'violet'])
    button["fg"] = color

#create window
window = tk.Tk()

# add button
button = tk.Button(text='Click me', command=change_fg_color)
button.pack()

# initializing window
window.mainloop()
