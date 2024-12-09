class Solution:
    def is_ok(self, x, y):
        if x%2==0 and y%2!=0:
            return True

        elif x%2!=0 and y%2==0:
            return True

        return False

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ## ss
        ## simple prefix sum type question
        pre = [0]

        for x in range(len(nums)-1):
            if self.is_ok(nums[x], nums[x+1]):
                pre.append(0)
            else:
                pre.append(1)

        pre = list(accumulate(pre))
        result = []
        for x,y in queries:
            if pre[x] == pre[y]:
                result.append(True)
            else:
                result.append(False)
        return result
        
