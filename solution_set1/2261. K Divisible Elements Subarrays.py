##ss
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        
        ## atmost 'k' elems div by p
        
        ans = 0
        
        def check(arr):
            return [x%p for x in arr].count(0)
        
        seen = set()
        def make_str(arr):
            return '.'.join([str(x) for x in arr])
        
        for x in range(len(nums)):
            temp = ''
            count = 0
            for y in range(x,len(nums)):
                if nums[y]%p==0:
                    count+=1
                    temp+=','+str(nums[y])
                    if count <= k and temp not in seen:
                        seen.add(temp)
                        ans+=1
                        
                    elif count > k:
                        break
                else:
                    temp+=','+str(nums[y])
                    if temp not in seen:
                        seen.add(temp)
                        ans+=1
                        
                
                    
            
                
        return ans
        
        
