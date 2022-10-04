##ss
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        
        i = 0
        diff = []
        for x in range(1,len(nums)):
            diff.append(nums[x]-nums[x-1])
            
        ans = []
        if len(nums) < 3:
            return 0
        while i < len(diff):
            pt = False
            #print(i)
            for x in range(i+1,len(diff)):
                if diff[x] != diff[i]:
                    pt = True
                    break
                    
            if pt == True and x-i >=2:
                ans.append((i,x))
                i = x
                
            elif pt== False:
                ans.append((i,x+1))
                i = x+1
            else:
                i+=1
                
        #print(ans)
        count = 0
        for x in range(len(ans)):
            count+=self.counts(ans[x])
            
        return count
        
    def counts(self,arr):
        #print(arr)
        c = 3
        total = 0
        while c <= arr[1] - arr[0] + 1:
            total += arr[1] - arr[0] - c + 2
            #print(total)
            c+=1
            
        return total
            
            
        
        
        
        
        
