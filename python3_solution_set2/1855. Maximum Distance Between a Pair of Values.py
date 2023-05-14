import bisect
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ## i,j such that nums1[i] <= nums2[j]
        ## dist is j-i
        nums2 = nums2[::-1]
        n = len(nums2)
        ans = 0
        for indx1, x in enumerate(nums1):
            indx2 = bisect.bisect_left(nums2,x)
            indx2 = n - indx2
            indx2-=1
            ans = max(ans, indx2 - indx1)
            #print(indx1, indx2)

        return ans
