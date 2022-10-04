##ss
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        return (int(coordinates[1]) + (ord(coordinates[0])-ord('a'))) % 2 == 0
        
        
        
