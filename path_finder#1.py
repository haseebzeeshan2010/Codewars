# Task
# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

# Empty positions are marked ..
# Walls are marked W.
# Start and exit positions are empty in all test cases.



def row_length(maze):
    count = 0
    for i in range(0,len(maze)):
        if maze[i] == "\n":
            return i+1

def path_finder(maze):
    
    r_length = row_length(maze)
    
    for i in range(0,len(maze)): # debugging section
        print(maze[i], i)
        

    if r_length*2 <= len(maze): # checks next row
        if maze[r_length*2] != "W":
            return path_finder(maze[r_length:])
        else:
            return True
    else:
        return False
    
    
#     for i in range(0,r_length):
#         if r_length*i <= len(maze):
#             print(r_length*i)
#             if maze[r_length*i] == "W":
#                 print("yay", r_length*i)
#             else:
#                 print("noo", r_length*i)
    print(maze[r_length*2] , " ", r_length*2)
    return True # can go to lower right corner from upper left one