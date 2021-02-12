class Controller:
    def __init__(self):
        self.position = { "x": 0, "y": 0 }
    def onPress(self, key):
        try:
            k = key.char
        except:
            k = key.name

        if k in ['left', 'right', 'up', 'down']:
            directions = {
                "left": { "x": 1, "y": 0 },
                "right": { "x": -1, "y": 0 },
                "up": { "x": 0, "y": 1 },
                "down": { "x": 0, "y": -1 },
            }

            self.moveBy(directions[k])
    
    def moveBy(self, movement):
        self.position["x"] += movement["x"]
        self.position["y"] += movement["y"]

        print(self.position)