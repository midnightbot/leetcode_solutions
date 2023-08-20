class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        arr = []
        i = 1
        while len(arr) < n:
            possible = True
            for it in arr:
                if it + i == k:
                    possible = False
                    break
            if possible:
                arr.append(i)
            i+=1

        return sum(arr)
