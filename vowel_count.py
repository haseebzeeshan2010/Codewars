# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.


#MY CODE
def get_count(sentence):
    char_count = 0
    
    for char in sentence:
        if char in ["a","e","i","o","u"]:
            char_count += 1
            
    return char_count

#BEST CODE
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")