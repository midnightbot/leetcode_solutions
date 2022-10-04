class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0
        ans = []
        for x in range(len(s)):
            if s[x]!=" ":
                count+=1
            elif s[x] == " ":
                ans.append(count)
                count = 0
                
                
        ans.append(count)
        #print(ans)
        if len(ans) ==1:
            return count
        elif len(ans) > 1 and count==0:
            for z in range(len(ans)-1,-1,-1):
                #print("inside")
                if ans[z]!=0:
                    return ans[z]
                
            return 0
        else:
            return count
        
