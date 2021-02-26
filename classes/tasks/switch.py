from pynput.keyboard import Key, Listener

class Switch:
    def __init__(self):
        self.grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 3, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        def getPosition(grid, search):
            for i, e in enumerate(grid):
                try: return { "x": i, "y": e.index(search) }
                except ValueError: pass

        self.position = getPosition(self.grid, 2)

        self.render()
        with Listener(on_press=self.press) as listener:
            listener.join()

    def render(self):
        print(self.position)

    def press(self, key):
        try: k = key.char
        except: k = key.name


        if k in ['left', 'right', 'up', 'down']:
            directions = {
                "left": { "x": 1, "y": 0 },
                "right": { "x": -1, "y": 0 },
                "up": { "x": 0, "y": 1 },
                "down": { "x": 0, "y": -1 },
            }

            return self.move(directions[k])
 
    def move(self, movement):
        positionTrait = self.grid[self.position["x"] + movement["x"]][self.position["y"] + movement["y"]]
        if positionTrait == 0 or positionTrait == 2:
            self.position["x"] += movement["x"]
            self.position["y"] += movement["y"]

            self.render()
        elif positionTrait == 3:
            return False