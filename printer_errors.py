


#MY CODE
def printer_error(s):
    error_num = 0
    for i in s:
        if ord(i) > 109:
            error_num += 1
    
    return f"{error_num}/{len(s)}"

#BEST CODE by gatekeeper
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))