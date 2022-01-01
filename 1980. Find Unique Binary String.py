##ss
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        for x in range(len(nums)):
            nums[x] = self.make_int(nums[x])
            
        #print(nums)
        nums = sorted(nums)
        #print(nums)
        prev = 0
        for x in range(len(nums)):
            if nums[x]!=prev:
                break
                
            else:
                prev+=1
                
        return self.make_bin(prev,len(nums))
        
    def make_int(self,nums):
        
        n = len(nums)
        ans =  0
        for x in range(n):
            ans+= int(nums[x]) * pow(2,x)
            
        return ans
    
    
    def make_bin(self,ans,n):
        
        temp = ""
        for x in range(n):
            if ans & (1<<x)!=0:
                temp+="1"
                
            else:
                temp+="0"
        return temp
        
            
        
