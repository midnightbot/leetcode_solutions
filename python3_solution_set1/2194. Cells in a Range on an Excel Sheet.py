##ss
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        diff = int(s[4]) - int(s[1])
        r1 = s[0]
        r2 = s[3]

        ans = []
        
        for x in range(int(s[1]), int(s[1]) + diff + 1):
            ans.append(r1 + str(x))
            
        for x in range(ord(r1)+1, ord(r2)+1):
            
            for y in range(int(s[1]), int(s[4]) + 1):
                ans.append(chr(x) + str(y))
                
            
        return ans
            
        
