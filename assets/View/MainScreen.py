import npyscreen
from assets.View import ChatBox
from assets.View import DialogsBox
import os
import assets.Control.DataBaseController as DataBaseController


class MainScreen(npyscreen.Form):

    def SetScreenValue(self, value):
        self.set_value(value)

    def create(self):
        dataBaseController = DataBaseController.DataBaseController()
        self.dialogsBox = self.add(DialogsBox.DialogsBox, name= "Dialogs", max_width= int(self.max_x /4) - 3,)
        self.chatBox = self.add(ChatBox.ChatBox, name= "Chat", relx= int(self.max_x / 4) + 2, rely= self.dialogsBox.rely, )
        self.dialogsBox.bindChatBox(self.chatBox)
        dataBaseController.LoadQuestsToWiget(self.dialogsBox)
        pass

