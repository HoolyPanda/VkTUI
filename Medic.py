from assets.Player import Player

class Medic(Player):

    def __init__(self, armorLevel = None, toolsLevel = None, characterLevel = None, name= None, weaponType = None):
        self.armorLevel = armorLevel
        self.toolsLevel = toolsLevel
        self.characterLevel = characterLevel
        self.name = name
        self.weaponType = weaponType
        pass