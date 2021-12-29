##SS
##Solution 1 (Recursion + Memoization)
##simple recursion with memoization
##key (curr,fuelleft) , therefore momo[(curr,fuelleft)] gives ways to reach end from curr position with fullleft fuel
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        final = set()
        ans = []
        memo = {}
        
        self.expand(locations,start,finish,fuel,ans,final,memo)
        #return len(final)%(pow(10,9)+7)
        return (memo[(start,fuel)]) % (pow(10,9)+7)
    
    def expand(self,locations,curr,finish,fuel,ans,final,memo):
        
        
        if fuel < 0:
            return 0
        
        ways = 0
        if curr == finish:
            ways+=1
            
        if (curr,fuel) in memo:
            return memo[(curr,fuel)] % (pow(10,9)+7)
        
        
        else:
            #ways = 0
            for x in range(len(locations)):
                if x!=curr and fuel - abs(locations[x]-locations[curr]) >=0:
                    #ans.append(x)
                    ways+=self.expand(locations,x,finish,fuel-abs(locations[x]-locations[curr]),ans,final,memo)
                    #ans.pop(len(ans)-1)
                    
            memo[(curr,fuel)] = ways % (pow(10,9)+7)
            return memo[(curr,fuel)]
        
