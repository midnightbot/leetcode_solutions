##ss
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        comp = ""
        ans = -1
        
        for x in range(len(num) - 2):
            
            thisnums = num[x:x+3]
            
            if (thisnums[0] == thisnums[1] == thisnums[2]) and int(thisnums) > ans:
                ans = int(thisnums)
                comp = thisnums
                
        return comp
        
