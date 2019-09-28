import npyscreen
import assets.View.LoginScreen
import assets.View.MainScreen
import assets.View.AlertPopup
import assets.Control.DataBaseController as DataBaseController

class VkTUI(npyscreen.NPSAppManaged):

    def main(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        LoginForm = self.addForm("LoginScreen", assets.View.LoginScreen.LoginScreen)
        dBC = DataBaseController.DataBaseController()

        nick= LoginForm.value['nick']
        password= LoginForm.value['password']
        authResult = dBC.AuthorizePlayer(_nick= nick, _password= password)
        if authResult:
            MainForm = self.addForm("MainScreen", assets.View.MainScreen.MainScreen,)
            # MainForm.SetScreenValue(LoginForm.value)
            MainForm.display()
            MainForm.edit()
        else:
            assets.View.AlertPopup.AlertPopup().DisplayText("Acess Denied")
            self.main()
        pass
