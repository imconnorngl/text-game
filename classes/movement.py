from .rendering import Rendering

class Movement():
    def __init__(self, root, position):
        self.position = position
        self.rendering = Rendering(root, position)
        
    def moveBy(self, movement):
        self.position["x"] = self.position["x"] + movement["x"]
        self.position["y"] = self.position["y"] + movement["y"]
        self.rendering.update()