from .renderer import Renderer

class Controller:
    def __init__(self, rooms):
        # Setup Default Variables
        self.rooms = rooms
        self.room = next((x for x in self.rooms if x["default"]), None)
        self.position = { "x": 0, "y": 0 }
        self.stats = {
            "movement": True,
            "requirements": []
        }

        # Setup Renderer Class
        self.renderer = Renderer(self.rooms, self.position, self.room, self.stats)

        self.room = self.renderer.changeRoom(self.room)
        self.position = self.renderer.render()

    # Define the onPress function which handles key presses
    def onPress(self, key):
        try: k = key.char
        except: k = key.name

        if self.stats["movement"] and k in ['left', 'right', 'up', 'down']:
            directions = {
                "left": { "x": 1, "y": 0 },
                "right": { "x": -1, "y": 0 },
                "up": { "x": 0, "y": 1 },
                "down": { "x": 0, "y": -1 },
            }

            self.moveBy(directions[k])

    # Define the moveBy function which handles movement of the player
    def moveBy(self, movement):
        if self.position["x"] +movement["x"] > 10 or self.position["x"] + movement["x"] < 0 or self.position["y"] +movement["y"] > 10 or self.position["y"] + movement["y"] < 0:
            print("You walk into a wall... Find a door to exit this room...")
        else:
            self.position["x"] += movement["x"]
            self.position["y"] += movement["y"]

            self.position = self.renderer.render()