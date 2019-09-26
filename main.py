import npyscreen
import LoginScreen
import MainScreen
import AlertPopup


class VkTUI(npyscreen.NPSAppManaged):

    def main(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        LoginForm = self.addForm("LoginScreen", LoginScreen.LoginScreen)
        MainForm = self.addForm("MainScreen", MainScreen.MainScreen,)
        MainForm.SetScreenValue(LoginForm.value)
        # authResult = MainForm.Auth()
        authResult = None
        if authResult:
            alert = self.addForm("Alert", AlertPopup.AlertPopup)
            alert.DisplayText(authResult)
        else:
            MainForm.display()
            MainForm.edit()
        pass

if __name__ == "__main__":
    App = VkTUI()
    App.run()
