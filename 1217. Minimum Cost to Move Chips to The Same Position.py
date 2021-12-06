class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        
        ##bring all even index coins to 0 by -2 operation
        ## bring all odd index coins to 1 by -2 operation
        
        ##then shift one of the tower above other
        
        ans = [x for x in position if x%2==0]
        count1 = len(ans)
        
        return min(count1, len(position)-count1)
        
