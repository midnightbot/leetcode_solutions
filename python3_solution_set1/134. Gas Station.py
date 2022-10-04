##ss
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        gasnow = 0
        
        stops = len(gas)
        
        gas = gas + gas + gas
        cost = cost + cost + cost
        comp = 0
        #print(gas,cost)
        
        for x in range(stops,stops+stops):
            gasnow = gas[x]
            z = x
            comp = 0
            if x!=stops and cost[x] == cost[x-1] and gas[x] == gas[x-1]:
                continue
            while gasnow >= cost[z] and comp!=stops:
                gasnow-=cost[z]
                z+=1
                gasnow+=gas[z]
                comp+=1
                
            if comp == stops:
                return (x - stops)
            
            #print(comp)
        return -1
