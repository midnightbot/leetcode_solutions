class Solution:
    def isNumber(self, s: str) -> bool:
        ##################################################################
        ## valid number = (decimal or int) + (e or E) + (integer)
        
        ## integer = (+ or -) and one or more digits
        
        ## decimal = (+ or -)
        ## 123.
        ## 123.45
        ## .123
        ##################################################################
        
        ## finds if string is valid integer
        def valid_integer(s):
            if len(s) == 0:
                return False
            digit_count = 0
            if s[0] in ['+','-']:
                for x in range(1,len(s)):
                    if s[x] not in "1234567890":
                        return False
                    else:
                        digit_count+=1
                return digit_count>=1
            else:
                for x in range(0,len(s)):
                    if s[x] not in "1234567890":
                        return False
                    else:
                        digit_count+=1
                    
                return digit_count>=1
        ##################################################################
        
        ## finds if string is valid decimal
        def valid_decimal(s):
            curr = 0
            if len(s) == 0:
                return False
            if s[0] in ['+','-']:
                curr+=1
            dot = 0
            after_dot = 0
            before_dot = 0
            for x in range(curr, len(s)):
                if s[x] in "1234567890":
                    if dot == 1:
                        after_dot+=1
                    elif dot == 0:
                        before_dot+=1
                    continue
                elif s[x] == '.' and dot == 0:
                    dot+=1
                    continue
                else:
                    return False
                
            if dot == 1:
                if s[0] in ['+','-']:
                    s = s[1:]
                temps = s.split('.')
                temp = []
                for x in temps:
                    if len(x) > 0:
                        temp.append(x)
                if len(temp) == 1 and (s[-1] == '.' or s[0] =='.'):
                    return True
                elif len(temp) == 2 and len(temp[0])>=1 and len(temp[1])>=1:
                    return True
            else:
                return False
            
        ##################################################################
        
        c1 = s.count('e')
        c2 = s.count('E')
        
        ## invalid number
        if c1 + c2 > 1:
            return False
        
        indx = -1
        if c1 == 1:
            indx = s.index('e')
        if c2 == 1:
            indx = s.index('E')
        
        ## no e/E in the string
        ## (decimal or int )
        if indx == -1:
            return valid_integer(s) or valid_decimal(s)
        
        ## (decimal or int) + (e/E) + (int)
        else:
            if indx == len(s)-1:
                return False
            part1 = s[:indx]
            part2 = s[indx+1:]
            
            return (valid_integer(part1) or valid_decimal(part1)) and (valid_integer(part2))
        
