from pynput.keyboard import Key, Listener
from classes.controller import Controller
import json, time

with open('config/rooms.json') as jsonFile:
    rooms = json.loads(jsonFile.read())

introduction = [
    "You wake up in a strange place...",
    "Light streaks through the slitted windows...",
    "You need to find a way out, you must, it's a neccessity."
]

for line in introduction:
    print(line)
    time.sleep(1)

title = open('config/art/title.txt').read().splitlines()

for line in title:
    print(line)
    time.sleep(0.1)

time.sleep(2)

controller = Controller(rooms)

with Listener(on_press=controller.onPress) as listener:
    listener.join()