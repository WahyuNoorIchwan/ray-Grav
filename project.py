import wx, os
import pandas as pd

# Class - Obj - to Save Project and other attributes
class Obj:
    def __init__(self, main):
        self.mainWindow = main

        self.data = None
        self.properties = None
        self.grids = {}

    # Method - Obj - Show Data
    def showData(self):
        # Get Table from Data Tab
        table = self.mainWindow.dataTab.table
        data = self.data

        # Change Grid Size
        nRow = table.GetNumberRows()
        table.DeleteRows(0, nRow)
        table.AppendRows(len(data))

        # Set Cells Value
        row = 0
        for key, column in data.items():
            for col in range(5):
                value = str(column[col])
                table.SetCellValue(row, col, value)

            # Increase Row
            row += 1

    # Method - Obj - Save Database
    def saveDatabase(self, filePath):
        # Compile Data
        batch = {}
        batch["properties"] = self.properties
        batch["data"] = self.data
        batch["grids"] = self.grids

        batch = str(batch)
        nChar = len(batch)

        # Write File
        file = open(filePath, "w")
        file.write(str(nChar) + "\n")
        file.write(batch)
        file.close()

class New:
    def __init__(self, main):
        self.mainWindow = main

        # Get File Path
        self.filePath = self.getFilePath()
        if self.filePath != "":
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
        # Setup Dialog and Layout
        dialog = wx.Dialog(self.mainWindow)
        size = self.mainWindow.screenSize
        dialog.SetSize(370, 160)

        panel = wx.Panel(dialog)

        # Forms - Project Name Label
        text = wx.StaticText(panel, -1)
        text.SetLabel("Project Name")
        text.SetPosition((20, 23))

        self.nameForm = wx.TextCtrl(panel, -1, "Gravity Data")
        self.nameForm.SetSize(200, -1)
        self.nameForm.SetPosition((100, 20))

        # Forms - Save Project
        text = wx.StaticText(panel, -1)
        text.SetLabel("Save to")
        text.SetPosition((20, 53))

        defPath = os.getcwd() + "\database.rdb"
        self.saveForm = wx.TextCtrl(panel, -1, defPath)
        self.saveForm.SetSize(200, -1)
        self.saveForm.SetPosition((100, 50))

        button = wx.Button(panel, -1)
        button.SetLabel("S")
        button.SetSize((25, -1))
        button.SetPosition((310, 50))
        button.Bind(wx.EVT_BUTTON, self.getSavePath)

        # Create Button
        button = wx.Button(panel)
        button.SetLabel("Create")
        button.SetSize(60, -1)
        button.SetPosition((240, 80))
        button.Bind(wx.EVT_BUTTON, self.createProject)

        # Show Dialog
        dialog.ShowModal()

    # Method New - Save Path
    def getSavePath(self, event):
        title = "Save Data"
        wildcard = "Database (*.rdb)|*.rdb"
        filepath = wx.FileDialog(self.mainWindow, title, wildcard=wildcard,
                                 style=wx.FD_SAVE)
        filepath.ShowModal()

        # Set New Path
        newPath = filepath.GetPath()
        if newPath != "":
            self.saveForm.SetLabel(newPath)

    # Method New - Create Project
    def createProject(self, event):
        # Create Data - Open Data to Numpy
        data = pd.read_excel(self.filePath).to_numpy()

        # Create Data - Convert to Dictionary
        n_data = len(data)
        data = {str(i).zfill(5): list(data[i, :])
                for i in range(n_data)}

        # Properties
        properties = {"name": self.nameForm.GetValue()}

        # Create Project Object
        project = Obj(self.mainWindow)
        project.data = data
        project.properties = properties

        # Show Loaded Data
        project.showData()

        # Save Database File
        project.saveDatabase(self.saveForm.GetValue())