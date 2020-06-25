import npyscreen
import ChatBox
import os
        

class DialogsBox(npyscreen.BoxTitle):
   
    def when_value_edited(self):
        if self.value is not None:
            if self.value == 1:
                os.system('vim')

            a = self.find_parent_app()
            a.MainForm.DISPLAY()
            a.MainForm._widgets_by_id[1].values.append('dfsfsdfdsfd\nfsdfsdf')
            self.chatBox.value = 'dfasdfasfas'
            a.MainForm._widgets_by_id[1].name = self.values[self.value]
            a.MainForm._widgets_by_id[1].display()
        self.parent.display()
        self.display()

    def when_cursor_moved(self):
        # TODO: change prewiev on chatbox
        a = self._my_widgets[0].cursor_line
        self.chatBox.name =  f'{self.values[a]} preview'
        self.chatBox.display()

    def _setValues(self, values, chatBox = None):
        self.values = values
        if chatBox:
            self.chatBox = chatBox

    def setChatBox(self, chatBox: ChatBox.ChatBox):
        self.chatBox = chatBox

    def create(self):
        pass