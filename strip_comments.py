# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas
# The code would be called like so:

# result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"


#MY CODE

def strip(string, markers):
    found = False
    for j in range(0,len(string)):
            if string[j] in markers:
                return string[:j]
                found = True
                
    if found == False:
        return string


def strip_comments(strng, markers):
    strng = strng.split("\n")

    new_strng = []

    for i in strng:
        new_strng.append(strip(i,markers))
            
    
    
    for string in range(0,len(new_strng)):
        if len(new_strng[string]) != 0:
            if new_strng[string][-1] == " ":
                new_strng[string] = "".join(list(new_strng[string])[:-1])

    
    new_string = "\n".join(new_strng)
    
    print(list(new_string))
    if len(new_string) != 0:
        if new_string[0] == "\t" and new_string[1] == "\n" or new_string[0] == " " and new_string[1] == "\n":
            print("Aye")
            return new_string[1:]
    return new_string


#BEST CODE by milesb

def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)