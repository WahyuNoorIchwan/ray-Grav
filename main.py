import wx, data, visualization, project

# Main Window Class
class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.project = None

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

        # Tabs - to Create Tab
        # container = wx.Notebook(self.mainWidget)
        # self.mainLayout.Add(container, 25)

        # self.dataTab = data.Tab(container)
        # self.dataTab.setup(self)
        # container.AddPage(self.dataTab, "Processing")

        self.visTab = visualization.Tab(self.mainWidget)
        self.visTab.setup(self)
        self.mainLayout.Add(self.visTab, 30, wx.EXPAND)

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
        func = lambda event: project.Open(self.mainWindow)
        self.mainWindow.Bind(wx.EVT_MENU, func, self.open)

        self.file.AppendSeparator()

        # File Menu - Save Project
        self.save = self.file.Append(-1, "Save Project")

        func = lambda event: None
        self.mainWindow.Bind(wx.EVT_MENU, func, self.save)

        # File Menu - Close Project
        self.close_p = self.file.Append(-1, "Close Project")
        func = lambda event: project.Close(self.mainWindow)
        self.mainWindow.Bind(wx.EVT_MENU, func, self.close_p)

        self.file.AppendSeparator()

        # File Menu - Close Program
        self.close = self.file.Append(-1, "Close")

        func = lambda event: None
        self.mainWindow.Bind(wx.EVT_MENU, func, self.close)

        # Edit Menu
        self.edit = wx.Menu()
        self.Append(self.edit, "&Edit")

        # Grid Menu
        self.grid = wx.Menu()
        self.Append(self.grid, "&Grid")

        # Grid Menu - Create Grid
        txt = "Create Grid"
        self.createGrid = self.grid.Append(-1, txt)

        # Grid Menu - Import Grid
        txt = "Import Grid"
        self.importGrid = self.grid.Append(-1, txt)

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