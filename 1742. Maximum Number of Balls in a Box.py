class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        ans = {}
        #ans[10] = 100
        #print(ans[10])
        num = highLimit-lowLimit+1
        for x in range(lowLimit,highLimit+1,1):
            sums = 0
            for digit in str(x):
                sums+=int(digit)
                #print(sums)
            if sums in ans.keys():
                ans[sums]+=1
            else:
                ans[sums]=1
            #print(ans)
            
        return max(list(ans.values()))
        
