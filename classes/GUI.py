import wx


class MusicApp(wx.Frame):

    def __init__(self, *args, **kw):
        super(MusicApp, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)
        closeButton = wx.Button(pnl, label='Close', pos=(20, 20))

        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((350, 250))
        self.SetTitle('wx.Button')
        self.Centre()

    def OnClose(self, e):

        self.Close(True)

class GUIClass():
    def GUImain(self):
        app = wx.App()
        ex = MusicApp(None)
        ex.Show()
        app.MainLoop()
