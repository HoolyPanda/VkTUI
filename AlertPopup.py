import npyscreen

class AlertPopup(npyscreen.MessagePopup):
    def create(self):
        # self.messageBox = self.add(npyscreen.TitleFixedText,)# relx= int(self.max_x / 5), rely= int(self.max_y/2),)
        # b = self.add(npyscreen.Button)
        pass

    def DisplayText(self, text):
        # self.messageBox.set_value(text)
        # self.messageBox.display()
        self.set_value(text)
        self.display()