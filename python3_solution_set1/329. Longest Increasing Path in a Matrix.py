##ss
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ##memo[(x,y)] give length of longest inc path from x,y
        ##up,down,left,right are valid moves
        
        ##try from every start point and find max path length from that point
        
        maxs =-1
        for x in range(len(matrix)):
            maxs = max(maxs,max(matrix[x]))
            
        result = -1
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                memo = {}
                self.expand(matrix,x,y,maxs,memo)
                result = max(result,memo[(x,y)])
        #print(memo)
        return result
    
    def expand(self,matrix,x,y,maxs,memo): ##function finds length of longest inc path from point (x,y)
        
        if matrix[x][y] == maxs:
            memo[(x,y)] = 1
            return memo[(x,y)]
        
        if (x,y) in memo:
            return memo[(x,y)]
        
        elif x < len(matrix) and y < len(matrix[0]):
            t1=  0
            t2 = 0
            t3 = 0
            t4 = 0
            
            if x-1>=0 and matrix[x-1][y] > matrix[x][y]:
                t1 = self.expand(matrix,x-1,y,maxs,memo)
                
            if x+1<len(matrix) and matrix[x+1][y] > matrix[x][y]:
                t2 = self.expand(matrix,x+1,y,maxs,memo)
                
            if y-1>=0 and matrix[x][y-1] > matrix[x][y]:
                t3 = self.expand(matrix,x,y-1,maxs,memo)
                
            if y+1 < len(matrix[0]) and matrix[x][y+1] > matrix[x][y]:
                t4 = self.expand(matrix,x,y+1,maxs,memo)
                
            memo[(x,y)] = 1 + max(t1,t2,t3,t4)
            
            return memo[(x,y)]
        
        
        
