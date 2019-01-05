import sys, time
from collections import deque
from chordsClasses.ChordInKey import Chords
from guizero import App, PushButton, Text, Combo, TextBox, Window

notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
# Not Necessary, but helpful for readablilty
#Major       = {'Major':(0,2,4,5,7,9,11)}
#Dorian      = {'Dorian':(0,2,3,5,7,9,10)}
#Phrygian    = {'Phrygian':(0,1,3,5,7,8,10)}
#Lydian      = {'Lydian':(0,2,4,6,7,9,11)}
#Mixolydian  = {'Mixolydian':(0,2,4,5,7,9,10)}
#Minor       = {'Minor':(0,2,3,5,7,8,10)}
#Locrian     = {'Locrian':(0,1,3,5,6,8,10)}

# Creates a dictionary containging how to build each key
modes = {'Major':(0,2,4,5,7,9,11),'Dorian':(0,2,3,5,7,9,10),'Phrygian':(0,1,3,5,7,8,10),'Lydian':(0,2,4,6,7,9,11),'Mixolydian':(0,2,4,5,7,9,10),'Minor':(0,2,3,5,7,8,10),'Locrian':(0,1,3,5,6,8,10)} 
dims = {'Major':6,'Dorian':5,'Phrygian':4,'Lydian':3,'Mixolydian':2,'Minor':1,'Locrian':0} 

fifth = 7

chordObj = Chords()
    
def handleSubmit():
    secDomText.clear()
    noteChoice = noteOptions.value
    typeChoice = typeChordOptions.value
    
    shiftedNotes, scale, dimsVal = getValuesForSecDom(noteChoice, typeChoice)
    
    secDomText.append(findChords(scale))  
    secDomText.append(chordObj.findSecondaryDominates(shiftedNotes, scale, dimsVal, fifth))      
    #text.append("Note Choice: ", noteChoice, " TypeChoice: ", typeChoice)
    print("Note Choice: ", noteChoice, " TypeChoice: ", typeChoice)
    
def getValuesForSecDom(key, mode):
    shiftKeys = deque(notes)        # Allows you to change the root notes of the key
    shiftVal = notes.index(key)     # Gets the amount that the notes have to be shifted by
    shiftKeys.rotate(-shiftVal)     # Shifts the notes to get correct root note

    scale = chordObj.notesInScale(modes.get(mode), shiftKeys) 
    
    shiftedNotes = list(shiftKeys)
    
    return shiftedNotes, scale, dims.get(mode)

def findChords(scale):
    retString = ""
    for count in range(len(scale)):
        chord = (scale[(count+0)%len(scale)], scale[(count+2)%len(scale)], scale[(count+4)%len(scale)])
        retString += ("\nThe " + str(count + 1) + " chord is: " + str(chord))
    return retString

#uses console as UI for application
def main():
    key = chordObj.userInput("Key", notes)
    mode = chordObj.userInput("Mode", modes) ##### Commenting out to run on alpha version
    
    print("Here are the chords in " + key, mode)

    shiftedNotes, scale, dimsVal = getValuesForSecDom(key, mode)
    print(findChords(scale))

    print(chordObj.findSecondaryDominates(shiftedNotes, scale, dimsVal, fifth))
    

##to run the console UI    
#main()
#time.sleep(10)
    
##to run the GUI UI
#initializes the application's features such as the combo boxes, instructions, and a submit button
app = App(title="Chords in Key")
instructionText = Text(app, text = "Instructions: Select a chord and a key from the drop down menus\n\n", size = 10)  
noteOptions = Combo(app, options=chordObj.notes)
typeChordOptions = Combo(app, options=chordObj.typeChords)
submitButton = PushButton(app, command = handleSubmit, text="Submit")
secDomText = Text(app, text = "Results: \n", size = 10)

app.display()