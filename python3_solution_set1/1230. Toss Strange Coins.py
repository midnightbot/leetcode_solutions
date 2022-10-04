##ss
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        
        ##exactly 'target' number of heads
        ## simple prob solution would be (n C target) groups multiplied with their probability
        
        ##solving it with dp
        
        @lru_cache(None)
        def solve_dp(pos,k):
            #print(pos,k)
            
            if k == 0 and pos == len(prob):
                return 1
            
            elif k > 0 and pos == len(prob):
                return 0
            
            elif k < 0:
                return 0
            
            elif pos < len(prob):
                #ans = 1
                temp1 = (1-prob[pos]) * solve_dp(pos+1,k)
                temp2 = (prob[pos]) * solve_dp(pos+1,k-1)
                
                return temp1 + temp2
            
            
        return solve_dp(0,target)
        #return ans
