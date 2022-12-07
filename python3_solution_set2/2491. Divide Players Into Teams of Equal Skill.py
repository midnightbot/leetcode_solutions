class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill = sorted(skill)
        sums = skill[0] + skill[-1]
        n = len(skill)
        ans = 0
        ans+= (skill[0] * skill[-1])
        #print(skill)
        for x in range(1, n//2):
            temp = skill[x] + skill[-x-1]
           # print(temp)
            if temp!=sums:
                return -1
            else:
                ans+= (skill[x]) * (skill[-x-1])

        return ans
