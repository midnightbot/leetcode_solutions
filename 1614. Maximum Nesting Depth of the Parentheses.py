class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxcount = 0
        for x in range(len(s)):
            if s[x]=="(":
                count+=1
                if count > maxcount:
                    maxcount = count
                
                print(maxcount)
            elif s[x]==")":
                count-=1
        return maxcount
        
