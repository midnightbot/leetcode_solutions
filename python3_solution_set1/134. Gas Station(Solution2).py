class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        
        total = 0
        curr = 0
        start = 0
        for x in range(len(gas)):
            total+= gas[x] - cost[x]
            curr += gas[x] - cost[x]
            
            if curr < 0:
                start = x+1
                curr = 0
                
                
        if total>=0:
            return start
        else:
            return -1
            
        
