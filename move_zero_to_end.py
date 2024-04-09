# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

#e.g.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


#my solution
def move_zeros(lst):
    num_zeroes = [zeroes for zeroes in lst if zeroes == 0] #adds all zeroes to an array
    
    lst = [value for value in lst if value != 0] + num_zeroes #first removes zeroes then concatenates the num_zeroes array with lst
    return lst

#best solution
def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array