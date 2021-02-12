import tkinter as tk
from functions.rendering import gridConstructor

class Rendering():
    def __init__(self, root, position):
        self.position = position
        self.root = root
        
    def update(self):
        for widget in self.root.winfo_children(): 
            widget.destroy()

        gridConstructor(self.root, self.position)