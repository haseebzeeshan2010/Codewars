# Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

# For example:

# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# # should return False 
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# # should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# # should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )


def same_structure_as(original,other):  
    if type(original) == type(other) :
        if len(original) == len(other):
            for i in range(0,len(original)):
                if type(original[i]) == list and type(other[i]) == list:

                    return same_structure_as(original[i],other[i])

                elif (type(original[i]) == list and type(other[i]) != list) or (type(original[i]) != list and type(other[i]) == list):
                    return False

                else:
                    original[i] == ""

            return True
        else:
            return False
        pass
    return False