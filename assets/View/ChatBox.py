import npyscreen

class ChatBox(npyscreen.BoxTitle):

    def setData(self):
        self.values = ["1","3"]

    def create(self):
        # a = npyscreen.MultiLieEdit(screen= self, relx= int(self.max_x / 5), rely= int(self.max_y/2), editable= False)
        # self._contained_widget = a
        self.display()

    def DisplayText(self, text):
        self.value = text
        self.display()
        self.edit()
        pass