class Solution:
    def countAsterisks(self, s: str) -> int:
        
        if s.count("|") == 0:
            return s.count("*")
        temp = s.split("|")
        if len(temp) < 2:
            return 0
        c = 0
        print(temp)
        for x in range(0,len(temp),2):
            c+=temp[x].count("*")
            
        return c
        
