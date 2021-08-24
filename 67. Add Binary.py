class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a_int = int(a,2)
        b_int = int(b,2)
        
        #print(a_int+b_int)
        
        ans = format(a_int+b_int,"b")
        
        return ans
        
