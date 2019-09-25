import npyscreen
import vk_api
import ChatBox
import DialogsBox
import vk_api

class MainScreen(npyscreen.Form):

    def Auth(self):
        # autorization
        self.session = vk_api.VkApi(
            login=self.value["login"],
            password=self.value["password"],
            app_id=6715195
        )
        try:
            self.session.auth(reauth= True)
        except Exception as e:
            return str(e)
        pass

    def SetScreenValue(self, value):
        self.set_value(value)

    def create(self):
        # dialogBoxX = self.ma
        self.dialogsBox = self.add(DialogsBox.DialogsBox, name= "Dialogs", max_width= int(self.max_x /4) - 3,)
        self.chatBox = self.add(ChatBox.ChatBox, name= "Chat", relx= int(self.max_x / 4) + 2, rely= self.dialogsBox.rely, )
        self.dialogsBox._setValues(["Dialog1", "Dialog2", "Dialog3"], chatBox= self.chatBox)
        pass
