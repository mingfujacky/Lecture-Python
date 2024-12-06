import tkinter as tk
import random

#define the action when clicking button
def roll():
    num = random.randint(1,6)
    lbl_result['text']=str(num)

#create window
window = tk.Tk()
window.rowconfigure([0,1], minsize=50)

window.columnconfigure(0, minsize=150)

# add button and label
btn_roll = tk.Button(text='Roll', command=roll)
lbl_result = tk.Label()

# put button and label
btn_roll.grid(row=0, column=0, sticky='nsew')
lbl_result.grid(row=1, column=0, sticky='nsew')

# initializing window
window.mainloop()