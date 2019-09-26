import npyscreen

class AlertPopup(npyscreen.Popup):

    def create(self):
        self.messageBox = self.add(npyscreen.MultiLineEdit, relx= int(self.max_x / 5), rely= int(self.max_y/2), editable= False)
        self.display()

    def DisplayText(self, text):
        self.messageBox.value = text
        self.messageBox.display()
        self.edit()
        pass