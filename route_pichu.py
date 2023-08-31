#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [Sushant Nirantar sniranta]
#
# Based on skeleton code provided in CSCI B551, Fall 2021.
from collections import deque
import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

def check_mov(row1,col1,row2,col2):
        #st=""
        if(col1==col2):
                if(row1<row2):
                        return "D"
                else:
                        return "U"
        if(row1==row2):
                if(col1<col2):
                        return "R"
                else:
                        return "L"
# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        my_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="@"][0]
        fringe=[(pichu_loc,0)]
        visited=set()
        solu={}
        while fringe:
                (curr_move, curr_dist)=fringe.pop(0)
                visited.add(curr_move)
                #return curr_move
                for move in moves(house_map,*curr_move):
                        
                        if not move in visited:
                                visited.add(move)
                                solu.setdefault(curr_move, [])
                                solu[curr_move].append(move)

                                if house_map[move[0]][move[1]]=="@":
                                        #return (curr_dist+1, "")  # return a dummy answer
                                        #return solu
                                        break
                                        
                                else:
                                        fringe.append((move,curr_dist+1))
        solu_values=solu.values()
        sol_val=[]
        sol_key=[]
        for i in solu_values:
                sol_val.append(i)
        solu_keys=solu.keys()
        for i in solu_keys:
                sol_key.append(i)
        #print(sol_val)
        #print(sol_key)
        real_sol=[]
        #for i in sol_val:
        #        if my_loc in i:
        #                print(sol_val.index(i))
        #print(sol_val[len(sol_val)-1])
        flag=0
        for i in sol_val:
                if my_loc in i:
                        flag=flag+1 
        if flag==0:
                return (-1,"")
        v=my_loc
        k=my_loc

        while k!=pichu_loc:
                ind=0
                for i in sol_val:
                        if v in i:
                                ind=sol_val.index(i)
                                real_sol.append(v)
                                k=sol_key[ind]
                        else:
                                
                                #print("-1")
                                ind = -1 #use break over here(return -1)
                v=k
        i=len(real_sol)-1
        rev_sol=[]
        while i>=0:
                rev_sol.append(real_sol[i])
                i=i-1
        #print(real_sol)
        initial_pos=pichu_loc
        #move xchecker
        st=""
        rev_sol_copy=rev_sol.copy()
        while rev_sol:

                new_pos=rev_sol.pop(0)
                st+=check_mov(*initial_pos,*new_pos)
                initial_pos=new_pos
        #print(st)
        if(my_loc==rev_sol_copy[len(rev_sol_copy)-1]):
                return (len(real_sol),st)
        #else:
                
                #return (-1, "")
        #print(rev_sol_copy[len(rev_sol_copy)-1])
        #return(len(real_sol),st)
        


        
                                        

                       
                                        
                        
                


# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        #search(house_map)
        #print(search(house_map))
        print("Here's the solution I found:")

        print(str(solution[0]) + " " + solution[1])


