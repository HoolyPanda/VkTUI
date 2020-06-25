import npyscreen

class AlertPopup(npyscreen.Popup):
    def create(self):
        # self.messageBox = self.add(npyscreen.TitleFixedText, relx= int(self.max_x / 5), rely= int(self.max_y/2),)
        self.messageBox = self.add(npyscreen.MultiLineEdit, value= "", relx= int(self.max_x / 5), rely= int(self.max_y/2), editable= False)
        # self.height = 20
        # self.message = "----"
        # b = self.add(npyscreen.Button, max_width= self.max_x, height= self.max_y)
        self.display()

    def DisplayText(self, text):
        self.messageBox = self.add(npyscreen.MultiLineEdit, value= text, relx= int(self.max_x / 5), rely= int(self.max_y/2), editable= False, max_length= len(text))
        self.display()
        pass