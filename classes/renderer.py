from .task import Tasks

import time, random

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
            if "trap" in currentObject: self.stats["health"] -= random.randint(5, 25)
            else:
                if "func" in currentObject: self.stats = self.tasks.task(currentObject["func"], self.stats)

                # Gives the user any rewards the object offers
                if "rewards" in currentObject: self.stats["requirements"].append(currentObject["rewards"])

                # Gives the user any items the object offers
                if "item" in currentObject: self.stats["inventory"].append(currentObject["item"])

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

            if self.stats["health"] <= 0:
                gameover = open('config/art/gameover.txt').read().splitlines()

                for line in gameover:
                    print(line)
                    time.sleep(0.1)

                time.sleep(1)
                print("You lost all your health...")
                exit()
            elif "captor_fought" in self.stats["requirements"]:
                title = open('config/art/win.txt').read().splitlines()

                for line in title:
                    print(line)
                    time.sleep(0.1)

                time.sleep(1)
                print("You finished with a health of " + str(self.stats["health"]))
                exit()

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
                    row += " O "
                elif currentObject:
                    if "requirement" not in currentObject:
                        row += " # "
                    elif "requirement" in currentObject and currentObject["requirement"] in self.stats["requirements"]:
                        row += " # "
                    else:
                        row += " X "
                else:
                    row += " X "
            grid += row
            grid += "\n"
        print("Your health is " + str(self.stats["health"]))
        print(grid)
        return self.position