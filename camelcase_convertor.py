# Write a method (or function, depending on the language) that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.

# Examples (input --> output):
# "hello case" --> "HelloCase"
# "camel case word" --> "CamelCaseWord"


#My Solution - possibly more efficient due to lack of overhead from.replace
def camel_case(s):
    s = s.split() #removes spaces and converts to list
    s = [i[0].upper()+i[1:].lower() for i in s ] #Converts to Camel Case
    return "".join(s) #Joins back the array

#More efficient version of my solution
def camel_case(s):
    s = s.split() #removes spaces and converts to list
    s = [i.title() for i in s ] #Converts to Camel Case
    return "".join(s) #Joins back the array

#Best Solution for concise code
def camel_case(s):
    return s.title().replace(" ", "") #Converts to Camel Case and removes space
