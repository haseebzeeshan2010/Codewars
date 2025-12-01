# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

# Example:

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
# Link to Jaden's former Twitter account @officialjaden via archive.org


#MY SOLUTION

def to_jaden_case(string):
    word_list = string.split(" ")
    
    if word_list: #Null Check
        for i in range(0,len(word_list)): # Separate words
            #Format in correct manner
            word_list[i] = word_list[i][0].upper() + word_list[i][1:].lower()

        jaden_case = " ".join(word_list) # Join back into single string
    return jaden_case

#BEST SOLUTION

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())