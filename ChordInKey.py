import sys
from collections import deque

keys = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
modes = ['Major','Dorian','Phrygian','Lydian','Mixolydian','Minor','Locrian']

def userInput(str, lst):
    ui = input("Enter a " + str +": ")
    if ui in lst:
        val = ui
    else:
        print(ui + " is not a " + str)
        sys.exit()
    return val

key = userInput("Key", keys)
mode = userInput("Mode", modes)

print("Here are the chords in " + key, mode)

shiftKeys = deque(keys)         # Allows you to change the root notes of the key

shiftVal = keys.index(key)      # Gets the amount that the notes have to be shifted by
shiftKeys.rotate(-shiftVal)     # Shifts the notes to get correct root note

#print(shiftKeys)               # Debugging

scale = (shiftKeys[0],shiftKeys[2],shiftKeys[4],shiftKeys[5],shiftKeys[7],shiftKeys[9],shiftKeys[11])

for count in range(len(scale)):
    chord = (scale[(count+0)%len(scale)], scale[(count+2)%len(scale)], scale[(count+4)%len(scale)])
    print("The " + str(count + 1) + " chord is: " + str(chord))