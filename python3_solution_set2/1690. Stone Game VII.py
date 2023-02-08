class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)

        @cache
        def find_ans(i,j):
            #print(i,j)
            if i >= j:
                return 0

            elif i >= n or j < 0:
                return 0

            else:
                ##alice takes f (i,j) -> (i+1,j)
                ##bob takes f (i+1,j) -> (i+2,j)
                ### in this case diff btn alice and bob will be
                ## sum(arr[i+1,j]) - sum(arr[i+2,j]) = arr[i+1]
                ## diff btn alice and bob will always be the number bob picks as he is playing after alice
                if i+1 < n:
                    a = stones[i+1] + find_ans(i+2,j)
                else:
                    a = stones[i]
                ##alice takes f
                ##bob takes l
                if i+1 < j:
                    b = stones[j] + find_ans(i+1,j-1)
                else:
                    b = stones[j]
                ##alice takes l
                ##bob takes f
                if i < j-1:
                    c = stones[i] + find_ans(i+1,j-1)
                else:
                    c = stones[i]
                ##alice takes l
                ##bob takes l
                if j-1>=0:
                    d = stones[j-1] + find_ans(i,j-2)
                else:
                    d = stones[j]
                return max(min(a,b), min(c,d))

        return find_ans(0, n-1)
