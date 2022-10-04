##ss
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        
        ## all zero
        ##all one
        ##zero followed by one
        
        ## ill take a split point
        ## make all elements from that split point 1
        
        zeros = s.count("0")
        ans = zeros
        ones = 0
        for x in range(len(s)):
            
            #print(zeros,ones)
            ans = min(ans,zeros + ones)
            
            if s[x] == "0":
                zeros-=1
            elif s[x] == "1":
                ones+=1
        ##     min(0 followed by one at some index, making all characters 1, making all characters 0)             
        return min(ans,s.count("0"),len(s)-s.count("0"))
            
        
