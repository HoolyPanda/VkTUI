import npyscreen
from assets.Control import DataBaseController as DBC
from assets.View import ChatBox


class DialogsBox(npyscreen.BoxTitle):
   
    def when_value_edited(self):
        self.dataBaseController = DBC.DataBaseController()
        if self.value is not None:
            self.chatBox.name = self.values[self.value]
            self.chatBox.values = "ddddd"
            self.dataBaseController.displayQuestDiscription(questDiscriptionFile= self.chatBox.name, wiget= self.chatBox)
            self.chatBox.display()

        self.display()

    def _setValues(self, values: []):
        self.values = values
        self.display()

    def _setValues(self, values: {}):
        for questName in values.keys():
            self.values.append(questName)
        self.display()
        pass

    def _appendValue(self, value: str):
        self.values.append(value)

    def bindChatBox(self, chatBox: ChatBox.ChatBox):
        self.chatBox = chatBox

    def create(self):
        pass