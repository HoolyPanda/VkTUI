import os
from assets.View.DialogsBox import DialogsBox
from assets.Model import Quest
import assets.Model.Medic as Medic
import json

class QuestLoader():
    def __init__(self):
        self.quests = []
        self.LoadEvents()
        pass

    def LoadEvents(self):
        a =os.listdir("DataBase") 
        for questName in os.listdir("DataBase"):
            if os.path.exists("DataBase/" + questName.replace('.txt', '') + ".json"):
                newQuest = self.LoadEventFromJson(filePath= "DataBase/" + questName.replace('.txt', '') + ".json")
                self.quests.append(newQuest)
            else:
                newQuest = Quest.Quest(discriptionFile= questName.replace('.txt', ''))
            pass

    def LoadQuestList(self, targetWiget: DialogsBox):
        for quest in self.quests:
            if quest.discriptionFile:
                targetWiget._appendValue(quest.discriptionFile)
                # questDiscription = open(quest.discriptionFile + ".txt", 'r').read()

            # questDiscription = open(quest.)
            pass
            

    def LoadCharacter(self, nick= None, password= None):
        for character in os.listdir("Runners"):
            fs = open("Runners/" + character, "r")
            characterDump = json.load(fs)
            if characterDump['nick'] == nick and characterDump['password'] == password:
                return True
        return False

    def LoadEventFromJson(self, filePath):
        fs = open(filePath, 'r')
        rawJson = json.load(fs)
        quest = Quest.Quest(discriptionFile= filePath.replace('.json', '.txt'))
        for runner in rawJson["runners"]:
            if runner["gameClass"] == "Medic":
                runner = Medic.Medic(
                                    toolsLevel= runner["toolsLevel"], 
                                    nick= runner["nick"], 
                                    characterLevel= runner['characterLevel'],
                                    weaponType= runner["weaponType"]) 
            quest.AddRunner(runner)
        return quest
