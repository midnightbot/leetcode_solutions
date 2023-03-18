class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        ## perm[i] > nums[i]
        ## sort nums, every number in nums should get the next big element in perm
        ## maintain freq count and solve the problem
        temp = sorted(nums)
        counter = {}

        for x in temp:
            counter[x] = counter.get(x,0) +1 

        ans = 0
        prev_balance = 0
        #print(counter)
        for it in sorted(list(counter.keys())):
            ans+= min(prev_balance, counter[it])
            prev_balance-=min(prev_balance, counter[it])
            prev_balance+=counter[it]
            #print(prev_balance)
        return ans
