class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        temp = Counter(str(n))
        ans = 0
        for x in temp:
            ans+=int(x)*int(temp[x])
        return ans
        
