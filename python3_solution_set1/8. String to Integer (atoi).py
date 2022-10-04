##ss
class Solution:
    def myAtoi(self, s: str) -> int:
        
        
        s = s.strip()
        #print(s)
        if len(s) == 0:
            return 0
        mins = 0
        pos = 0
        num = ""
        
        if s[0] == '-' or s[0]=="+":
            for x in range(1,len(s)):

                if (ord(s[x])<48 or ord(s[x])>57):
                    if len(num) == 0:
                        return 0
                    if s[0] == '+':
                        if int(num)<=pow(2,31)-1: ##number negative and in the range
                            return int(num)
                        else:##negative and out of range
                            return pow(2,31) - 1
                    else:
                        if int(num) <= pow(2,31): ##positive and in the range
                            return -1*int(num)
                        else:##positive and out of range
                            return -1 * 2147483648
                
                num+=s[x]
                
            if len(num) == 0:
                return 0
            
            if s[0] == '+':
                if int(num)<=pow(2,31)-1:
                    return int(num)
                else:
                    return pow(2,31) - 1
            else:
                if int(num) <= pow(2,31):
                    return -1*int(num)
                else:
                    return -1 * 2147483648                
            

                
            
        elif ord(s[0])>=48 and ord(s[0])<=57:
            #print("inside")
            for x in range(len(s)):
                #print(num)
                if (ord(s[x])<48 or ord(s[x])>57):
                    if len(num) == 0:
                        return 0
                    
                    if int(num) < pow(2,31) -1:
                        return int(num)
                    else:
                        return pow(2,31)-1
                
                num+=s[x]
                
            if int(num) < pow(2,31) - 1:
                return int(num)
            else:
                return pow(2,31) - 1
            
        return 0
        

                
            
            
        
        
