class Solution:
    def isBalanced(self, num: str) -> bool:
        num = [int(x) for x in num]
        return sum([num[x] for x in range(len(num)) if x%2==0]) == sum([num[x] for x in range(len(num)) if x%2!=0])
        
