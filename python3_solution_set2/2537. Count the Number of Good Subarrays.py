class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        ## simple two pointer approach
        ## move j till we get k or more pairs
        ## once we get k or more pairs move i to a position where number of pairs is less than k
        dicts = {}
        pairs = 0
        i = 0
        j = 0
        n = len(nums)

        ans = 0

        while j<n:
            if nums[j] in dicts:
                pairs+=dicts[nums[j]]
                dicts[nums[j]]+=1
                if pairs >= k:

                    while pairs >= k:
                        ans+=(n-j)
                        pairs-=(dicts[nums[i]]-1)
                        dicts[nums[i]]-=1
                        i+=1
                        

            else:
                dicts[nums[j]] = 1

            j+=1
        return ans

        
