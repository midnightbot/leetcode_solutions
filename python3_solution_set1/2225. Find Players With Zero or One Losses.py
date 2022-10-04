##ss
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        ## no lost matches
        ## lost one match
        
        
        winner = Counter(matches[x][0] for x in range(len(matches)))
        loser = Counter(matches[x][1] for x in range(len(matches)))
        
        #print(winner, loser)
        p1 = []
        p2 = []
        
        for x in winner:
            if x not in loser:
                p1.append(x)
                
            
                
                
        for x in loser:
            if loser[x] == 1:
                p2.append(x)
                
        p1 = sorted(p1)
        p2 = sorted(p2)
        return [p1,p2]
