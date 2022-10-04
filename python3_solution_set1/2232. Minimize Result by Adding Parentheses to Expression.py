##ss
class Solution:
    def minimizeResult(self, expression: str) -> str:
        
        #print(eval("2*(47+38)"))
        
        comp = expression.split("+")
        t1 = [x for x in comp[0]]
        t2 = [x for x in comp[1]]
        
        opt1 = []
        opt2 = []
        
        opt1.append(["(" + "".join(t1), "(" + "".join(t1)])
        
        for x in range(1,len(t1)):
            temp = "".join(t1[0:x]) + "*(" + "".join(t1[x:])
            temps = "".join(t1[0:x]) + "(" + "".join(t1[x:])
            opt1.append([temp,temps])
        
        
        
        for x in range(1,len(t2)):
            temp = "".join(t2[0:x]) + ")*" + "".join(t2[x:])
            temps = "".join(t2[0:x]) + ")" + "".join(t2[x:])
            opt2.append([temp,temps])
            
        temp = "".join(t2) + ")"
        opt2.append([temp,temp])
        
        variety = []
        
        for x in opt1:
            for y in opt2:
                temp = x[0] + "+" + y[0]
                temp2 = x[1] + "+" + y[1]
                
                variety.append([temp,temp2])
                
        mins = float('inf')
        ans = ""
        
        for x in variety:
            if eval(x[0]) < mins:
                mins = eval(x[0])
                ans = x[1]
                
        return ans
