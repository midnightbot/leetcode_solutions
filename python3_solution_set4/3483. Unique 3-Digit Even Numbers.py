class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()

        for x,y,z in permutations(digits,3):
            if x!=0 and z%2==0:
                ans.add((x,y,z))
        return len(ans)
        
