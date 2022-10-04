class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        ans  = []
        check1 = []
        check2 = []
        for x in range(len(timePoints)):
            str1 = timePoints[x][0]+timePoints[x][1]
            str2 = timePoints[x][3]+timePoints[x][4]
            
            ans.append(int(str1)*60 + int(str2))
            if int(str1)*60 + int(str2) > 720:
                check1.append(1440 - (int(str1)*60 + int(str2)))
            else:
                check2.append(int(str1)*60 + int(str2))
            
        check1 = sorted(check1,reverse=False)
        check2 = sorted(check2,reverse=False)
        mins1 = float('inf')
        for x in range(len(check1)-1):
            if mins1 > check1[x+1]-check1[x]:
                mins1 = check1[x+1]-check1[x]
                
        mins2 = float('inf')
        for x in range(len(check2)-1):
            if mins2 > check2[x+1]-check2[x]:
                mins2 = check2[x+1]-check2[x]
           
        minimum1 = float('inf')
        if len(check1)!=0 and len(check2)!=0:
            minimum1 = min(check1)+min(check2)
            
        mins3 = float('inf')
        ans = sorted(ans,reverse=False)
        for x in range(len(ans)-1):
            if ans[x+1]-ans[x] < mins3:
                mins3 = ans[x+1]-ans[x]
            
            
        #minimum1 = min(check1)+min(check2)
        
        return min(mins1,mins2,minimum1,mins3)
            
        
