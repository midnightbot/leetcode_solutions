class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ans = 0
        data = {x:[] for x in range(len(grid[0]))}

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                data[y].append(grid[x][y])
        
        for col in data:
            arr = data[col]
            for i in range(1, len(arr)):
                if arr[i] > arr[i-1]:
                    continue
                elif arr[i] == arr[i-1]:
                    ans+=1
                    arr[i]+=1
                else:
                    diff = arr[i-1] - arr[i]
                    ans+=diff+1
                    arr[i]+=diff+1
        return ans
        
