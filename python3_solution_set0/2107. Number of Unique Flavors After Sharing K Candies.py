##ss
class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        
        dicts = {}
        
        for x in range(len(candies)):
            if candies[x] in dicts.keys():
                dicts[candies[x]]+=1
                
            else:
                dicts[candies[x]] = 1
                
        for x in range(k):
            dicts[candies[x]]-=1
            
        ans = - float('inf')
        #ans = max(ans,self.find_unq(dicts))
        count = self.find_unq(dicts)
        ans = max(ans,count)
        #print(dicts)
        #print(count)
        
                
        for x in range(1,len(candies)-k+1):
            #print(dicts)
            #print(count,dicts,"--->",x)
            if dicts[candies[x-1]]!=0:
                dicts[candies[x-1]]+=1
                
            elif dicts[candies[x-1]] == 0 : ##new flavor hence increase count
                count+=1
                dicts[candies[x-1]] = 1
                
                
            dicts[candies[x+k-1]]-=1
            if dicts[candies[x+k-1]] == 0: ##this flavor completely given, so reduce count
                count-=1
                #dicts.pop(candies[x+k-1],None)
            #print(count, "->",x)
            ans = max(ans,count)
        
        return ans
    def find_unq(self,dicts):
        
        ans = 0
        for x in dicts.keys():
            if dicts[x]!=0:
                ans+=1
            
        return ans
