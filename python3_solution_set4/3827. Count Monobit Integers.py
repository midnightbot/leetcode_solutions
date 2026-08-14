class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 0
        for x in range(n+1):
            temp = (format(x,'b'))
            if len(set(temp)) == 1:
                ans+=1
        return ans
        
