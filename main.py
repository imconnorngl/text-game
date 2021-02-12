from pynput.keyboard import Key, Listener
from classes.controller import Controller
import json

with open('config/rooms.json') as jsonFile:
    rooms = json.loads(jsonFile.read())

controller = Controller(rooms)

with Listener(on_press=controller.onPress) as listener:
    listener.join()