##ss
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.vote = {}
        self.winner = {}
        self.ans = []
        for x in range(len(times)):
            if persons[x] in self.vote:
                self.vote[persons[x]]+=1
                
            else:
                self.vote[persons[x]] = 1
                
            maxs = -float('inf')
            winners = []
            for z in self.vote:
                if self.vote[z] > maxs:
                    maxs = self.vote[z]
                    winners = [z]
                    
                elif self.vote[z] == maxs:
                    winners.append(z)
                    
            if len(winners) == 1:
                self.winner[times[x]] = winners[0]
                
            else:
                for k in range(x,-1,-1):
                    if persons[k] in winners:
                        self.winner[times[x]] = persons[k]
                        break
                        
        for x in self.winner:
            self.ans.append([x,self.winner[x]])

    def q(self, t: int) -> int:
        left = 1
        right = len(self.ans)
        
        #mid = left + (right-left)//2
        
        while left < right:
            mid = left + (right-left)//2
            if self.ans[mid][0] > t:
                right = mid
                
            elif self.ans[mid][0] == t:
                return self.ans[mid][1]
            
            else:
                left = mid + 1
                
        #print(mid)
        return self.ans[right-1][1]
        
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
