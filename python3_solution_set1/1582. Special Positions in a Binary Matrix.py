##ss
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        rowsum = [0 for x in range(len(mat))]
        colsum = [0 for x in range(len(mat[0]))]
        
        for x in range(len(mat)):
            rowsum[x] = sum(mat[x])
            
        for x in range(len(mat[0])):
            ans = 0
            for y in range(len(mat)):
                ans+=mat[y][x]
                
            colsum[x] = ans
            
        count = 0
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                
                if mat[x][y] == 1 and rowsum[x] == 1 and colsum[y] == 1:
                    count+=1
                    
        return count
