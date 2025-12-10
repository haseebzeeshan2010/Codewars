
#MY CODE
def sq_in_rect(lng, wdth):
    
    if lng == wdth: return None #Zero square check

    sqr_list = []
    #Euclidean algorithm application
    while lng > 0 and wdth > 0:
        if lng > wdth:
            lng = lng - wdth
            sqr_list.append(wdth)
        else:
            wdth = wdth - lng
            sqr_list.append(lng)
    return sqr_list

#BEST VERSION OF EUCLIDEAN ALGORITHM
def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None

    sqr_list = []
    while lng and wdth:
        if lng < wdth:
            lng, wdth = wdth, lng
        count, lng = divmod(lng, wdth) #divmod gets the quotient and remainder
        sqr_list.extend([wdth] * count) #extend is the same as append but for multiple values
    return sqr_list