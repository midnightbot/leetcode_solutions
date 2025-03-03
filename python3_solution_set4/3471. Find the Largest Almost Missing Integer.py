class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = {}

        for x in range(len(nums)-k+1):
            arr = nums[x:x+k]
            
            for i in set(arr):
                freq[i] = freq.get(i,0) + 1
        
        ans = [-1]
        print(freq)
        for x in freq:
            if freq[x] == 1:
                ans.append(x)
        
        return max(ans)
        
