from .renderer import Renderer

class Controller:
    def __init__(self, rooms):
        # Setup Default Variables
        self.rooms = rooms
        self.room = {}
        self.position = { "x": 0, "y": 0 }
        self.stats = {
            "requirements": []
        }

        # Load default room from config
        default = next((x for x in self.rooms if x["default"]), None)
        self.setupRoom(default)

        # Setup Renderer Class
        self.renderer = Renderer(self.room, self.position, self.room, self.stats)

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

        self.renderer.render()

    def setupRoom(self, room):
        self.position = room["spawn"]
        self.room = room
