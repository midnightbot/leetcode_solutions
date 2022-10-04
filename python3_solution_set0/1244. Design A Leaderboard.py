##ss
##simple dictionary + heaps
##dictionary + brute force also accepted
class Leaderboard:

    def __init__(self):
        self.dicts = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.dicts.keys():
            self.dicts[playerId]+=score
            
        else:
            self.dicts[playerId] = score
            
        

    def top(self, K: int) -> int:
        ans = []
        ##heaps in python are min heaps
        ## we want top K elements
        ##way1 , insert all elemnts, pop n-K elements, ans will be sum of left K elements
        ##way2, insert -ves of all elemtents, hence more the value more -ve it will be, then pop K elements and add the in answer and return -ve of answer
        for x in self.dicts.keys():
            heapq.heappush(ans,self.dicts[x]*-1)
            
        ret_ans = 0
        for x in range(K):
            ret_ans+=heapq.heappop(ans)*-1
            
        return ret_ans
        
        

    def reset(self, playerId: int) -> None:
        self.dicts[playerId] = 0
        
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
