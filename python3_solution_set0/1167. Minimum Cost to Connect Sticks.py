##ss
## always add two of the smallest stick
##greedy approach, AOA Week 2
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        sticks = sorted(sticks)
        size = 0
        cost = 0
        while len(sticks)!=1:
            s1 = sticks.pop(0)
            s2 = sticks.pop(0)
            
            cost+=s1+s2
            sticks.append(s1+s2)
            sticks = sorted(sticks)
            #print(sticks,cost)
            #sticks.append()
        
        return cost
        
