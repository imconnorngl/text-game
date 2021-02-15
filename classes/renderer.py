from .task import Tasks

import time

class Renderer:
    def __init__(self, rooms, position, room, stats):
        # Setup Default Variables

        self.stats = stats
        self.rooms = rooms
        self.position = position
        self.room = room
        self.tasks = Tasks(self.stats)

    # Changes the room which the user is located in
    def changeRoom(self, room, position = {}):
        self.room = room

        if bool(position): self.position = position
        else: self.position = room["spawn"]

        return self.room

    # Renders the interactive display for the user
    def render(self):
        currentObject = next((x for x in self.room["objects"] if x["location"] == self.position), None)

        if currentObject and currentObject["location"] == self.position:
            self.sendGrid()
            
            self.stats["movement"] = False

            # Displays the prompts for an event
            for prompt in currentObject["prompts"]:
                print(prompt)
                time.sleep(1)

            # Executes the function for an event
            if "func" in currentObject: self.tasks.task(currentObject["func"])

            # Gives the user any rewards the object offers
            if "rewards" in currentObject: self.stats["requirements"].append(currentObject["rewards"])

            # Moves the user to any room the object offers
            if "travel" in currentObject:
                room = next((x for x in self.rooms if x["identifier"] == currentObject["travel"]["room"]), None)
                
                if bool(room):
                    if "position" in currentObject["travel"]:
                        self.changeRoom(room, currentObject["travel"]["position"])
                    else: 
                        self.changeRoom(room)
                else:
                    print("This door lead nowhere...")

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