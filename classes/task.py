import sys, time

class Tasks:
    def __init__(self, stats):
        self.stats = stats

        self.tasks = {
            "power_switch": self.power_switch,
            "check_phone": self.check_phone
        }

    def sendText(self, text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)

    def task(self, task):
        self.tasks[task]()

    def power_switch(self):
        input("PRESS ENTER TO TURN ON THE POWER")

    def check_phone(self):
        self.sendText("Anonymous: You are here because you hurt me young warrior. Fight your way out and I may let you go... Justice will be served...")
        response = input("You:\n\nA) Who are you?\nB) I did nothing?\nC) Why am I here?\n\nSELECT YOUR CHOICE")

        messages = { 
            "a": "I am your worst nightmare... Escape, though. and you'll be free.", 
            "b": "Of course you did nothing... It's always nothing from you people. You will learn.", 
            "c": "You need to prove that you are stronger than you proved yourself that day you broke my heart."
        }

        self.sendText("Anonymous: " + messages[response.lower()] if response.lower() in messages else "You chose not to answer me? Your unworthiness is undoubtable...")


        
        