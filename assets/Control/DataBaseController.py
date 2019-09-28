from assets.Model.EventLoader import QuestLoader
from assets.View.ChatBox import ChatBox


class DataBaseController():
    def __init__(self):
        self.data = ""
        self.questLoader = QuestLoader()
        pass

    def AuthorizePlayer(self, _nick = None, _password = None):
        return self.questLoader.LoadCharacter(nick = _nick, password = _password)

    def LoadQuestsToWiget(self, wiget):
        self.questLoader.LoadQuestList(targetWiget= wiget)

    def displayQuestDiscription(self, questDiscriptionFile: str, wiget: ChatBox):
        self.questLoader.LoadQuestData(filePath= questDiscriptionFile, targetWiget= wiget)
        pass