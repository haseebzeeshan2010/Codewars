def check_braces(string):
    value = False
    new_string = string
    while value != True:
        
        if new_string[0] == "[" and new_string[-1] == "]":
            new_string = new_string[1:][:-1]
        elif new_string[0] == "(" and new_string[-1] == ")":
            new_string = new_string[1:][:-1]
        elif new_string[0] == "{" and new_string[-1] == "}":
            new_string = new_string[1:][:-1]
        else:
            new_string = "invalid"
        
        if len(new_string) == 0:
            value = True
        elif new_string == "invalid":
            return False
        else:
            value = False
#         print(len(new_string))
    return True