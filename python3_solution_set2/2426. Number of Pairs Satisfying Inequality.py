import bisect
from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        ## nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff
        
        
        temp = SortedList()
        n = len(nums1)
        ans = 0
        for x in range(n):
            indx = temp.bisect_right(nums1[x] - nums2[x] + diff)
            ans+=indx
            temp.add(nums1[x] - nums2[x])
            
        return ans
