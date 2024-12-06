import tkinter as tk
window = tk.Tk()

a = tk.StringVar()
a.set('')

ent_string = tk.Entry(textvariable=a)
lbl_result = tk.Label(textvariable=a)

ent_string.pack()
lbl_result.pack()

window.mainloop()