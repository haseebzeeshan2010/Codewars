# # <-----------Task------------->
# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.


#My solution
def sum_two_smallest_numbers(numbers):
    validate = [i for i in numbers if type(i) == int and i > 0] # code for validation
    sort_asc = sorted(validate) # sorts in ascending order
    return(sort_asc[0]+sort_asc[1]) # returns final sum

#Best solution
import heapq
def sum_two_smallest_numbers(numbers):
    validate = [i for i in numbers if type(i) == int and i > 0] # code for validation
    return sum(heapq.nsmallest(2, validate))#Heap does same as .sort(), but more efficient