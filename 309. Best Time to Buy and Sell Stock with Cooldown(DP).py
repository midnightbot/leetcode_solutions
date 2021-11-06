class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        opt = [0]*len(prices)
        opt[0] = 0
        if len(prices) == 1:
            return 0
        elif len(prices) == 2 and (prices[1]-prices[0])>0:
            return prices[1] - prices[0]
        elif len(prices) == 2 and (prices[1]-prices[0])<=0:
            return 0
        
            
        if prices[1] > prices[0]:
            opt[1] = prices[1] - prices[0]
            
        temp1 = prices[1] - prices[0]
        temp2 = prices[2] - prices[1]
        temp3 = prices[2] - prices[0]
        maxss = max(temp1,temp2,temp3)
        if maxss > 0:
            opt[2] = maxss

        for i in range(3,len(prices)):
            maxs = -float('inf')
            #print(maxs)
            for j in range(2,i):
                if prices[i] > prices[j]:
                    temp = prices[i] - prices[j] + opt[j-2]
                    if temp > maxs:
                        maxs = temp
                        
            #print("hi",prices[i]-prices[0])
            #print(i,maxs)
            opt[i] = max(opt[i-1],maxs,0,prices[i]-prices[1],prices[i] - prices[0])
        print(opt)
                
        return max(opt)   
            
        #print(opt)
        
