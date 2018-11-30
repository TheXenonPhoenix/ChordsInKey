import wx
from chordsClasses.ChordInKey import Chords

chordObj = Chords()

class MusicApp(wx.Frame):

    def __init__(self, *args, **kw):
        super(MusicApp, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)
        submitButton = wx.Button(pnl, label='Close', pos=(150, 150))
        noteCombo = wx.ComboBox(pnl, pos=(75, 10), choices=chordObj.notes, 
            style=wx.CB_READONLY)
        cb = wx.ComboBox(pnl, pos=(200, 10), choices=chordObj.typeChords, 
            style=wx.CB_READONLY)

        submitButton.Bind(wx.EVT_BUTTON, self.OnSubmit)

        self.SetSize((350, 250))
        self.SetTitle('Chords')
        self.Centre()

    def OnSubmit(self, e):

        self.Close(True)

class GUIClass():
    def GUImain(self):
        app = wx.App()
        ex = MusicApp(None)
        ex.Show()
        app.MainLoop()
