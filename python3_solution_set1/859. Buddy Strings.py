##ss
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        diff = 0
        conn = []
        if len(s)!=len(goal):
            return False
        
        for x in range(len(s)):
            if s[x]!=goal[x]:
                diff+=1
                conn.append([s[x],goal[x]])
                
             
        
        if diff in [1]:
            return False
        
        if diff == 0:
            c = Counter(s)
            for x in c:
                if c[x] >=2:
                    return True
                
            return False
        
        if diff > 2:
            return False
        
        elif diff == 2:
            if conn[0][0] == conn[1][1] and conn[0][1] == conn[1][0]:
                return True
            
            return False
        
