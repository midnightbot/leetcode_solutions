##ss
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        ans = 0
        
        left = 0
        #print(numBottles , numExchange)
        while numBottles + left >= numExchange:
            #print("inside")
            ans+=numBottles
            left+= numBottles % numExchange
            numBottles = numBottles // numExchange
            
            if left >= numExchange:
                numBottles+= left // numExchange
                left = left % numExchange
              
        
            
        return (ans + numBottles)
            
            
            
        
