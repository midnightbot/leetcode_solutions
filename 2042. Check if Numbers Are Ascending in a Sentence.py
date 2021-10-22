class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        temp = [int(x) for x in s.split() if x.isdigit()]
        
        if temp == sorted(temp) and len(temp) == len(set(temp)):
            return True
        else:
            return False
                
        
