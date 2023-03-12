class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:

        cnt = Counter({0:1})
        for it in accumulate(nums, operator.xor):
            cnt[it]+=1

        return sum([(it * (it-1))//2 for it in cnt.values()])

        
