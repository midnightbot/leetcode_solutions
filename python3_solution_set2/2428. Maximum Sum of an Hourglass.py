class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        
        def find_ans(arr):
            ans = 0
            
            ans+=sum(arr[0])
            ans+=sum(arr[-1])
            ans+=arr[1][1]
            return ans
        
        maxs = 0
        for x in range(0,len(grid)-2):
            for y in range(0,len(grid[0])-2):
                #print("hi")
                arr = grid[x:x+3]
                final_arr = []
                for it in arr:
                    final_arr.append(it[y:y+3])
                    
                #print(final_arr)
                #print("\n")
                maxs = max(maxs, find_ans(final_arr))
                
        return maxs
