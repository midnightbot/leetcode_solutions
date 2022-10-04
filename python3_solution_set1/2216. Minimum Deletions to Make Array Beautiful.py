##ss
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        
        ## len of nums is even
        ## nums[i] % nums[i+1] for all i%2 == 0
        stack = []
        dels = 0
        
        for x in nums:
            if len(stack)%2 != 0 and stack and stack[-1] == x:
                dels+=1
                
            else:
                stack.append(x)
                
            #print(stack)
            
        if stack and len(stack) > 2 and len(stack)%2!=0 and stack[-1] == stack[-2]:
            dels+=1
            stack.pop()
            
        elif len(stack)%2!=0:
            dels+=1
            
        return dels
            #stack.append(x)
            
        
