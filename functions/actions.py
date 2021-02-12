from .rendering import gridConstructor

def pickUp(self):
    if self.started:
        print(self.position)

def startGame(self):
    if not self.started:
        for widget in self.root.winfo_children(): 
            widget.destroy()

        self.started = True
        gridConstructor(self.root, self.position)