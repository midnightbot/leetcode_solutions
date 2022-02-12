##ss
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        
        ans = set()
        comp = [0 for x in range(10)]
        
        for x in range(len(s)-1):
            comp = [0 for x in range(10)]
            comp[ord(s[x])-ord('0')]+=1
            for y in range(x+1,len(s)):
                comp[ord(s[y])-ord('0')]+=1
                if self.compare(comp):
                    ans.add(s[x:y+1])
                    
        for x in range(len(s)):
            ans.add(s[x])
        #print(ans)   
        return len(ans)
        
        
    def compare(self,arr):
        maxs = max(arr)
        for x in range(10):
            if arr[x]!=0 and arr[x]!=maxs:
                return False
            
        return True
