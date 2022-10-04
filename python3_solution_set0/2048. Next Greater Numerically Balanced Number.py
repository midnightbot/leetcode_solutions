class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        temp = [1, 22, 122, 333, 1333, 4444, 44441, 55555, 22333, 122333, 155555, 224444, 666666] ##only 6 digits number considered as 0<=n<= 10^6
        
        final_check = self.permum(temp)
        #print(final_check)
        for x in range(len(final_check)):
            if final_check[x] > n:
                return final_check[x]
            
    
        
        
    def permum(self, temp):
        temp = [str(t) for t in temp]
        final_check  = []
        for x in temp:
            final_check += list( set("".join(p) for p in itertools.permutations(list(x))))
            
        final_check = [int(c) for c in final_check]
        final_check.append(1224444) ##appending the lowest seven digit number
        final_check.sort()
        return final_check
        
