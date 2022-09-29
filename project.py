import wx

# Class - Obj - to Save Project and other attributes
class Obj:
    def __init__(self, main):
        self.main = main
        self.mainWindow = self.main.main

class New:
    def __init__(self, main):
        self.mainWindow = main

        # Get File Path
        filePath = self.getFilePath()
        if filePath != "":
            self.newDialog()

    # Method New - Get File Path
    def getFilePath(self):
        title = "Open Gravity Data"
        wildcard = "Excel files (*.xlsx)|*.xlsx"
        filepath = wx.FileDialog(self.mainWindow, title, wildcard=wildcard,
                                 style=wx.FD_OPEN)
        filepath.ShowModal()
        return filepath.GetPath()

    # Method New - New Project Dialog
    def newDialog(self):
        None