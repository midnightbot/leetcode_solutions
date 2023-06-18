class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0

        while mainTank!=0:
            if mainTank >= 5:
                ans+=50
                mainTank-=5
                if additionalTank > 0:
                    additionalTank-=1
                    mainTank+=1

            else:
                ans+=mainTank*10
                mainTank = 0


        return ans
