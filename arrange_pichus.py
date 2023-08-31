#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [Sushant Nirantar sniranta]
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
def successors(house_map):
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' ]

def row_col_block(house_map,row,col):
    l= set()
    for i in range(len(house_map[0])):
        l.add((row,i))
    for i in range(len(house_map)):
        l.add((i,col))
    return l


def row_right(house_map,row,col):
    l=set()
    i=col
    while(i<len(house_map[0])):
        l.add((row,i))
        i=i+1
    return l
def row_left(house_map,row,col):
    l=set()
    i=col
    while(i>=0):
        l.add((row,i))
        i=i-1
    return l
def col_up(house_map,row,col):
    l=set()
    i=row
    while(i>=0):
        l.add((i,col))
        i=i-1
    return l
def col_down(house_map,row,col):
    l=set()
    i=row
    while(i<len(house_map)):
        l.add((i,col))
        i=i+1
    return l
def right_down_diagonal(house_map,row,col):
    l=set()
    while(row<len(house_map) and col<len(house_map[0])):
        l.add((row,col))
        row=row+1
        col=col+1
    return l
def right_up_diagonal(house_map,row,col):
    l=set()
    while(row>=0 and col<len(house_map[0])):
        l.add((row,col))
        row=row-1
        col=col+1
    return l
def left_up_diagonal(house_map,row,col):
    l=set()
    while(row>=0 and col>=0):
        l.add((row,col))
        row=row-1
        col=col-1
    return l
def left_down_diagonal(house_map,row,col):
    l=set()
    while(row<len(house_map) and col>=0):
        l.add((row,col))
        row=row+1
        col=col-1
    return l
def return_wall_list(house_map):
    wall_list=[]
    for r in range(len(house_map)):
        for c in range(len(house_map[0])):
            if(house_map[r][c]=='X' or house_map[r][c]=='@'):
                wall_list.append((r,c))
    return wall_list
