import npyscreen
# import npy
# npyscreen
import LoginScreen
import MainScreen
import AlertPopup


class VkTUI(npyscreen.NPSAppManaged):

    def main(self):
        
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        self.LoginForm = self.addForm("LoginScreen", LoginScreen.LoginScreen)
        self.MainForm = self.addForm("MainScreen", MainScreen.MainScreen)
        self.MainForm.SetScreenValue(self.LoginForm.value)
        self.MainForm.name = 'MAiN'
        authResult = self.MainForm.Auth()
        if authResult:
            alert = self.addForm("Alert", AlertPopup.AlertPopup)
            alert.DisplayText(authResult)
            alert.edit()
        else:
            self.MainForm.display()
            self.MainForm.edit()
        pass


if __name__ == "__main__":
    App = VkTUI()
    App.run()
