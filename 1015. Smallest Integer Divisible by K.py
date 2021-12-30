class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k%2 == 0:
            return -1
        
        #strs = "1"
        rem = 0
        
        for x in range(1,k+1):
            
            rem = (rem*10 + 1) % k
            #print(rem)
            if rem == 0:
                return x
                #return int(strs)
            
            #strs+="1"
            
        return -1
        
