import npyscreen 
from npyscreen import Form


class LoginScreen(npyscreen.Form): 

    def create(self):
        self.loginInput = self.add(npyscreen.TitleText,name= "Login:", value= "MazaHacka")
        self.passLabel = self.add(npyscreen.TitlePassword, name= "Pass:")
        self.confirmButton = self.add(npyscreen.ButtonPress, name= "Confirm", when_pressed_function= self.confirmButtonPress)
        self.display()
        self.edit()

    def confirmButtonPress(self):
        self.set_value({"nick":self.loginInput.value, "password":self.passLabel.value})
        self.exit_editing()
    