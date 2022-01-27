##ss
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #set1 = set(nums1)
        set2 = set(nums2)
        ans = []
        #print(set1,set2)
        for x in nums1:
            
            mins = float('inf')
            #print(x)
            for z in range(nums2.index(x)+1,len(nums2)):

                if nums2[z]>x and nums2[z] < mins:
                    #print(z,x)
                    mins = nums2[z]
                    break

            if mins == float('inf'):
                ans.append(-1)
            else:
                ans.append(mins)
                    
        return ans
        
