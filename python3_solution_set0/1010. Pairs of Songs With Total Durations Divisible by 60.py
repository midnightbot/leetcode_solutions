from math import comb
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        count = [0 for x in range(60)]
        
        for x in range(len(time)):
            count[time[x]%60]+=1
            
        ans = 0
        #print(count)
        for x in range(1,30):
            ans+=count[x] * count[60-x] ##if there are say 2 numbers in group 1 and 3 numbers in group 59
            ##their any combination will be valid hence 2*3
            #print(x,ans)
        #print(ans)   
        
        ans+= comb(count[0],2) ##two numbers from group 0 will also be valid
        ans+=comb(count[30],2) ##two numbers from group 60 will also be valid
        
        return ans
        
        
