class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        def find_ans(arr):
            freq = dict(Counter(arr))
            freq = [[i,freq[i]] for i in freq]
            freq = sorted(freq, key = lambda i:(-i[1],-i[0]))
            freq = [i for i in freq][:x]
            ans = []
            for (i,j) in freq:
                ans+=[i for k in range(j)]
            # print(ans)
            return sum(ans)

        result = []
        for z in range(len(nums)-k+1):
            temp = find_ans(nums[z:z+k])
            result.append(temp)
        return result
        
