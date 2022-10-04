##ss
class Solution:
    def countSegments(self, s: str) -> int:
        
        temp = []
        for x in s.split(" "):
            if len(x) > 0 and x[0] in "!@#$%^&*()_+-=',.:" + "qwertyuiopasdfghjklzxcvbnm" + "QWERTYUIOPASDFGHJKLZXCVBNM" + "1234567890":
                temp.append(x)
        #print(temp)
        return len(temp)
        
