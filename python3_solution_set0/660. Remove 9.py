##ss
class Solution:
    def newInteger(self, n: int) -> int:
        
        ans = ''
        while n:
            ans+=str(n%9)
            n = n // 9
            
        ans = ans[::-1]
        return int(ans)
