class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for x in range(len(nums1)):
            temp = nums1[x]
            okok = nums2.index(temp)
            ans.append(okok)
            nums2[okok] = -1
            
        
        return ans
