class Solution:
    def countTestedDevices(self, bp: List[int]) -> int:
        count = 0

        for x in range(len(bp)):
            if bp[x] - count > 0:
                count+=1
                
        return count
        
