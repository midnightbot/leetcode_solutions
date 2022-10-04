##ss
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        ##either buy individually or purchase it in a offer
        ##these are the two branches of recursion
        
        self.ans = 0
        for x in range(len(needs)):
            self.ans+= needs[x] * price[x]
            
        def cost(price,special,needs,thisans):
            #print(needs,thisans,special)
            if needs == [0 for x in range(len(needs))]:
                #print("insdie")
                self.ans = min(self.ans,thisans)
                
            elif self.check(needs):
                done = False
   
                for x in range(len(special)):
                    if self.submask(needs,special[x]):
                        done = True
                        newneed = copy.copy(needs)
                        #print(needs,x)
                        newans = self.buyallsingle(newneed,price)
                        self.ans = min(self.ans, newans+thisans)
                        newneed = self.subt(newneed,special[x])
                        
                        cost(price,special,newneed,thisans+special[x][-1])
                        
                if done == False:
                    temp = 0
                    for x in range(len(needs)):
                        temp+=needs[x] * price[x]
                        
                        needs[x] = 0
                        
                    cost(price,special,needs,temp + thisans)
                        
                        
        cost(price,special,needs,0)
        return self.ans
         
    def buyallsingle(self,needs,price):
        ans = 0
        for x in range(len(needs)):
            ans+=needs[x] * price[x]
            
        return ans
    
    def check(self,needs):
        
        for x in range(len(needs)):
            if needs[x] < 0:
                return False
            
        return True
    
    def submask(self,needs,offer):
        
        for x in range(len(needs)):
            if needs[x] < offer[x]:
                return False
            
        return True
    
    def subt(self,needs,offer):
        
        for x in range(len(needs)):
            needs[x]-=offer[x]
            
        return needs
