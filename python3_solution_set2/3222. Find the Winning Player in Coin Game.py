class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        
        turn = min(x, y//4)
        return "Alice" if turn%2!=0 else "Bob"
        
