class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        
        ## simple sliding window question
        ## do not use math.pow() gives TLE
        @cache
        def find_pow(x,y):
            if y == 1:
                return x
            else:
                return x * find_pow(x,y-1)
        mods = 10**9 + 7

        dicts = {}
        ans = -1
        n = len(nums)
        
        def find_ans(comp):
            res = 0

            for it in comp:
                res+=find_pow(it, comp[it])
            return res%mods

        
        for x in range(k):
            dicts[nums[x]] = dicts.get(nums[x],0)+1
        curr = find_ans(dicts)%mods
        ans = max(ans, curr)

        for x in range(k,n):
            ## removing x-k element will reduce the sum by how much
            n1 = nums[x-k]
            p1 = dicts[n1]
            a = find_pow(n1,p1)
            if p1 == 1:
                b = 0
            else:
                b = find_pow(n1,p1-1)
            diff1 = a-b

            dicts[n1]-=1

            ## adding x element will increase the sum by how much
            n2 = nums[x]
            p2 = dicts.get(n2,0)
            if p2 == 0:
                a = 0
            else:
                a = find_pow(n2, p2)
            dicts[n2] = dicts.get(n2,0)+1
            b = find_pow(n2,p2+1)
            diff2 = b - a

            ## update the curr sum
            curr-=diff1
            curr+=diff2
            curr%=mods

            ## update the ans
            ans = max(ans, curr)

        return ans%mods
