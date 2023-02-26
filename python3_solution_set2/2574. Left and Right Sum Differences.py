class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:

        pre1 = [0] + list(itertools.accumulate(nums))
        pre2 = (list(itertools.accumulate(nums[::-1]))[::-1] + [0])

        ans = []
        #print(pre1)
        #print(pre2)
        for x in range(len(nums)):
            ans.append(abs(pre1[x+1] - pre2[x]))

        return ans
