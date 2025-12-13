# Create a program that will take in a string as input and, if there are duplicates of more than two alphabetical characters in the string, returns the string with all the extra characters in a bracket.

# For example, the input "aaaabbcdefffffffg" should return "aa[aa]bbcdeff[fffff]g"

# Please also ensure that the input is a string, and return "Please enter a valid string" if it is not.

#MY CODE
def string_parse(strng):
    if type(strng) != str: return "Please enter a valid string"

    if strng == "": return ""

    result = ""
    count = 1
    last_letter = strng[0]

    for i in range(1, len(strng)+1):


        if i < len(strng) and strng[i] == last_letter:
            count += 1
        else:

            if count <= 2:
                result += last_letter * count
            else:
                result += last_letter * 2 + "[" + last_letter * (count - 2) + "]"

            if i < len(strng):
                last_letter = strng[i]
                count = 1

    return result


#BEST CODE by colbydauph
import re
def string_parse(string):
    return re.sub(r'(.)\1(\1+)', r'\1\1[\2]', string) if isinstance(string, str) else 'Please enter a valid string'