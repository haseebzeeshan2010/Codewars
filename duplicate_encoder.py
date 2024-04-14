# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# Notes
# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

#Best solution
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

#Efficiency is O(n^3) due to count in time complexity and O(n) in space complexity

#My solution
def duplicate_encode(word):
    word = word.lower()
    new_word = ""
    for i in word:
        if word.count(i) > 1:
            new_word += ")"
        else:
            new_word +="("
        
    return(new_word)

#Efficiency is O(n^3) due to count in time complexity and O(n) in space complexity

#Revamped solution for efficiency
def duplicate_encode(word):
    word = word.lower()
    char_count = {}
    
    for i in word:
        char_count[i] = char_count.get(i, 0) + 1 # adds to value in dictionary each time character is found
    
    return "".join(["(" if char_count[j] == 1 else ")" for j in word])

#Note: This is both O(n) efficiency in space and time complexity


# #BELOW IS FOR TESTING ONLY
# import random
# import string

# def generate_random_string(length):
#     """Generate a random string of given length."""
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for _ in range(length))

# # Generate 1000 random strings of length 10
# random_strings = [duplicate_encode(generate_random_string(10)) for _ in range(1000)]