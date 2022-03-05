##ss
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        
        ##idea is to match first and last char with min swaps and reduce the string to s[1:-1] and solve it recursively
        
        self.ans = float('inf')
        
        n = len(s)
        ##a,b,c,d
        @lru_cache(None)
        def make_palindrome(s):
            #print(s)
            if len(s) == 1 or len(s) == 0:
                return 0
            
            elif s[0] == s[-1]:
                return make_palindrome(s[1:-1])
            
            else:
                ##making 1 chr equal to last
                
                #new_s = copy.deepcopy(s)
                
                indx1 = s.index(s[-1])
                part1 = float('inf')
                #if indx1!= len(s)-1:
                    #part1 = make_palindrome(s[0:indx1] + s[indx1+1:-1])
                 
                ##making last char match the first
                
                indx2 = s[::-1].index(s[0])
                part2 = float('inf')
                #if indx2!=0:
                    #part2 = make_palindrome(s[1:len(s)-indx2-1] + s[len(s) - indx2:])
                
                if indx1 == indx2 == None:
                    return float('inf')
                
                elif indx1 == len(s)-1 and indx2!=0:
                    return indx2 + make_palindrome(s[1:len(s)-indx2-1] + s[len(s) - indx2:])
                
                elif indx1!=len(s)-1 and indx2 == 0:
                    return indx1 + make_palindrome(s[0:indx1] + s[indx1+1:-1])
                    
                else:
                    if indx1 > len(s) - indx2-1:
                        return indx1 + make_palindrome(s[0:indx1] + s[indx1+1:-1])
                    
                    elif indx1 < len(s) - indx2 -1:
                        return indx2 + make_palindrome(s[1:len(s)-indx2-1] + s[len(s) - indx2:])
                    else:
                        return min(indx1 + make_palindrome(s[0:indx1] + s[indx1+1:-1]),indx2 + make_palindrome(s[1:len(s)-indx2-1] + s[len(s) - indx2:]))
                    
                    #return min(indx1+part1, indx2+part2)
                
                
                
        return make_palindrome(s)
                
            
            
        
