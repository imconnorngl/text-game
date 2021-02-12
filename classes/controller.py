from .movement import Movement
from functions.actions import pickUp, startGame

class Controller():
    def __init__(self, root, position):
        self.position = position
        self.started = False
        self.root = root
        self.movement = Movement(root, self.position) 
        
        self.directions = {
            "up": { "x": 0, "y": 1},
            "down": { "x": 0, "y": -1},
            "left":  { "x": -1, "y": 0},
            "right": { "x": 1, "y": 0},
        }

        self.actions = {
            "p": pickUp,
            "s": startGame
        }

    def onPress(self, event):
        if event.keysym.lower() in self.directions:
            if self.started: self.movement.moveBy(self.directions[event.keysym.lower()])
        elif event.keysym.lower() in self.actions:
            self.actions[event.keysym.lower()](self)