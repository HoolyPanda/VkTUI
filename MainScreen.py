import curses.ascii
import vkAPI
import npyscreen
import ChatBox
import DialogsBox
import vk_api

class MainScreen(npyscreen.Form):

    def Auth(self):
        # autorization

        self.session = vk_api.VkApi(
            login=self.value["login"],
            password=self.value["password"],
            # scope='messages',
            app_id=7102642
        )
        try:
            self.session.auth(reauth= True)
        except Exception as e:
            return str(e)
        pass
        self.supervisor = vkAPI.VkSuperviser(session=self.session)
        self.LoadDialogs()

    def SetScreenValue(self, value):
        self.set_value(value)

    def LoadDialogs(self):
        dialogs = self.supervisor.getDialogs()
        self.dialogsBox._setValues(["Dialog1", "Dialog2", "Dialog3"], chatBox= self.chatBox)
        pass

    def create(self):
        # self.add_handlers({'h': self.h_exit_down})
        self.dialogsBox = self.add(DialogsBox.DialogsBox, name= "Dialogs", max_width= int(self.max_x /4) - 3,)
        self.chatBox = self.add(ChatBox.ChatBox, name= "Chat", relx= int(self.max_x / 4) + 2, rely= self.dialogsBox.rely, )
        pass
