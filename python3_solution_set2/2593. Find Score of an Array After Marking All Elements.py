class Solution:
    def findScore(self, nums: List[int]) -> int:

        ## sort the array nums and traverse it in the sorted order
        n = len(nums)
        score = 0
        temp = [[nums[x], x] for x in range(n)]
        temp = sorted(temp, key = lambda x:(x[0], x[1]))
        for ele, indx in temp:
            if nums[indx]!=-1:
                score+=nums[indx]
                nums[indx] = -1
                nums[max(0,indx-1)] = -1
                nums[min(n-1, indx+1)] = -1

            else:
                continue

        return score
