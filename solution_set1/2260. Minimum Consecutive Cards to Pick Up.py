##ss
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        dicts = {}
        mins = float('inf')
        
        for indx,val in enumerate(cards):
            if val in dicts:
                mins = min(mins, indx - dicts[val] + 1)
                dicts[val] = indx
                
            else:
                dicts[val] = indx
                
        return mins if mins!=float('inf') else -1
        
        
