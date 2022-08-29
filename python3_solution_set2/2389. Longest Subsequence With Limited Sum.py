import bisect
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        ans = []
        
        nums.sort()
        pre = [0] + list(itertools.accumulate(nums))
        
        for x in queries:
            done = False
            for y in range(len(pre)):
                if pre[y] > x:
                    done = True
                    ans.append(y-1)
                    break
            if done == False:
                ans.append(len(nums))
        
        return ans
        
