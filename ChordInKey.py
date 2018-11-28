import sys, time
from collections import deque

#region Global Variables

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

#endregion

# Returns the notes of the mode starting at the root note
def notesInScale(mode, shiftKeys):
    scale = []
    for step in mode:
        scale.append(shiftKeys[step])
    return scale

# Prompts the user to enter in a possible value in a list
# returns the value if its in the list, else quits the program
def userInput(str, lst):
    ui = input("Enter a " + str +": ")
    if ui in lst:
        val = ui
    else:
        print(ui + " is not a " + str)
        sys.exit()
    return val

# var shiftedNotes - all the notes shifted by the current key
# var scale - the notes in the current key
# var dim - chord location of the diminished chord in the working mode
def findSecondaryDominates(shiftedNotes, scale, dim):
    for count in range(1,7):        # Starts after the root
        if count == dim: continue   # Does not run on the diminished chord
        chordTone = shiftedNotes.index(scale[count])
        chord = (shiftedNotes[(chordTone+fifth)%len(shiftedNotes)], shiftedNotes[(chordTone+fifth+4)%len(shiftedNotes)], shiftedNotes[(chordTone+fifth+7)%len(shiftedNotes)], shiftedNotes[(chordTone+fifth+10)%len(shiftedNotes)])
        print("The Secondary Dominate of the " + str(count + 1) + " chord is: " + str(chord))

def main():
    key = userInput("Key", notes)
    mode = userInput("Mode", modes) ##### Commenting out to run on alpha version
    
    print("Here are the chords in " + key, mode)

    shiftKeys = deque(notes)        # Allows you to change the root notes of the key
    shiftVal = notes.index(key)     # Gets the amount that the notes have to be shifted by
    shiftKeys.rotate(-shiftVal)     # Shifts the notes to get correct root note

    scale = notesInScale(modes.get(mode), shiftKeys) 

    for count in range(len(scale)):
        chord = (scale[(count+0)%len(scale)], scale[(count+2)%len(scale)], scale[(count+4)%len(scale)])
        print("The " + str(count + 1) + " chord is: " + str(chord))

    shiftedNotes = list(shiftKeys)

    findSecondaryDominates(shiftedNotes, scale, dims.get(mode))
    
main()
time.sleep(10)