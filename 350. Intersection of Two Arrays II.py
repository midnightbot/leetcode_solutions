class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        for x in range(len(nums1)):
            for y in range(len(nums2)):
                if nums1[x] == nums2[y]:
                    ans.append(nums1[x])
                    nums1[x] = -1
                    nums2[y] = -2
                    break
                    
        return ans
        
