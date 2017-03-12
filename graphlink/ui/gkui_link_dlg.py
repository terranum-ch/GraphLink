import wx
from ..core.gk_link import GKLink

###########################################################################
# Class GKUIEditLink
###########################################################################


class GKUILinkDialog (wx.Dialog):
    def __init__(self, parent, nodemanager, link):
        wx.Dialog.__init__(
            self, parent, id=wx.ID_ANY, title=u"Edit Link",
            pos=wx.DefaultPosition, size=wx.Size(350, -1),
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.m_link = link
        self.m_node_manager = nodemanager
        my_node_labels = []
        for node in self.m_node_manager.m_nodes:
            my_node_labels.append(node.m_name)

        m_from_node_ctrlChoices = my_node_labels
        m_to_node_ctrlChoices = my_node_labels

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.AddGrowableCol(1)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"From Node:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        fgSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        # m_from_node_ctrlChoices = []
        self.m_from_node_ctrl = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,-1),
            m_from_node_ctrlChoices, 0)
        self.m_from_node_ctrl.SetSelection(0)
        fgSizer1.Add(self.m_from_node_ctrl, 0, wx.ALL|wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"To Node:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        fgSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_to_node_ctrl = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_to_node_ctrlChoices, 0)
        self.m_to_node_ctrl.SetSelection(0)
        fgSizer1.Add(self.m_to_node_ctrl, 0, wx.ALL|wx.EXPAND, 5)

        bSizer1.Add(fgSizer1, 0, wx.EXPAND, 5)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Link Options"), wx.VERTICAL)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText3 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Label:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        fgSizer2.Add(self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_label_link_ctrl = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.m_label_link_ctrl, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText4 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Color:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        fgSizer2.Add(self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_color_link_ctrl = wx.ColourPickerCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE)
        fgSizer2.Add(self.m_color_link_ctrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer1.Add(fgSizer2, 0, wx.EXPAND, 5)

        bSizer1.Add(sbSizer1, 1, wx.EXPAND|wx.ALL, 5)

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button(self, wx.ID_OK)
        m_sdbSizer1.AddButton(self.m_sdbSizer1OK)
        self.m_sdbSizer1Cancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer1.AddButton(self.m_sdbSizer1Cancel)
        m_sdbSizer1.Realize();

        bSizer1.Add(m_sdbSizer1, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_sdbSizer1OK.Bind(wx.EVT_BUTTON, self.OnOk)

    def TransferDataToWindow(self):
        # TODO: Implement the logic here for link loading
        return True

    def OnOk(self, event):
        # get selected node 1 and 2
        my_node1 = self.m_node_manager.m_nodes[self.m_from_node_ctrl.GetSelection()]
        my_node2 = self.m_node_manager.m_nodes[self.m_to_node_ctrl.GetSelection()]

        self.m_link.m_node1 = my_node1
        self.m_link.m_node2 = my_node2
        self.m_link.m_label = self.m_label_link_ctrl.GetValue()
        self.m_link.m_color = self.m_color_link_ctrl.GetColour().GetAsString(wx.C2S_HTML_SYNTAX)
        event.Skip()
