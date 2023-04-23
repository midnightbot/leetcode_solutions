class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        ## range [1,k]
        mods = 10**9 + 7
        n = len(s)
        @cache
        def find_ans(indx):
            if indx == n:
                return 1
            if s[indx] == '0':
                return 0

            ans = 0
            nums = 0
            for i in range(indx, n):
                nums = nums*10 + int(s[i])
                if nums <= k:
                    ans = (ans + find_ans(i+1))%mods
                else:
                    break

            return ans%mods

        return find_ans(0)


        
