class Renderer:
    def __init__(self, rooms, position, room, stats):
        # Setup Default Variables

        self.stats = stats
        self.rooms = rooms
        self.position = position
        self.room = room

    # Changes the room which the user is located in
    def changeRoom(self, room):
        self.room = room
        self.position = room["spawn"]
        return self.position

    # Renders the interactive display for the user
    def render(self):
        currentObject = next((x for x in self.room["objects"] if x["location"] == self.position), None)

        if currentObject and currentObject["location"] == self.position:
            self.sendGrid()
            
            self.stats["movement"] = False

            # Executes the event which is required to occur at the location
            print("Press ENTER to move onto the next prompt.")
            for prompt in currentObject["prompts"]:
                input(prompt)
        
            # Gives the user any rewards the object offers
            if "rewards" in currentObject: self.stats["requirements"].append(currentObject["rewards"])

            # Moves the user to any room the object offers
            if "travel" in currentObject:
                room = next((x for x in self.rooms if x["identifier"] == currentObject["travel"]), None)
                self.changeRoom(room)

            self.stats["movement"] = True

            return self.sendGrid()
        else:
            return self.sendGrid()

    # Sends the grid of the users current location
    def sendGrid(self):
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
        return self.position