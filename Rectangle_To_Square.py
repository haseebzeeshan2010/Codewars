# You will be given two dimensions

# a positive integer length
# a positive integer width
# You will return a collection or a string (depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the squares.

# Examples in general form:
# (depending on the language)

#   sqInRect(5, 3) should return [3, 2, 1, 1]
#   sqInRect(3, 5) should return [3, 2, 1, 1]

#   You can see examples for your language in **"SAMPLE TESTS".**
# Notes:
# lng == wdth as a starting case would be an entirely different problem and the drawing is planned to be interpreted with lng != wdth. (See kata, Square into Squares. Protect trees! http://www.codewars.com/kata/54eb33e5bc1a25440d000891 for this problem).

# When the initial parameters are so that lng == wdth, the solution [lng] would be the most obvious but not in the spirit of this kata so, in that case, return None/nil/null/Nothing or return {} with C++, [] with Perl, Raku.

# In that case the returned structure of C will have its sz component equal to 0.

# Return the string "nil" with Bash, PowerShell, Pascal and Fortran.


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