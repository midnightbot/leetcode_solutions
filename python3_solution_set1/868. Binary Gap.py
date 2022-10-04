##ss
class Solution:
    def binaryGap(self, n: int) -> int:
        
        temp = str(format(n,"b"))
        
        ans = 0
        for x in range(len(temp)-1):
            if temp[x] == '1':
                for y in range(x+1,len(temp)):
                    if temp[y] == '1':
                        ans = max(ans, y-x)
                        break
                        
        return ans
        
