import npyscreen
import ChatBox


class DialogsBox(npyscreen.BoxTitle):
   
    def when_value_edited(self):
        if self.value is not None:
            self.chatBox.name = self.values[self.value]
            self.chatBox.display()
        self.display()

    def _setValues(self, values):
        self.values = values

    def setChatBox(self, chatBox: ChatBox.ChatBox):
        self.chatBox = chatBox

    def create(self):
        pass