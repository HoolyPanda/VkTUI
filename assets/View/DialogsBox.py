import npyscreen
from assets.View import ChatBox


class DialogsBox(npyscreen.BoxTitle):
   
    def when_value_edited(self):
        if self.value is not None:
            self.chatBox.name = self.values[self.value]
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