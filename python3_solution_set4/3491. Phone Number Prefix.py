class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:

        n = len(numbers)

        for x in range(n):
            for y in range(x+1, n):
                mins = min(len(numbers[x]), len(numbers[y]))
                if numbers[x][:mins] == numbers[y][:mins]:
                    return False
        
        return True
        
