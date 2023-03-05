class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:

        mods = 10**9 + 7

        n = len(types)

        @cache
        def find_ans(indx, left):
            if left == 0:
                return 1

            elif indx == n:
                return 0

            else:
                ans = 0
                for it in range(types[indx][0]+1):
                    balance = left - it*types[indx][1]
                    if balance >= 0:
                        ans+= find_ans(indx+1, balance)

                return ans%mods

        return find_ans(0,target)%mods
