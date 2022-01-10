##ss
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if len(a) > len(b):
            diff = len(a) - len(b)
            adds = ""
            for x in range(diff):
                adds+="0"
                
            b = adds + b
            
        elif len(b) > len(a):
            diff = len(b) - len(a)
            adds = ""
            for x in range(diff):
                adds+="0"
                
            a = adds + a
        
        carry,ans = self.add(a,b)
        ans = ans[::-1]
        if carry == 1:
            ans = "1" + ans
            
        return ans
    def add(self,bina,binb):
        carry = 0
        result = ""
        for x in range(len(bina)-1,-1,-1):
            if bina[x] == "1" and binb[x] == "1" and carry == 0:
                result+="0"
                carry = 1
                
            elif bina[x] =="1" and binb[x] == "1" and carry == 1:
                result+="1"
                carry = 1
                
            elif bina[x] == "1" and binb[x] == "0" and carry == 0:
                result+="1"
                carry = 0
                
            elif bina[x] == "1" and binb[x] == "0" and carry == 1:
                result+="0"
                carry = 1
                
            elif bina[x] == "0" and binb[x] =="1" and carry == 0:
                result+="1"
                carry  = 0
                
            elif bina[x] == "0" and binb[x] == "1" and carry == 1:
                result+="0"
                carry = 1
                
            elif bina[x] == "0" and binb[x] == "0" and carry ==0:
                result+="0"
                carry = 0
                
            elif bina[x] == "0" and binb[x] == "0" and carry == 1:
                result+="1"
                carry = 0
        return carry,result
