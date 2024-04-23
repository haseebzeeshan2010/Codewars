# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.

# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

#My solution
def scramble(s1, s2):
    s1 = list(s1)
    for i in s2:
        if i not in s1:
            return False
        s1.remove(i)
    return True

#Best solution

from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0


#Edited solution

from collections import Counter

def scramble(s1,s2):
    return Counter(s2)-Counter(s1) == {}