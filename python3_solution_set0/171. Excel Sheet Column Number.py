class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        comp = [x for x in str(columnTitle)]
        #print(comp,ord('A'),ord('Z')) ##-64
        #print(ord('Y')-64)
        ans = 0
        for x in range(len(comp)):
            ans *=26
            comp[x] = ord(comp[x]) - 64
            ans+=comp[x]
            
        return ans
           
            
       
            
        
        
        
