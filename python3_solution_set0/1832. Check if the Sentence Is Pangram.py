class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        unique = []
        if len(sentence) < 26:
            return False
        
        else:
            for char in sentence[::]:
                if char not in unique:
                    unique.append(char)
                    
            if len(unique)==26:
                return True
            
            else:
                return False
                
        
