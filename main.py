import tkinter as tk
from classes.controller import Controller
from functions.rendering import gridConstructor

root = tk.Tk()

controller = Controller(root, { "x": 0, "y": 0 })

root.bind('<KeyPress>', controller.onPress)
root.attributes('-fullscreen', True)

text = tk.Text(master=root, bg="black", fg="white")
text.pack(expand=True, fill='both')
text.insert(tk.END, "Press S to start.")

root.mainloop()