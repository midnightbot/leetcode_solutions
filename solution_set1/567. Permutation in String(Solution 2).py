##ss
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        comp1 = self.make_map(s1)
        
        temp1 = s2[0:len(s1)]
        comp2 = self.make_map(temp1)
        
        if self.samee(comp1,comp2):
            return True
        for x in range(len(s1),len(s2),1):
            comp2[ord(s2[x-len(s1)]) - ord('a')]-=1
            
            comp2[ord(s2[x])-ord('a')]+=1
            #print(comp2)
            if self.samee(comp1,comp2):
                return True
            
        return False
            
        
        
    def make_map(self,s1):
        
        ans = [0 for x in range(26)]
        
        for x in range(len(s1)):
            ans[ord(s1[x])-ord('a')]+=1
            
        return ans
        
    def samee(self,s1,s2):
        
        for x in range(26):
            if s1[x]!=s2[x]:
                return False
            
        return True
