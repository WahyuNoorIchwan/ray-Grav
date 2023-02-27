import wx, vtk
from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor

class Tab(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup Layout
        self.layout = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.layout)

        # Attributes
        self.objects = {}

    def setup(self, mainWindow):
        self.mainWindow = mainWindow

        # Create Layout
        sidebar = Sidebar(self, style=wx.SUNKEN_BORDER)
        sidebar.setup(self)

        self.create_vtk_window()

    # Method Tab - Create VTK Window
    def create_vtk_window(self):
        # Window
        self.vtkWidget = vtkWidget(self, 1, style=wx.SUNKEN_BORDER)
        self.layout.Add(self.vtkWidget, 10, wx.EXPAND)

        # Renderer
        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(255, 255, 255)
        self.vtkWidget.GetRenderWindow().AddRenderer(self.renderer)

        # Interactor Style - set to 2D
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
        self.iren.SetInteractorStyle(vtk.vtkInteractorStyleImage())

        self.renderer.ResetCamera()

# Class - VTK Widget
class vtkWidget(wxVTKRenderWindowInteractor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Class - Sidebar
class Sidebar(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.layout = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.layout)

    def setup(self, main):
        self.main = main
        self.mainWindow = self.main.mainWindow

        # Setup Sidebar
        main_size = self.mainWindow.screenSize
        self.size = (int(main_size[0] * 0.2), main_size[1])

        self.SetMaxSize(self.size)
        self.main.layout.Add(self, 1, wx.EXPAND)

        # Create Layout
        self.create_header()
        self.create_object_tree()

    # Method Sidebar - Create Header
    def create_header(self):
        # Container
        header = wx.Panel(self, style=wx.RAISED_BORDER)
        header.SetMinSize((self.size[0], 25))
        header.SetBackgroundColour((240, 241, 242))
        self.layout.Add(header)

        header_ly = wx.BoxSizer()
        header.SetSizer(header_ly)

        # Text
        text = wx.StaticText(header)
        text.SetLabel("    Grid List")
        header_ly.Add(text, 1, wx.CENTER)

    # Method Sidebar - Create Object Tree
    def create_object_tree(self):
        self.main.tree = object_tree(self)
        self.main.tree.setup(self.main)
        self.layout.Add(self.main.tree, 1, wx.EXPAND)

        self.root = self.main.tree.AddRoot('Root ', -1, -1)

        child_1 = self.main.tree.AppendItem(self.root, 'Child')
        child_2 = self.main.tree.AppendItem(self.root, 'Child')

        self.main.tree.Expand(self.root)

# Class - Object Tree
class object_tree(wx.TreeCtrl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add Mouse Event
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.clicked_label)

    # Method Object Tree - Setup
    def setup(self, main):
        self.main = main
        self.mainWindow = self.main.mainWindow

    # Method Object Tree - Clicked Label
    def clicked_label(self, event):
        print("Item CLicked")