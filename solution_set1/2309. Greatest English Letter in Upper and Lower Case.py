##ss
class Solution:
    def greatestLetter(self, s: str) -> str:
        
        print(ord('a') - ord('A'))
        
        seen = set()
        
        for x in s:
            seen.add(x)
            
            
        ans = ""
        
        for x in range(ord('a'), ord('z')+1,1):
            #print(chr(x))
            if chr(x) in seen and chr(x-32) in seen:
                ans = chr(x-32)
                
        return ans