# check if house_map is a goal state
def is_goal(house_map, k):
    #Making a list of all pichus and walls in the given array.
    pichu_list=[]
    wall_list=return_wall_list(house_map)
    for r in range(len(house_map)):
        for c in range(len(house_map[0])):
            if(house_map[r][c]=='p'):
                pichu_list.append((r,c))
    #for r in range(len(house_map)):
    #    for c in range(len(house_map[0])):
    #        if(house_map[r][c]=='X' or house_map[r][c]=='@'):
    #            wall_list.append((r,c))
    
    #creating a block_list_set
    block_list= set()
    #print(pichu_list)

    first_elem=pichu_list.pop(0)
    #Popping first pichu from the list and exploring all 8 directions
    right_side=row_right(house_map,*first_elem)
    left_side=row_left(house_map,*first_elem)
    up_side=col_up(house_map,*first_elem)
    down_side=col_down(house_map,*first_elem)
    right_d_up=right_up_diagonal(house_map,*first_elem)
    right_d_down=right_down_diagonal(house_map,*first_elem)
    left_d_up=left_up_diagonal(house_map,*first_elem)
    left_d_down=left_down_diagonal(house_map,*first_elem)
   
    #block_list=block_list.union(*union_list)
    
    #print(wall_list)
    #new_right_side=set()
    #checking for first presence of wall in block_list in every direction
    for i in range(len(wall_list)):
        curr=wall_list.pop(0)
        #print(len(wall_list))
        if(curr in right_side):
            free_side=row_right(house_map,*curr)
            right_side=right_side-free_side
        if(curr in left_side):
            free_side=row_left(house_map,*curr)
            left_side=left_side-free_side
        if(curr in up_side):
            free_side=col_up(house_map,*curr)
            up_side=up_side-free_side
        if(curr in down_side):
            free_side=col_down(house_map,*curr)
            down_side=down_side-free_side
        if(curr in right_d_up):
            free_side=right_up_diagonal(house_map,*curr)
            right_d_up=right_d_up-free_side
        if(curr in right_d_down):
            free_side=right_down_diagonal(house_map,*curr)
            right_d_down=right_d_down-free_side
        if(curr in left_d_up):
            free_side=left_up_diagonal(house_map,*curr)
            left_d_up=left_d_up-free_side
        if(curr in left_d_down):
            free_side=left_down_diagonal(house_map,*curr)
            left_d_down=left_d_down-free_side
    #creating an initial block_list_set from the first present pichu
    block_list=block_list.union(right_side)
    block_list=block_list.union(left_side)
    block_list=block_list.union(up_side)
    block_list=block_list.union(down_side)
    block_list=block_list.union(right_d_up)
    block_list=block_list.union(right_d_down)
    block_list=block_list.union(left_d_up)
    block_list=block_list.union(left_d_down)
    #print(block_list)
    #print(return_wall_list(house_map))
            
    flag=0
    #print(right_side)
    #new_length=len(pichu_list)
    #iterating for remaining pichus
    t=1
    for i in range(len(pichu_list)):
        #print(pichu_list)
        curr=pichu_list.pop(0)#first element popped, second element pop and check for row, column and diagonal
        if(curr in block_list):
            #print("-1")
            flag=flag+1
            return (flag,False)
        
        else:
            #14th september, add new pichu block positions to block list
            t=t+1
            right_side=row_right(house_map,*curr)
            left_side=row_left(house_map,*curr)
            up_side=col_up(house_map,*curr)
            down_side=col_down(house_map,*curr)
            right_d_up=right_up_diagonal(house_map,*curr)
            right_d_down=right_down_diagonal(house_map,*curr)
            left_d_up=left_up_diagonal(house_map,*curr)
            left_d_down=left_down_diagonal(house_map,*curr)
            wall_list=return_wall_list(house_map)

            for j in range(len(wall_list)):
                curr=wall_list.pop(0)
                #print(len(wall_list))
                if(curr in right_side):
                    free_side=row_right(house_map,*curr)
                    right_side=right_side-free_side
                if(curr in left_side):
                    free_side=row_left(house_map,*curr)
                    left_side=left_side-free_side
                if(curr in up_side):
                    free_side=col_up(house_map,*curr)
                    up_side=up_side-free_side
                if(curr in down_side):
                    free_side=col_down(house_map,*curr)
                    down_side=down_side-free_side
                if(curr in right_d_up):
                    free_side=right_up_diagonal(house_map,*curr)
                    right_d_up=right_d_up-free_side
                if(curr in right_d_down):
                    free_side=right_down_diagonal(house_map,*curr)
                    right_d_down=right_d_down-free_side
                if(curr in left_d_up):
                    free_side=left_up_diagonal(house_map,*curr)
                    left_d_up=left_d_up-free_side
                if(curr in left_d_down):
                    free_side=left_down_diagonal(house_map,*curr)
                    left_d_down=left_d_down-free_side

            block_list=block_list.union(right_side)
            block_list=block_list.union(left_side)
            block_list=block_list.union(up_side)
            block_list=block_list.union(down_side)
            block_list=block_list.union(right_d_up)
            block_list=block_list.union(right_d_down)
            block_list=block_list.union(left_d_up)
            block_list=block_list.union(left_d_down)


            
    return (flag,count_pichus(house_map)==k)

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):
    fringe = [initial_house_map]
    if(is_goal(initial_house_map,k)[1]):
        return(initial_house_map,k)
    while len(fringe) > 0:
        for new_house_map in successors( fringe.pop(0) ):
            if(is_goal(new_house_map,k)[1]):
                #print("hello")
                return(new_house_map,True)
            if(is_goal(new_house_map,k)[0]==0):
                fringe.append(new_house_map)
            else:
                continue

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    #is_goal(house_map,k)
    print (printable_house_map(solution[0]) if solution[1] else "False")


