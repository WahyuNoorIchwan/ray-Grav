import wx, calculations
import wx.grid as grid
import numpy as np

class Tab(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, mainWindow):
        self.mainWindow = mainWindow

        # Set Layout
        self.layout = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.layout)

        # Visualize Button
        self.viz_butt = wx.Button(self)
        self.viz_butt.SetLabel("Visualize")
        self.viz_butt.SetSize(150, -1)

        self.layout.Add(self.viz_butt, 0.2, wx.ALIGN_RIGHT)
        self.viz_butt.Bind(wx.EVT_BUTTON, self.visualize)

        # Create Table
        self.table = Table(self)
        self.table.setup(self)
        self.layout.Add(self.table, 0.8, wx.EXPAND)

    # Method Tab - Visualize - Visualize CBA data
    def visualize(self, event):
        # Gridding - Prepare Data
        data = self.mainWindow.project.data
        data = [value for value in data.values()]
        data = np.array(data)

        grid = calculations.gridding(self.mainWindow, data)
        grid.parametersDialog()

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