##ss
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        pre = []
        
        sums = 0
        
        for x in nums:
            sums+=x
            pre.append(sums)
            
        post = []
        
        sums = 0
        for x in nums[::-1]:
            sums+=x
            post.append(sums)
           
        post = post[::-1]
        
        c = 0
        
        for x in range(len(pre)-1):
            if pre[x] >= post[x+1]:
                c+=1
                
            #print(c)
            
        #print(pre)
        #print(post)
        return c
            
        
