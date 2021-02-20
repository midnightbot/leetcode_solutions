class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 = [""]*n
        arr2 = [""]*n

        ans = [""]*2*n
        
        for x in range(n):
            arr1[x] = nums[x]
            arr2[x] = nums[x+n]
        ans[0] = arr1[0]
        ans[1] = arr2[0]
        for y in range(1,2*n):
            if y%2==0:
                ans[y]=arr1[int(y/2)]
            else:
                ans[y] = arr2[int(y/2)]
        return ans
        
