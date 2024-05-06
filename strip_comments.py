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
    print(strng, markers)
    new_strng = []

    for i in strng:
        new_strng.append(strip(i,markers))
            
    
    
    for string in range(0,len(new_strng)):
        if len(new_strng[string]) != 0:
            if new_strng[string][-1] == " ":
                new_strng[string] = "".join(list(new_strng[string])[:-1])

    return "\n".join(new_strng)