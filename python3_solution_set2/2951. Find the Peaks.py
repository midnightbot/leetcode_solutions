class Solution:
    def findPeaks(self, m: List[int]) -> List[int]:
        ans = []
        for x in range(1, len(m)-1):
            if m[x-1] < m[x] > m[x+1]:
                ans.append(x)
        return ans
        
