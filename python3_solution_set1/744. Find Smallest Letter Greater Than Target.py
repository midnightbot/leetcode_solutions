class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        letters = letters + letters
        
        for x in letters:
            if x > target:
                return x
            
        return letters[0]
