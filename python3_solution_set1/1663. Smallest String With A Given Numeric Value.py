##ss
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ## length 'n' and numerical value = 'k'
        
        ans = ""
        i = 0
        
        while i < n:
            #print(n,ans)
            for x in range(1,27):
                if k - x <= 26 * (n - i - 1):
                    ans+=chr(x - 1 + ord('a'))
                    k-= x
                    break
            i+=1
        
        return ans
