class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        
        return (2**(len(s)-k+1))%(10**9 + 7)
                
            
        
