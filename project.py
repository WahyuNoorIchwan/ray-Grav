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

    # Method - Obj - Append Data
    def appendData(self, batch):
        self.properties = batch["properties"]
        self.grid = batch["grids"]

    # Method - Obj - Save Database
    def saveDatabase(self, filePath):
        # Compile Data
        batch = {}
        batch["properties"] = self.properties
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
            self.createProject()

    # Method New - Get File Path
    def getFilePath(self):
        title = "Save New Project As"
        wildcard = "Ray Database (*.rdb)|*.rdb"
        filepath = wx.FileDialog(self.mainWindow, title, wildcard=wildcard,
                                 style=wx.FD_SAVE)
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
    def createProject(self):
        # Get Project Name
        name = self.filePath.split()[-1]
        name = name.replace('\\', '/')
        name = name.split("/")[-1]

        # Properties
        properties = {"name": name}

        # Prepare Project and Data
        batch = {"properties": properties,
                 "grids": {}}

        project = Obj(self.mainWindow)
        project.appendData(batch)
        project.saveDatabase(self.filePath)

        # Store Project on Main Window
        self.mainWindow.project = project
        self.mainWindow.filePath = self.filePath

        # Set Main Window Title
        title = "Ray-Grav - {}".format(name)
        self.mainWindow.SetTitle(title)

# Class - Open Project
class Open:
    def __init__(self, main):
        self.mainWindow = main

        # Open and Confirm Data
        stats = self.readData()

        if stats:
            project = Obj(self.mainWindow)
            project.appendData(self.batch)
            project.showData()
            self.mainWindow.project = project

    # Method Open - Read and Validate Data
    def readData(self):
        filePath = "database.rdb"

        # Open Data
        file = open(filePath, "r")
        database = file.readlines()
        file.close()

        # Validate Data
        nChar = int(database[0])

        if len(database[1]) != nChar:
            stats = False
        else:
            # Try to Convert Data
            try:
                self.batch = eval(database[1])
            except:
                stats = False
            else:
                stats = True

        # Return Status
        return stats

# Class - Close - to Close Project
class Close:
    def __init__(self, main):
        self.mainWindow = main
        self.emptyTable()
        self.mainWindow.project = None

    # Method Close - Empty Table
    def emptyTable(self):
        table = self.mainWindow.dataTab.table
        nRow = table.GetNumberRows()
        table.DeleteRows(0, nRow)
        table.AppendRows(5)