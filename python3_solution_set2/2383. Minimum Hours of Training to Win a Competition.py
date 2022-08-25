class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        
        eng = 0
        exp = 0
        ## experience gap
        for x in experience:
            if x < initialExperience:
                initialExperience+=x
            else:
                exp+=x-initialExperience+1
                initialExperience+=x-initialExperience+1
                initialExperience+=x
        
        ## energy gap
        if sum(energy) < initialEnergy:
            eng = 0
        else:
            eng+=sum(energy) - initialEnergy + 1
        #print(eng,exp)
        return eng + exp
