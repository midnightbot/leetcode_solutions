##ss
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        
        ans = []
        n = len(nums[0])
        for x,y in queries:
            new_arr = [[int(nums[a][-y:]),a] for a in range(len(nums))]
            new_arr = sorted(new_arr, key = lambda x:x[0])
            #print(new_arr)
            ans.append(new_arr[x-1][1])
            
        return ans
