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