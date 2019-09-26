from assets.Player import Player

class Event():
    def __init__(self):
        self.discriptionPath = None
        self.runners = []

    
    def AddRunner(self, runner: Player):
        if runner not in self.runners:
            self.runners.append(runner)
        pass