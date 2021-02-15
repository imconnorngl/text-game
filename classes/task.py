class Tasks:
    def __init__(self, stats):
        self.stats = stats

        self.tasks = {
            "power_switch": self.power_switch
        }

    def task(self, task):
        self.tasks[task]()

    def power_switch(self):
        input("PRESS ENTER TO TURN ON THE POWER")