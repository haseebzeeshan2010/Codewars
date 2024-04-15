#TASK
# A format for expressing an ordered list of integers is to use a comma separated list of either

# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

# Example:

# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
# Courtesy of rosettacode.org


#Best Solution
def solution(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)


#My solution
def solution(args):
    range_list = []
    temp = []
    for i in range(0,len(args)-1):
        
        temp.append(str(args[i]))
        if args[i+1] != args[i] + 1:
            if len(temp) > 2:
                range_list.append(f"{temp[0]}-{temp[-1]}")
            else:
                range_list.append(",".join(temp))
            temp = []
    temp.append(str(args[-1]))
    if len(temp) > 2:
        range_list.append(f"{temp[0]}-{temp[-1]}")
    else:
        range_list.append(",".join(temp))
    return(",".join(range_list))