import sys, time
from .tasks.switch import Switch

class Tasks:
    def __init__(self, stats):
        self.tasks = {
            "power_switch": self.power_switch,
            "check_phone": self.check_phone,
            "fight_captor": self.fight_captor
        }

    # Task Executer
    def task(self, task, stats):
        return self.tasks[task](stats)

    # Power Switch
    def power_switch(self, stats):
        Switch()
        input("PRESS ENTER TO TURN ON THE POWER")
        return stats

    # Phone Task
    def check_phone(self, stats):
        self.sendText("Anonymous: You are here because you hurt me young warrior. Fight your way out and I may let you go... Justice will be served...")
        response = input("You:\n\nA) Who are you?\nB) I did nothing?\nC) Why am I here?\n\nSELECT YOUR CHOICE\n\n")

        messages = { 
            "a": { "message": "I am your worst nightmare... Escape, though. and you'll be free.", "health": 0 }, 
            "b": { "message": "Of course you did nothing... It's always nothing from you people. You will learn.", "health": -50 }, 
            "c": { "message": "You need to prove that you are stronger than you proved yourself that day you broke my heart.", "health": 0 }
        }

        self.sendText("Anonymous: " + messages[response.lower()]["message"] if response.lower() in messages else "You chose not to answer me? Your unworthiness is undoubtable..." + "\n")
        
        health = messages[response.lower()]["health"] if response.lower() in messages else -100
        print("You chose the wrong answer and lost health..." if health < 0 else "You chose wisely and did not lose health...")
        print((str(health) + " health") if health < 0 else "")
        stats["health"] += health
        return stats

    def fight_captor(self, stats):
        #Fight()
        input("PRESS ENTER TO END FIGHT SCENE")
        return stats

    # Extra Utils
    def sendText(self, text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)