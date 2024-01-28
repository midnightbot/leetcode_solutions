class Solution:
    def minimumPushes(self, word: str) -> int:
        temp = Counter(word)
        arr = [(x,temp[x]) for x in temp]
        arr = sorted(arr, key = lambda x:-x[1])
        ans = 0 
        for indx, (x,y) in enumerate(arr):
            
            ans += y * ((indx//8) + 1)
        return ans
        
