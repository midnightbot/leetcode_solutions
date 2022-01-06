##ss
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        
        
        for x in range(len(s)//2):
            if (len(s)-x-1)%(x+1) == 0:
                #print("inside",x)
                temps = s[0:x+1]
                for y in range((len(s)-x-1) // (x+1)):
                    temps+=s[0:x+1]
                    
                #print(temps)   
                if temps == s:
                    return True
                
        return False
