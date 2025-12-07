# Sentence Calculator
# Calculate the total score (sum of the individual character scores) of a sentence given the following score rules for each allowed group of characters:

# Lower case [a-z]: 'a'=1, 'b'=2, 'c'=3, ..., 'z'=26
# Upper case [A-Z]: 'A'=2, 'B'=4, 'C'=6, ..., 'Z'=52
# Digits [0-9] their numeric value: '0'=0, '1'=1, '2'=2, ..., '9'=9
# Other characters: 0 value
# Note: input will always be a string

#MY CODE/BEST CODE

def letters_to_numbers(s):

    total_score = 0
    
    s = s.replace(" ", "") # preprocess by removing spaces    
    for char in s:
        
        #Check for lowercase
        if char.islower():
            total_score += ord(char.lower()) - 96
        
        #Check for uppercase
        elif char.isupper():
            total_score += (ord(char.lower()) - 96)*2

        #Check for numbers
        elif char.isdigit():
            total_score += int(char)

    return total_score