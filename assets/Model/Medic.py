from assets.Model.Player import Player

class Medic(Player):

    def __init__(self, armorLevel = None, toolsLevel = None, characterLevel = None, nick= None, weaponType = None, gameClass = None):
        self.nick = nick
        self.password = None
        self.gameClass = gameClass
        self.armorLevel = armorLevel
        self.toolsLevel = toolsLevel
        self.characterLevel = characterLevel
        self.weaponType = weaponType
        pass