import wx
from chordsClasses.ChordInKey import Chords

chordObj = Chords()

class MusicApp(wx.Frame):

    def __init__(self, *args, **kw):
        super(MusicApp, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)

        #font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.BOLD)

        title = wx.StaticText(pnl, label='Notes in Key',pos = (50,10), style=wx.ALIGN_LEFT)
        
        #title.SetFont(font)

        submitButton = wx.Button(pnl, label='Submit', pos=(50, 100))

        noteCombo = wx.ComboBox(pnl, pos=(25, 50), choices=chordObj.notes, style=wx.CB_READONLY)
        keyCombo = wx.ComboBox(pnl, pos=(100, 50), choices=chordObj.typeChords, style=wx.CB_READONLY)

        submitButton.Bind(wx.EVT_BUTTON, self.OnSubmit(noteCombo))


        self.SetSize((750, 300))
        self.SetTitle('Sing Along with Kevin')
        self.Centre()

    def OnSubmit(self, e):
        noteSelection = self.noteCombo.GetValue()
        keySelection = self.keyCombo.GetValue()
        print(noteSelection)
        print(keySelection)
        #secondWindow = DisplayWindow()


    
# class DisplayWindow():
#     def __init__(self, *args, **kw):
#         super(DisplayWindow, self).__init__(*args, **kw)
#         self.InitUI()

#     def InitUI(self):
#         disPnl = wx.Panel(self)
#         self.Show()


class GUIClass():
    def GUImain(self):
        app = wx.App()
        ex = MusicApp(None)
        ex.Show()
        app.MainLoop()
