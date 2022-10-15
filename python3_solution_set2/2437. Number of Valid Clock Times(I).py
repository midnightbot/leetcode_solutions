class Solution:
    def countTime(self, time: str) -> int:
        
        ## if we have 0? then we can replace ? with 10 different values [0-9]
        ## if we have 1? then we can replace ? with 10 different values [0-9]
        ## if we have 2? then we can replace ? with 4 different values  [0-3]
        hr12 = {0:10, 1:10, 2:4} 
        
        ## if we have ?0 we can replace ? with 3 values [0-2]
        hr21 = {0:3,1:3, 2:3, 3:3, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2}
        
        
        min12 = {0:10, 1:10, 2:10, 3:10, 4:10, 5:10}
        min21 = {0:6, 1:6, 2:6, 3:6, 4:6, 5:6, 6:6, 7:6, 8:8, 9:6}
        
        
        ## calculating how many hours can be made from this structure
        a = 1
        comp1 = [time[0], time[1]]
        
        if comp1 == ['?',"?"]:
            a = 24
            
        elif comp1[0] == '?' and comp1[1]!="?":
            a = hr21[int(comp1[1])]

        elif comp1[0]!="?" and comp1[1] == "?":
            a = hr12[int(comp1[0])]
            
            
        ## calculating how many minutes can be made from this structure
        comp2 = [time[3], time[4]]
        b = 1
        if comp2 == ['?',"?"]:
            b = 60
            
        elif comp2[0] == '?' and comp2[1]!="?":
            b = min21[int(comp2[1])]

        elif comp2[0]!="?" and comp2[1] == "?":
            b = min12[int(comp2[0])]
        
        return a*b  ## finding total combinations
