#!/urs/bin/python
import wx
from ..core.gk_node import GKNode, GK_SHAPE_TYPE


class GKUINodeEditDialog(wx.Dialog):
    def __init__(self, parent, node):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Edit Node", pos=wx.DefaultPosition, size=wx.DefaultSize,
                           style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.m_node = node
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.AddGrowableCol(1)
        fgSizer1.AddGrowableRow(1)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Label:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        fgSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_label_ctrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_label_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        fgSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_desc_ctrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250, 100),
                                       wx.TE_MULTILINE)
        fgSizer1.Add(self.m_desc_ctrl, 1, wx.ALL | wx.EXPAND, 5)

        bSizer4.Add(fgSizer1, 1, wx.EXPAND, 5)

        self.m_style_ctrl = wx.RadioBox(self, wx.ID_ANY, u"Style", wx.DefaultPosition, wx.DefaultSize, GK_SHAPE_TYPE, 1,
                                        wx.RA_SPECIFY_COLS)
        self.m_style_ctrl.SetSelection(0)
        bSizer4.Add(self.m_style_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Image: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer5.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_img_ctrl = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                            wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        bSizer5.Add(self.m_img_ctrl, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer4.Add(bSizer5, 0, wx.EXPAND, 5)

        m_buttons_ctrl = wx.StdDialogButtonSizer()
        self.m_buttons_ctrlSave = wx.Button(self, wx.ID_SAVE)
        m_buttons_ctrl.AddButton(self.m_buttons_ctrlSave)
        self.m_buttons_ctrlCancel = wx.Button(self, wx.ID_CANCEL)
        m_buttons_ctrl.AddButton(self.m_buttons_ctrlCancel)
        m_buttons_ctrl.Realize()

        bSizer4.Add(m_buttons_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()
        bSizer4.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_img_ctrl.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUIImage)
        self.m_buttons_ctrlSave.Bind(wx.EVT_BUTTON, self.OnSave)

    def __del__(self):
        pass

    def OnUpdateUIImage(self, event):
        """Update the UI for the image browse control"""
        index = GK_SHAPE_TYPE.index("image")
        if self.m_style_ctrl.GetSelection() == GK_SHAPE_TYPE.index("image"):
            event.Enable(True)
        else:
            event.Enable(False)

    def TransferDataToWindow(self):
        if self.m_node.m_name:
            self.m_label_ctrl.SetValue(self.m_node.m_name)
        if self.m_node.m_description:
            self.m_desc_ctrl.SetValue(self.m_node.m_description)
        self.m_style_ctrl.SetSelection(GK_SHAPE_TYPE.index(self.m_node.m_shapetype))
        if self.m_node.m_external_link:
            self.m_img_ctrl.SetPath(self.m_node.m_external_link)
        return True

    def OnSave(self, event):
        self.m_node.m_name = self.m_label_ctrl.GetValue()
        self.m_node.m_description = self.m_desc_ctrl.GetValue()
        self.m_node.m_shapetype = GK_SHAPE_TYPE[self.m_style_ctrl.GetSelection()]
        self.m_node.m_external_link = self.m_img_ctrl.GetPath()
        self.EndModal(wx.ID_SAVE)
        event.Skip()
