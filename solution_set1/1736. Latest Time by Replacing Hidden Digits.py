##ss
class Solution:
    def maximumTime(self, time: str) -> str:
        
        ##lastest time
        
        
        s = time.split(":")
        
        hrs = ""
        mins = ""
        if s[0] == "??":
            hrs = "23"
            
        elif s[0][0] == "?" and s[0][1]!="?":
            if int(s[0][1]) < 4:
                hrs = "2" + s[0][1]
                
            else:
                hrs = "1" + s[0][1]
                
        elif s[0][0]!="?" and s[0][1] == "?":
            if s[0][0] == "2":
                hrs = "2" + "3"
                
            else:
                hrs = s[0][0] + "9"
                
        else:
            hrs = s[0]
                
        if s[1] == "??":
            mins = "59"
            
        elif s[1][0] == "?" and s[1][1]!="?":
            mins = "5" + s[1][1]
            
        elif s[1][0]!="?" and s[1][1] == "?":
            mins = s[1][0] + "9"
            
        else:
            mins = s[1]
        return hrs + ":" + mins
        #f
        
