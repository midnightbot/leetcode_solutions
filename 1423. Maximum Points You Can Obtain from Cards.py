class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        ans = []
        lens = len(cardPoints)
        prev_ans = 0
        
        for x in range(k+1):
            start = (lens - k + x) % lens
            temp = 0
            
            if x == 0:
                for y in range(k):
                    temp+= cardPoints[(start+y)%lens]
                    
                prev_ans = temp
                ans.append(temp)
            else:
                
                temp = prev_ans - cardPoints[(start-1) % lens]
                temp+= cardPoints[(start+k-1)%lens]
                prev_ans = temp
                ans.append(temp)
            
        return max(ans)
                
                
                
