import random, time

class Fight:
    def __init__(self, stats):
        self.stats = stats
        self.boss = { 
            "health": 100 
        }

        self.moves = [
            { "name": "Kick", "file": "1", "damage": 20 },
            { "name": "Side Punch", "file": "2", "damage": 5 },
            { "name": "Forward Punch", "file": "3", "damage": 10 },
            { "name": "Sucker Punch", "file": "4", "damage": 25 },
        ]

        if "stick" in self.stats["inventory"]: self.moves.append({ "name": "Stick Hit", "file": "5", "damage": 40 })

    def startFight(self):
        while True:
            self.playerHit()
            time.sleep(2)
            self.bossHit()
            if self.stats["health"] <= 0:
                return self.stats
            elif self.boss["health"] <= 0:
                return self.stats

    def playerHit(self):
        string = ""
        for move in self.moves:
            string += move["file"] + ". " + move["name"] + "\n"
        print("\n\n" + string)
        move = input("SELECT A MOVE\n\n")

        try: 
            index = int(move) - 1
            move = self.moves[index]
        except:
            move = None
        
        if move is not None:
            art = open('config/art/movement/' + move["file"] + '.txt').read().splitlines()
            print("\n".join(art))
            print("You did a " + move["name"] + " and the enemy lost " + str(move["damage"]))
            self.boss["health"] -= move["damage"]
        else:
            print("You didn't choose your move wisely... Skipped.")
        self.display()

    def bossHit(self):
        index = random.randint(0, 3)
        move = self.moves[index]
        art = open('config/art/movement/' + move["file"] + '.txt').read().splitlines()
        print("\n".join(art))
        print("The enemy did a " + move["name"] + " and you lost " + str(move["damage"]))
        self.stats["health"] -= move["damage"]
        self.display()

    def display(self):
        print("Your health is", self.stats["health"])
        print("The bosses health is", self.boss["health"])