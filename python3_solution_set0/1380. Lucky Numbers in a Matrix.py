##ss
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        
        mins_r = []
        for x in range(len(matrix)):
            mins_r.append(min(matrix[x]))
            
        mins_c = []
        for x in range(len(matrix[0])):
            temp = -float('inf')
            for y in range(len(matrix)):
                if matrix[y][x] > temp:
                    temp = matrix[y][x]
                    
            mins_c.append(temp)
            
        ans = set(mins_r).intersection(set(mins_c))  
        return ans
                
            
        
        
