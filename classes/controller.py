class Controller:
    def __init__(self):
        self.position = { "x": 0, "y": 0 }
    
    def onPress(self, key):
        print(key)