from guizero import App, PushButton, Text, Combo, TextBox, Window
from chordsClasses.ChordInKey import Chords

chordObj = Chords()

class GUIClass():
    def GUImain(self):
        #initializes the application's features such as the combo boxes, instructions, and a submit button
        app = App(title="Chords in Key")
        instructionText = Text(app, text = "Instructions: Select a chord and a key from the drop down menus\n\n", size = 10)  
        noteOptions = Combo(app, options=chordObj.notes)
        typeChordOptions = Combo(app, options=chordObj.typeChords)
        secDomText = Text(app, text = "Results: \n\n\n\n\n\n\n\n", size = 10)
        submitButton = PushButton(app, text = "Submit", command = self.handleSubmit(noteOptions, typeChordOptions, secDomText))
        app.display()   

    def handleSubmit(self, notes, typeChords, text):
        noteChoice = notes.value
        typeChoice = typeChords.value
        text.append("Note Choice: ", noteChoice, " TypeChoice: ", typeChoice)
        print("Note Choice: ", noteChoice, " TypeChoice: ", typeChoice)
