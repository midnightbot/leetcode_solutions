class Solution:
    def similarRGB(self, color: str) -> str:
        
        def toint(temp):
            strs = []
            
            for x in temp:
                if x == 'a':
                    strs.append(10)
                elif x=='b':
                    strs.append(11)
                elif x=='c':
                    strs.append(12)
                elif x=='d':
                    strs.append(13)
                elif x=='e':
                    strs.append(14)
                elif x=='f':
                    strs.append(15)
                else:
                    strs.append(int(x))
                    
            strs = strs[::-1]
            
            return int(strs[1])*16 + int(strs[0])
        
        def dist(int1,int2):
            return abs(int1-int2)
        
        part1 = color[1:3]
        part2 = color[3:5]
        part3 = color[5:]
        
        arr = []
        
        arr.append(toint(part1))
        arr.append(toint(part2))
        arr.append(toint(part3))
        
        result = ""
        ords = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
        
        for x in arr:
            mins = float('inf')
            jointhis = ""
            
            for y in ords:
                if mins > dist(x,toint(str(y)+str(y))):
                    mins = dist(x,toint(str(y)+str(y)))
                    jointhis = str(y)
                    
            result+=jointhis+jointhis
            
        
        return "#" + result
        
    
        
    
        
