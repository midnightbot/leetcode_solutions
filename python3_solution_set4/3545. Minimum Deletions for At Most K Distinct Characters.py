class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        temp = Counter(s)
        if len(temp.keys()) <= k:
            return 0
        else:
            temp = list(temp.values())
            temp.sort()
            temp = temp[:len(temp)-k]
            return sum(temp)        
