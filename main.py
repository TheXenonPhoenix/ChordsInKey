import sys, time
from collections import deque
from classes.GUI import GUIClass
from chordsClasses.ChordInKey import Chords

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

def runGUI():
    gui = GUIClass()
    gui.GUImain()

def main():
    chordObj = Chords()
    key = chordObj.userInput("Key", notes)
    mode = chordObj.userInput("Mode", modes) ##### Commenting out to run on alpha version
    
    print("Here are the chords in " + key, mode)

    shiftKeys = deque(notes)        # Allows you to change the root notes of the key
    shiftVal = notes.index(key)     # Gets the amount that the notes have to be shifted by
    shiftKeys.rotate(-shiftVal)     # Shifts the notes to get correct root note

    scale = chordObj.notesInScale(modes.get(mode), shiftKeys) 

    for count in range(len(scale)):
        chord = (scale[(count+0)%len(scale)], scale[(count+2)%len(scale)], scale[(count+4)%len(scale)])
        print("The " + str(count + 1) + " chord is: " + str(chord))

    shiftedNotes = list(shiftKeys)

    chordObj.findSecondaryDominates(shiftedNotes, scale, dims.get(mode), fifth)
    
#main()
runGUI()
#time.sleep(10)