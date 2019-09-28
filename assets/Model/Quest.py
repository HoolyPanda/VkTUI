from assets.Model.Player import Player
from assets.Model import Medic
# from assets.Model import 

class Quest():
    def __init__(self, discriptionFile = None):
        self.discriptionFile = discriptionFile
        self.runners = []

    
    def AddRunner(self, runner: Player):
        if runner not in self.runners:
            self.runners.append(runner)
        pass

    def RemoveRunner(self, runner: Player):
        if runner in self.runners:
            self.runners.pop(self.runners.remove(runner))