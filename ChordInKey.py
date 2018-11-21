import sys
from collections import deque

notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']


Major       = (0,2,4,5,7,9,11)
Dorian      = (0,2,3,5,7,9,10)
Phrygian    = (0,1,3,5,7,8,10)
Lydian      = (0,2,4,6,7,9,11)
Mixolydian  = (0,2,4,5,7,9,10)
Minor       = (0,2,3,5,7,8,10)
Locrian     = (0,1,3,5,6,8,10)

modes = ['Major','Dorian','Phrygian','Lydian','Mixolydian','Minor','Locrian'] # hardcoded to just work with major

modestest = {'Major':(0,2,4,5,7,9,11)}

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

key = userInput("Key", notes)
mode = userInput("Mode", modes)
print("Here are the chords in " + key, mode)


shiftKeys = deque(notes)         # Allows you to change the root notes of the key
shiftVal = notes.index(key)      # Gets the amount that the notes have to be shifted by
shiftKeys.rotate(-shiftVal)     # Shifts the notes to get correct root note


print(mode)

scale = notesInScale(Minor, shiftKeys) 

for count in range(len(scale)):
    chord = (scale[(count+0)%len(scale)], scale[(count+2)%len(scale)], scale[(count+4)%len(scale)])
    print("The " + str(count + 1) + " chord is: " + str(chord))