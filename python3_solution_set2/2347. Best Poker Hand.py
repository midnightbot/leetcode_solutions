class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        
        temp1 = Counter(ranks)
        temp2 = Counter(suits)
        
        if len(temp2.keys()) == 1:
            return "Flush"
        
        if max(temp1.values()) >= 3:
            return "Three of a Kind"
        if max(temp1.values()) == 2:
            return "Pair"
            
        return "High Card"
        
