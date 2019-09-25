import npyscreen
import LoginScreen
import MainScreen

class VkTUI(npyscreen.NPSAppManaged):

    def main(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        # LoginForm = self.addForm("LoginScreen", LoginScreen.LoginScreen)
        MainForm = self.addForm("MainScreen", MainScreen.MainScreen, colums= 2, rows= 1)
        MainForm.edit()
        pass


if __name__ == "__main__":
    App = VkTUI()
    App.run()
