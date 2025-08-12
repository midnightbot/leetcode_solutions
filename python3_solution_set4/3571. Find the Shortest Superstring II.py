class Solution:
    def is_contained(self, s1, s2):
        if s1 in s2:
            return s2
        elif s2 in s1:
            return s1
        return ""
        
    def find_common(self, s1, s2):
        mins = min(len(s1), len(s2))
        indx1 = -1
        indx2 = -1
        ## s1 end is s2 start
        for x in range(mins+1):
            if s2[:x] == s1[-x:]:
                indx1 = x-1
            else:
                continue

        ## s2 end is s1 start
        for x in range(mins+1):
            if s1[:x] == s2[-x:]:
                indx2 = x-1
            else:
                continue

        if indx1 == indx2 == -1:
            return s1+s2
        elif indx1 < indx2:
            return s2[:len(s2)-indx2-1] + s1
        else:
            return s1[:len(s1)-indx1-1] + s2

    def shortestSuperstring(self, s1: str, s2: str) -> str:
        is_contained = self.is_contained(s1, s2)
        if is_contained != "":
            return is_contained 
        return self.find_common(s1, s2)

        
