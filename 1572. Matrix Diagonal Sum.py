class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1 = 0
        sum2 = 0
        
        for x in range(len(mat)):
            sum1+=mat[x][x]
            
        #print(sum1)
            
        for y in range(len(mat)):
            sum2+=mat[len(mat)-y-1][y]
        
        if len(mat)%2!=0:
            temp = int(len(mat)/2)
            sum2-= mat[temp][temp]
        #print(sum2)
            
            
        return sum1+sum2
        
