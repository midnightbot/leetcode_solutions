class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # minimize sum1 and maximize sum2
        num_len = len(nums)
        n = num_len//3

        # try all splits from index n to 2n
        # say x is split
        # remove all high numbers from 0..x
        # remove all small numbers from x..3n

        # here we are caluclating for all subarrays [0:x] what are min 'n' numbers to be taken for sum1
        sum1 = []
        q = []
        curr = 0
        for x in range(num_len):
            if x >= n:
                top = -q[0]
                if top > nums[x]:
                    heapq.heappop(q)
                    curr-=top
                    curr+=nums[x]
                    heapq.heappush(q, -nums[x])

            else:
                heapq.heappush(q, -nums[x])
                curr+=nums[x]
            sum1.append(curr)

        # similarly calculate what 'n' numbers to be taken for sum2 to maximize the sum
        sum2 = []
        curr = 0
        q = []
        for x in range(num_len-1,-1,-1):
            if x < num_len - n:
                top = q[0]
                if top < nums[x]:
                    heapq.heappop(q)
                    curr-=top
                    curr+=nums[x]
                    heapq.heappush(q, nums[x])
            else:
                heapq.heappush(q, nums[x])
                curr+=nums[x]
            sum2.append(curr)
        sum2 = sum2[::-1]

        # calculate diff
        ans = float('inf')
        for x in range(n-1, 2*n):
            ans =  min(ans, sum1[x] - sum2[x+1])
        # print(sum1, sum2)
        return ans
        
