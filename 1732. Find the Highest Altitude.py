class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=[]
        ans.append(0)
        sums = 0
        for x in range(len(gain)):
            sums = sums + gain[x]
            ans.append(sums)
        return max(ans)
            
        
