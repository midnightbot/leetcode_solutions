##ss
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        result =  float('inf')
        
        
        nums = sorted(nums)
        
        
        
        
        def twosum(nums,make):
            left = 0
            right = len(nums) - 1
            ans = float('inf')
            thissusm = 0
            #print(make,nums)
            #print(nums)
            while left < right:
                #print(left,right,nums[left]+nums[right])
                #print(nums[left] + nums[right],nums,make)
                if nums[left] + nums[right] == make:
                    thissum = nums[left] + nums[right]
                    
                    return make
                
                elif nums[left] + nums[right] > make:
                    #ans = min(ans,abs(make-(nums[left]+nums[right])))
                    if abs(make-(nums[left]+nums[right])) < ans:
                        ans = min(ans,abs(make-(nums[left]+nums[right])))
                        thissum = nums[left] + nums[right]
                        
                    right-=1
                    
                else:
                    
                    #print("thiscase",abs(make-(nums[left]+nums[right])))
                    if abs(make-(nums[left]+nums[right])) < ans:
                        ans = min(ans,abs(make-(nums[left]+nums[right])))
                        thissum = nums[left] + nums[right]
                    #ans = min(ans,abs(make-(nums[left]+nums[right])))
                    left+=1
            #print("ans",ans)        
            return thissum
            
            
        #print(nums,"original")   
       #ans  = twosum(nums[0:1]+nums[2:],target-nums[1])   
        #print(ans)
        chck = float('inf')
        finals = 0
        for x in range(len(nums)):
            temp = nums[x]
            nums.pop(x)
            thisans = twosum(nums,target - temp)
            #print(nums,target-temp,thisans,temp)
            nums.insert(x,temp)
            #print(thisans,temp)
            thissums = thisans + temp
            
            if abs(target - thissums) < chck:
                chck = abs(target - thissums)
                finals = thissums
            #result = min(result,thisans+temp)
            
            
        return finals
        
