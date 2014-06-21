'''
Created on  May 10, 2014
Modified on May 14, 2014
Version 0.015
@author: rainier.madruga@gmail.com
A simple Python Program to based on Tony Dowler's "How To Host a Dungeon".
	More Information available at: http://www.planet-thirteen.com/Dungeon.aspx
'''
# Sample Dungeon Log available at: http://www.planet-thirteen.com/images/dd/DungeonLog1.txt
import random
import collections
import csv

'''# Function to roll a number of multi-sided dice '''
def diceRoll(num, sides):
    x = num
    y = sides
    counter = 0
    score = 0
    while counter < x:
        score += random.randint(1,y)
        counter +=1
    return score

''' Define Object to store the Dungeon '''
class Dungeon(object):
    def __init__(self, name, prim_state):
        self.name = name
        self.prim_state = prim_state

# Create dictionaries for the Dungeon
d_Primordial = {}  # create a primordial dictionary.
# index: e, diceroll: value, value: prim_desc

# Debug Process here
x = diceRoll(1,8)

'''# Function to randomly generate the character's name '''
def dungeonName():
    names = ['The Frightful Tombs of Aggoria', 'The Black Mines of Basalt', 'The Temple of Elemental Mistrust', 'The Underhill Dungeon', 'Bald Mountain']
    dunName = random.choice(names)
    return dunName

# Define the Dungeon's Base State
prim_scores = [diceRoll(1,8), diceRoll(1,8), diceRoll(1,8)]
new_dungeon = Dungeon(dungeonName(), prim_scores)

def Primordial(x):
    dieRoll = x
    prim_desc = ''
    if x == 1:
        prim_desc = "A deposit of Mithral" 
    elif x >1 and x<4:
        prim_desc = "A series of Natural Caverns"
    elif x == 4:
        prim_desc = "A vein of Gold"
    elif x == 5:
        prim_desc = "A Cave Complex"
    elif x == 6:
        prim_desc = "An Underground River" 
    elif x == 7:
        prim_desc = "An Ancient Wyrm"
    else:
        prim_desc = "Make Up Your Own or Chose from Table"
    return prim_desc



# Output Dungeon Description

with open('dungeon_archive.txt', 'a+') as f:
    f.write(new_dungeon.name + ' is a deep and ancient dungeon. It is filled with:' + '\n')
    for i in new_dungeon.prim_state:
        f.write("     %d " % i + Primordial(i) + '\n')
    f.write('')
    f.close()

# Duplicate Output to Terminal
print new_dungeon.name + ' is a deep and ancient dungeon. It is filled with:'
for i in new_dungeon.prim_state:
    print "     %d " % i + Primordial(i)
