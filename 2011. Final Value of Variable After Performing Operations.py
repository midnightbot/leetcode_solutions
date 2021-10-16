class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        ans = 0
        
        for x in range(len(operations)):
            if operations[x][0] == '-' or operations[x][1] == '-':
                ans = ans - 1
                
            else:
                ans = ans +1
                
        return ans
                
            
        
