import wx
import wx.grid as grid

class Tab(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set Layout
        self.layout = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.layout)

        # Create Table
        self.table = Table(self)
        self.table.setup(self)
        self.layout.Add(self.table, 1, wx.EXPAND)

# Class - Table - to Show Data
class Table(grid.Grid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, mainWindow):
        self.mainWindow = mainWindow

        # Setup Table Size
        self.CreateGrid(10, 5)

        # Set Column Header
        self.header = ["Station", "x", "y", "z", "CBA"]

        for i in range(len(self.header)):
            self.SetColLabelValue(i, self.header[i])
            self.SetColSize(i, 100)