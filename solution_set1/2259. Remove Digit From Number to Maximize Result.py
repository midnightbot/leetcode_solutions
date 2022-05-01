##ss
class Solution:
    def removeDigit(self, numbers: str, digit: str) -> str:
        
        options = []
        
        indx = []
        
        for x in range(len(numbers)):
            if numbers[x] == digit:
                indx.append(x)
                
                
        for x in indx:
            options.append(numbers[0:x] + numbers[x+1:])
        
        options = [int(x) for x in options]
        options.sort()
        
        return str(options[-1])
        
