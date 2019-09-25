import npyscreen
import vk_api
import ChatBox
import DialogsBox

class MainScreen(npyscreen.Form):

    def Auth(self):
        # autorization
        pass

    def SetScreenValue(self, value):
        self.set_value(value)

    def create(self):
        # dialogBoxX = self.ma
        self.dialogsBox = self.add(DialogsBox.DialogsBox, name= "Dialogs", max_width= int(self.max_x /4) - 3,)
        self.chatBox = self.add(ChatBox.ChatBox, name= "Chat", relx= int(self.max_x / 4) + 2, rely= self.dialogsBox.rely, )
        self.dialogsBox._setValues(["Dialog1", "Dialog2", "Dialog3"], chatBox= self.chatBox)
        self.display()
        pass
