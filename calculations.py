import numpy as np
import wx

# Class - Gridding
class gridding:
    def __init__(self, mainWindow, data):
        self.mainWindow = mainWindow
        self.data = data

    # Method Gridding - Calculate Grid Size
    def cal_grid_size(self):
        # Data range
        xrange = max(self.data[:, 0]) - min(self.data[:, 0])
        yrange = max(self.data[:, 1]) - min(self.data[:, 0])

        d = max(xrange/100, yrange/100)

    # Method Gridding - Parameters Dialog
    def parametersDialog(self):
        dialog = wx.Dialog(self.mainWindow)
        dialog.SetSize(210, 250)

        # Grid Size
        text = wx.StaticText(dialog, -1)
        text.SetLabel("Grid Size")
        text.SetPosition((20, 20))

        self.gridSize = wx.SpinCtrl(dialog, -1)
        self.gridSize.SetSize((150, -1))
        self.gridSize.SetPosition((20, 40))

        # Grid Dimension
        text = wx.StaticText(dialog, -1)
        text.SetLabel("Grid Dimension")
        text.SetPosition((20, 80))

        text = wx.StaticText(dialog, -1)
        text.SetLabel("nx")
        text.SetPosition((20, 100))

        self.nxLabel = wx.StaticText(dialog, -1)
        self.nxLabel.SetLabel("100")
        self.nxLabel.SetPosition((70, 100))

        text = wx.StaticText(dialog, -1)
        text.SetLabel("ny")
        text.SetPosition((20, 120))

        self.nyLabel = wx.StaticText(dialog, -1)
        self.nyLabel.SetLabel("100")
        self.nyLabel.SetPosition((70, 120))

        text = wx.StaticText(dialog, -1)
        text.SetLabel("total")
        text.SetPosition((20, 140))

        self.nLabel = wx.StaticText(dialog, -1)
        self.nLabel.SetLabel("10000")
        self.nLabel.SetPosition((70, 140))

        dialog.ShowModal()