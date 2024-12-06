import tkinter as tk
window = tk.Tk()
window.title("Getting Textvariable from Entry")

text_variable = tk.StringVar()
entry = tk.Entry(window, textvariable=text_variable)
entry.pack()

entered_text = text_variable.get()
print("Entered text:", entered_text)
def retrieve_text():
   # Retrieve the text from the textvariable
   entered_text = text_variable.get()
   print("Entered text:", entered_text)

# Create a button to trigger text retrieval
button = tk.Button(window, text="Retrieve Text", command=retrieve_text)
button.pack()
window.mainloop()