# Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

# The keypad has the following layout:

# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
# He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

# He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

# * possible in sense of: the observed PIN itself and all variations considering the adjacent digits

# Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

# Detective, we are counting on you!


#My solution
import itertools

def get_pins(observed):
    
    keypad = [None,None,None,None,"1","4","7",None,"2","5","8",None,"3","6","9",None,None,None,None]    
    possibilities = []
    for i in observed:
        temp = []
        if int(i) == 0:
            temp.append("8")
        else:
            if int(i) == 8:
                temp.append("0")
            number = keypad.index(i)
            if keypad[number+1] != None:
                temp.append(keypad[number+1])
            if keypad[number+4] != None:
                temp.append(keypad[number+4])
            if keypad[number-1] != None:
                temp.append(keypad[number-1])
            if keypad[number-4] != None:
                temp.append(keypad[number-4])

        temp.append(i)
        possibilities.append(temp)
        
        
    combinations = itertools.product(*possibilities)
    combinations = list(combinations)
    
    result = ["".join(element) for element in combinations]

    return(result)
    
#Best solution - by jolaf
from itertools import product


ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]