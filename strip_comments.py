def strip(strng, markers):
#     print(strng, len(strng))
    for j in range(0,len(strng)):
            if len(strng) == 1:
                    print("oaaaaaa")
            if strng[j] in markers:
                
                print(strng,strng[-1])
                strng = strng[:j]
                
                
                if strng[-1] == " ":
                    return strng[:-1]
                
                return strng

def strip_comments(strng, markers): # NOTE: Remember to add \n at end of each one!
#     print(strng, markers)
    strng = strng.split("\n")
    for i in range(0,len(strng)):
        stripped = strip(strng[i],markers)
        if stripped != None:
            strng[i] = stripped
    return("\n".join(strng))
        
#         if strng[i] in markers:
#             temp = strng[i:]
#             begin_index = i
        
#         if strng[i] == "\n":
# #             indexes.append(i)
#             remove_strng.append(temp[:i-begin_index])
#             temp = ""

        
         

#     print(remove_strng)
            
            
            
            
            
# !apples, pears /nbannanas