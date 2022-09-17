import bisect
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        ans = 0
        players = sorted(players)
        trainers = [-1] + sorted(trainers)
        i = 0
        t = len(trainers)
        for x in players:
            done = False
            while i < t and x > trainers[i]:
                i+=1
                
            if i < t and x <= trainers[i]:
                ans+=1
                i+=1
                
        return ans
                
            
        
