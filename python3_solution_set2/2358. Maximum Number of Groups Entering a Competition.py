class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        grades = sorted(grades)
        ans = 0
        prev = 0
        prev_c = 0
        
        curr = 0
        curr_c = 0
        
        for x in grades:
            curr+=x
            curr_c+=1
            
            if curr > prev and curr_c > prev_c:
                prev_c = curr_c
                prev = curr
                curr = 0
                curr_c = 0
                ans+=1

        return ans
        
