class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        sorted_piles = sorted(piles)
        #print(sorted_piles)
        count = 0
        counter = 1
        lens = len(piles)
        while counter!=int(len(piles)/3)+1:
            #print(sorted_piles[lens-2*counter])
            count+=sorted_piles[lens-2*counter]
            counter+=1
            
        return count
        
