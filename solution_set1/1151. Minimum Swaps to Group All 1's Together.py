class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        pre = []
        
        pre.append(data[0])
        
        for x in range(1,len(data)):
            #print(data[x])
            pre.append(pre[-1] + data[x])
            #print(pre)
            
        counts = data.count(1)
        
        #print(counts)
        #print(pre)
        ans = counts - pre[counts-1]
        #print(ans)
        #pre.insert(0,0)
        for x in range(1,len(pre)-counts):
            #print(x)
            ans = min(ans, counts - pre[x+counts] + pre[x])
        return ans
        
