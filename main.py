import wx, data, visualization, project

# Main Window Class
class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Screen Size - Depend on Laptop
        display = wx.Display(0)
        self.screenSize = display.GetGeometry().GetSize()
        self.SetSize(self.screenSize[0], self.screenSize[1])

        # Main Widget
        self.mainWidget = wx.Panel(self)
        self.mainLayout = wx.BoxSizer(wx.VERTICAL)
        self.mainWidget.SetSizer(self.mainLayout)

        # Create Layout
        self.create_layout()

    # Method Main - Create Layout
    def create_layout(self):
        # Menu Bar
        self.menuBar = menuBar()
        self.menuBar.setup(self)
        self.SetMenuBar(self.menuBar)

        # Tabs
        container = wx.Notebook(self.mainWidget)
        self.mainLayout.Add(container, 25)

        self.dataTab = data.Tab(container)
        container.AddPage(self.dataTab, "Processing")

        self.visTab = visualization.Tab(container)
        self.visTab.setup(self)
        container.AddPage(self.visTab, "Visualization")

        # Footer
        self.footer = Footer(self.mainWidget)
        self.footer.setup(self)
        self.mainLayout.Add(self.footer, 1, wx.EXPAND)

# Class - Menu Bar
class menuBar(wx.MenuBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mainWindow = None

    def setup(self, mainWindow):
        self.mainWindow = mainWindow

        # Create Menus
        self.create_menus()

    # Method Menu Bar - Create Menus
    def create_menus(self):
        # File Menu
        self.file = wx.Menu()
        self.Append(self.file, "&File")

        # File Menu - New Project
        self.new = self.file.Append(-1, "New Project")

        func = lambda event: project.New(self.mainWindow)
        self.mainWindow.Bind(wx.EVT_MENU, func, self.new)

        # File Menu - Open Project
        self.open = self.file.Append(-1, "Open Project")

        func = lambda event: print(text)
        self.mainWindow.Bind(wx.EVT_MENU, func, self.open)

        # Edit Menu
        self.edit = wx.Menu()
        self.Append(self.edit, "&Edit")

        # Filter Menu
        self.filter = wx.Menu()
        self.Append(self.filter, "&Filter")

        # Tools Menu
        self.tools = wx.Menu()
        self.Append(self.tools, "&Tools")

        # Info Menu
        self.info = wx.Menu()
        self.Append(self.info, "&Info")

# Class - Footer
class Footer(wx.Panel):
    def __init__(self, mainWindow, *args, **kwargs):
        super(Footer, self).__init__(mainWindow, *args, **kwargs)

    def setup(self, mainWindow):
        self.mainWindow = mainWindow

        # Show Text
        self.text = wx.StaticText(self, pos=(20, 0))
        self.text.SetLabel("This is Footer")

# Launch Application
if __name__ == "__main__":
    app = wx.App()
    frame = MainWindow(None, title="Ray-Grav")
    frame.Maximize(True)
    frame.Show()
    app.MainLoop()