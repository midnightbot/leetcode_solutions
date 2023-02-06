class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def find_ans(i,j):
            if i > j:
                return 0

            else:
                a = nums[i] + find_ans(i+2,j)
                b = nums[i] + find_ans(i+1,j-1)

                c = nums[j] + find_ans(i+1,j-1)
                d = nums[j] + find_ans(i,j-2)

                return max(min(a,b), min(c,d))

        ans = find_ans(0,len(nums)-1)
        left = sum(nums) - ans

        return ans>=left

        
