##ss
from itertools import permutations
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        
        
        ##brute force approach
        ## as size of matrix is small (3X3 atmost), trying out all possible combination of flips
        comp = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
        
        ## basic idealogy is flip can be done at a position or not done at that position
        ##this makes 2 branches of our recursion
        
        
        temp = copy.deepcopy(mat)
        print(mat)
        ans = []
        points = [] ##contains all positions
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                points.append([x,y])
             
        #print(points," ")
        #print("*")
        l = list(permutations(points))
  
        #for x in range(len(l)):
            #tempo = copy.deepcopy(mat)
        self.flips(temp,0,ans,comp,0,l[x])
        
        if len(ans) == 0:
            return -1
        
        return min(ans)

        
    def flips(self,grid,pos,ans,comp,steps,points):
        
        #print(grid)
        
        if self.check(grid,comp):
            #print(grid)
            ans.append(steps)

        if pos < len(points): ##trying out all permutations for all points
            curr = points[pos]
            temps = copy.deepcopy(grid)

            if curr[0] - 1 >=0:
                if temps[curr[0]-1][curr[1]] == 1:
                    temps[curr[0]-1][curr[1]] = 0

                else:
                    temps[curr[0]-1][curr[1]] = 1


            if curr[0] + 1 < len(grid):
                if temps[curr[0]+1][curr[1]] == 1:
                    temps[curr[0]+1][curr[1]] = 0

                else:
                    temps[curr[0]+1][curr[1]] = 1


            if curr[1]-1>=0:
                if temps[curr[0]][curr[1]-1] == 1:
                    temps[curr[0]][curr[1]-1] = 0

                else:
                    temps[curr[0]][curr[1]-1] = 1


            if curr[1] + 1 < len(temps[0]):
                if temps[curr[0]][curr[1]+1] == 0:
                    temps[curr[0]][curr[1]+1] = 1


                else:
                    temps[curr[0]][curr[1]+1] = 0


            if temps[curr[0]][curr[1]] == 0:
                temps[curr[0]][curr[1]] = 1

            else:
                temps[curr[0]][curr[1]] = 0


            self.flips(grid,pos+1,ans,comp,steps,points) ##flip not done at this positions
            self.flips(temps,pos+1,ans,comp,steps+1,points) ##flip done on this position , hence steps+1
                

    def check(self,arr1,arr2): ##checking if array is all zeros now
        
        for x in range(len(arr1)):
            for y in range(len(arr1[0])):
                if arr1[x][y]!=arr2[x][y]:
                    return False
                
                
        return True
        
        
                
