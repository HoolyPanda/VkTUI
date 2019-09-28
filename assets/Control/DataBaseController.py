from assets.Model.EventLoader import QuestLoader

class DataBaseController():
    def __init__(self):
        self.data = ""
        self.questLoader = QuestLoader()
        pass

    def AuthorizePlayer(self, _nick = None, _password = None):
        return self.questLoader.LoadCharacter(nick = _nick, password = _password)

    def LoadQuestsToWiget(self, wiget):
        self.questLoader.LoadEventsToWiget(targetWiget= wiget)