# Given two numbers: 'left' and 'right' (1 <= 'left' <= 'right' <= 200000000000000) return sum of all '1' occurencies in binary representations of numbers between 'left' and 'right' (including both)

# Example:
# countOnes 4 7 should return 8, because:
# 4(dec) = 100(bin), which adds 1 to the result.
# 5(dec) = 101(bin), which adds 2 to the result.
# 6(dec) = 110(bin), which adds 2 to the result.
# 7(dec) = 111(bin), which adds 3 to the result.
# So finally result equals 8.
# WARNING: Segment may contain billion elements, to pass this kata, your solution cannot iterate through all numbers in the segment!

def count_ones(left, right):
    ones = 0
    for i in range(left,right+1):
        ones += bin(i).count("1")
    return ones

#BEST SOLUTION

def count(n):
    if n is 0: return 0  # if n is 0, return 0
    x = int(math.log(n, 2))  # calculate the highest power of 2 less than or equal to n
    return x * 2 ** (x - 1)  # return the number of 1s in the most significant part of the binary representation of n
         + n - 2 ** x  # subtract the least significant part of the binary representation of n
         + 1  # add 1 for the most significant part of the binary representation of n
         + count(n - 2 ** x)  # recursively calculate the number of 1s in the least significant part of the binary representation of n