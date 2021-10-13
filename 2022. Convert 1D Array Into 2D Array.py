class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        ans = []
        temp  = []
        
        if m*n != len(original):
            return []
        for x in range(len(original)):
            
            if len(temp) == n:
                ans.append(temp)
                temp = []
                temp.append(original[x])
            else:
                
                temp.append(original[x])
                
                
        ans.append(temp)        
        return ans
        
