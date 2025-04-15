class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        skip = 0

        for x in fruits:
            placed = False
            for y in range(len(baskets)):
                if baskets[y] >= x:
                    baskets[y] = -1
                    placed = True
                    break
            
            if not placed:
                skip+=1
                
        return skip
        
