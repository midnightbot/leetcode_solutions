class Solution:
    def countTime(self, time: str) -> int:
        
        
        hr12 = {0:10, 1:10, 2:4}
        
        hr21 = {0:3,1:3, 2:3, 3:3, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2}
        
        
        min12 = {0:10, 1:10, 2:10, 3:10, 4:10, 5:10}
        min21 = {0:6, 1:6, 2:6, 3:6, 4:6, 5:6, 6:6, 7:6, 8:8, 9:6}
        
        
        a = 1
        comp1 = [time[0], time[1]]
        
        if comp1 == ['?',"?"]:
            a = 24
            
        elif comp1[0] == '?' and comp1[1]!="?":
            a = hr21[int(comp1[1])]

        elif comp1[0]!="?" and comp1[1] == "?":
            a = hr12[int(comp1[0])]
            
        
        comp2 = [time[3], time[4]]
        b = 1
        if comp2 == ['?',"?"]:
            b = 60
            
        elif comp2[0] == '?' and comp2[1]!="?":
            b = min21[int(comp2[1])]

        elif comp2[0]!="?" and comp2[1] == "?":
            b = min12[int(comp2[0])]
        
        return a*b
