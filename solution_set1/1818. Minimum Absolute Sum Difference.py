##ss
import bisect
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        
        prefix = [abs(nums1[x] - nums2[x]) for x in range(len(nums1))]
        
        mods = 10**9 + 7
        comp = sorted(nums1)
        
        ## find the left-most and right-most element closest to every numebr and replace and check
        
        #print(comp)
        def check(nums):
            return [bisect.bisect_left(comp,nums), bisect.bisect_right(comp,nums)]
        
        def valid(arr):
            ans = []
            for x in arr:
                if 0<=x<len(comp):
                    ans.append(x)
                    
                if 0<=x-1<len(comp):
                    ans.append(x-1)
                    
                if 0<=x+1<len(comp):
                    ans.append(x+1)
                    
            return ans
        
        result = sum(prefix)
        ans = sum(prefix)
        #print(result)
        for x in range(len(nums1)):
            indx = valid(check(nums2[x]))
            
            #result-=abs(nums1[x] - nums2[x])
            
            mins = float('inf')
            #print(x,indx)
            for y in indx:
                mins = min(mins, abs(comp[y] - nums2[x]))
             
            ans = min(ans, result - abs(nums1[x] - nums2[x]) + mins)
            #print(ans,mins,abs(nums1[x] - nums2[x]))
        
        return ans%mods
            
        
