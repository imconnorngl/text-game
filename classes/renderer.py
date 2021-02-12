class Renderer:
    def __init__(self, rooms, position, room, stats):
        # Setup Default Variables

        self.stats = stats
        self.rooms = rooms
        self.position = position
        self.room = room

    def render(self):
        grid = ""
        for y in range(10, -1, -1):
            row = ""
            for x in range(10, -1, -1):
                currentPosition = { "x": x, "y": y }
                currentObject = next((x for x in self.room["objects"] if x["location"] == currentPosition), None)
                if currentPosition == self.position:
                    row += "O"
                elif currentObject:
                    if "requirement" not in currentObject:
                        row += "#"
                    elif "requirement" in currentObject and currentObject["requirement"] in self.stats["requirements"]:
                        row += "#"
                    else:
                        row += "X"
                else:
                    row += "X"
            grid += row
            grid += "\n"

        print(grid)