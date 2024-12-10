import tkinter as tk
window = tk.Tk()

window.columnconfigure([0, 1, 2], weight=1, minsize=80)
window.rowconfigure([0, 1, 2], weight=1, minsize=60)

for i in range(3):
    
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=2,
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame,
                         text=f'Row {i}\nColumn {j}',
                )
        label.pack(padx=5, pady=5)
       
window.mainloop()       