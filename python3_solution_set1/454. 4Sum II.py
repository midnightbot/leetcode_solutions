##ss
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        dicts = {}
        result  = 0
        for x in range(len(nums1)):
            for y in range(len(nums2)):
                ans = nums1[x] + nums2[y]
                if ans in dicts:
                    dicts[ans]+=1
                    
                else:
                    dicts[ans] = 1
                    
        for x in range(len(nums3)):
            for y in range(len(nums4)):
                ans = nums3[x] + nums4[y]
                
                result+= dicts.get(-1*ans,0)
                
        return result
        
