class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        def left_shift(arr, k):
            prev = arr
            for x in range(k%len(arr)):
                arr = [arr[-1]] + arr[:-1]
            
            return arr == prev

        def right_shift(arr, k):
            prev = arr
            for x in range(k%len(arr)):
                arr = arr[1:] + [arr[0]]
            return arr == prev

        ans = True
        for indx, x in enumerate(mat):
            if indx%2==0:
                ans = ans & left_shift(x,k)
            else:
                ans = ans & right_shift(x,k)
        return ans

        
