import npyscreen 
from npyscreen import Form


class LoginScreen(npyscreen.Form): 
    
    def create(self):
        self.loginInput = self.add(npyscreen.TitleText,name= "Login:", value= "---")
        self.passLabel = self.add(npyscreen.TitlePassword, name= "Pass:")
        self.confirmButton = self.add(npyscreen.ButtonPress, name= "Confirm", when_pressed_function= self.confirmButtonPress)
        self.display()
        self.edit()


    def confirmButtonPress(self):
        self.set_value({"login":self.loginInput.value, "password":self.passLabel.value})
        self.set_value({"login":open('./l.cfg', 'r').readline(), "password":open('./p.cfg', 'r').readline()})
        self.exit_editing()
    