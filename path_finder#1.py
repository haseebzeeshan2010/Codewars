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



#Version 2 Solution

def flood_fill(maze, column, row):
    print("//////")
    print(column,row,maze[column],"         ", maze[column][row])
    
    print(maze[column][row])
    if maze[column][row] == ".":
        print("NOWALL")
        
        if len(maze)-1 >= column+1:
            flood_fill(maze,column+1,row)
            
    if maze[column][row] == "W":
        print("WALL")
        return False
    
#     return True
    

def path_finder(maze):
    maze = maze.split("\n")
    print(maze)
    
    print(flood_fill(maze,0,0))
    return True # can go to lower right corner from upper left one




#BEST SOLUTION

def path_finder(maze):
    matrix = list(map(list, maze.splitlines()))
    stack, length = [[0, 0]], len(matrix)
    while len(stack):
      x, y = stack.pop()
      if matrix[x][y] == '.':
        matrix[x][y] = 'x'
        for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
          if 0 <= x < length and 0 <= y < length:
            stack.append((x, y))
    return matrix[length-1][length-1] == 'x'