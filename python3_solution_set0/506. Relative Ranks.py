##ss
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        ans = [-1 for x in range(len(score))]
        score = [[score[x],x] for x in range(len(score))]
        
        score = sorted(score, reverse= True, key = lambda x:x[0])
        print(score)
        
        for x in range(len(score)):
            ans[score[x][1]] = str(x+1)
            
        for x in range(len(ans)):
            if ans[x] == "1":
                ans[x] = "Gold Medal"
                
            elif ans[x] == "2":
                ans[x] = "Silver Medal"
                
                
            elif ans[x] == "3":
                ans[x] = "Bronze Medal"
                
        return ans
