class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        ## bit comparison
        
        comp1 = [0 for x in range(30)]
        comp2 = [0 for x in range(30)]
        
        
        for x in range(1,len(nums)):
            temp = format(x,"b")
            c = str(temp)
            #c = c[::-1]
            l = len(comp1) - 1
            for k in range(len(c)-1,-1,-1):
                if c[k] == '1':
                    comp1[l]+=1
                    
                l-=1
                
        for x in range(len(nums)):
            temp = format(nums[x],"b")
            c = str(temp)
            l = len(comp2) - 1
            
            for k in range(len(c)-1,-1,-1):
                if c[k] == '1':
                    comp2[l]+=1
                    
                l-=1
               
        #print(comp1,comp2)
        temp = [str(min(max(comp2[x]-comp1[x],0),1)) for x in range(30)]
        final_s = "".join(temp)
        
        return int(final_s,2)
