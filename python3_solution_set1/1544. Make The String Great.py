##ss
class Solution:
    def makeGood(self, s: str) -> str:
        
        ans = False
        
        #print(ord('a'))
        #print(ord('A'))
        #print(ord('B')-ord('b'))
        while ans == False:
            change = False
            for x in range(len(s)-1):
                
                if abs(ord(s[x]) - ord(s[x+1])) == 32:
                    change = True
                    s = s[0:x] + s[x+2:]
                    
                    break
                    
            if change == False:
                ans = True
                
        return s
        
