##ss
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        grps = []
        
        prev = s[0]
        count = 1
        for x in range(1,len(s)):
            if prev == s[x]:
                count+=1
                
            else:
                grps.append([prev,count])
                prev = s[x]
                count = 1
                
        grps.append([prev,count])
        ans  = 0
        for x in range(len(grps)-1):
            if grps[x][0]!=grps[x+1][0]:
                ans+=min(grps[x][1],grps[x+1][1])
                
                
        return ans
            
        #print(grps)
            
