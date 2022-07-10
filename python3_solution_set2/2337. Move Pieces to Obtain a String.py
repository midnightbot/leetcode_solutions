##ss
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        str1 = ""
        str2 = ""
        a = []
        b = []
        for it,x in enumerate(start):
            if x!="_":
                str1+=x
                a.append([x,it])
                
        for it,x in enumerate(target):
            if x!="_":
                str2+=x
                b.append([x,it])
                
        if str1!=str2:
            return False
        #print(a,b)
        for x in range(len(a)):
            if a[x][0] == "L" and a[x][1] < b[x][1]:
                return False
                
            elif a[x][0] == "R" and a[x][1] > b[x][1]:
                return False
            
        return True
