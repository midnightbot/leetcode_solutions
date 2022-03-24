##ss
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        maxs = max(damage)
        
        if maxs > armor:
            return sum(damage) - maxs + (maxs - armor) + 1
        
        else:
            return sum(damage) - maxs + 1
        
