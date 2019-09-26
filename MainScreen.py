import npyscreen
import ChatBox
import DialogsBox
import os

class MainScreen(npyscreen.Form):

    def SetScreenValue(self, value):
        self.set_value(value)

    def getQuests(self):
        quests = []
        for quest in os.listdir("./DataBase"):
            quests.append(quest)
        return quests

    def create(self):
        self.dialogsBox = self.add(DialogsBox.DialogsBox, name= "Dialogs", max_width= int(self.max_x /4) - 3,)
        self.chatBox = self.add(ChatBox.ChatBox, name= "Chat", relx= int(self.max_x / 4) + 2, rely= self.dialogsBox.rely, )
        self.dialogsBox.setChatBox(self.chatBox)
        quests = self.getQuests()
        self.dialogsBox._setValues(quests)
        pass
