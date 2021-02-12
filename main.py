from pynput.keyboard import Key, Listener
from classes.controller import Controller

controller = Controller()

with Listener(on_press=controller.onPress) as listener:
    listener.join()