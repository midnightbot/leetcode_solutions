class Solution:
    def maxNumberOfFamilies(self, n: int, rs: List[List[int]]) -> int:
        
        rs = sorted(rs, key = lambda x:x[0])
        
        indx = 1
        curr = 1
        temp = set([1,2,3,4,5,6,7,8,9,10])
        ans = 0
        
        for x in range(len(rs)):
            if rs[x][0]!=indx:
                diff = rs[x][0] - indx - 1
                ans+= diff * 2
                indx = rs[x][0]
                if 2 in temp and 3 in temp and 4 in temp and 5 in temp:
                    ans+=1
                    temp.remove(4)
                    temp.remove(5)
                    
                if 6 in temp and 7 in temp and 8 in temp and 9 in temp:
                    ans+=1
                    temp.remove(6)
                    temp.remove(7)
                    
                if 4 in temp and 5 in temp and 6 in temp and 7 in temp:
                    ans+=1
                
                temp = set([1,2,3,4,5,6,7,8,9,10])
                temp.remove(rs[x][1])
        
            else:
                temp.remove(rs[x][1])
                
            
        if 2 in temp and 3 in temp and 4 in temp and 5 in temp:
            ans+=1
            temp.remove(4)
            temp.remove(5)

        if 6 in temp and 7 in temp and 8 in temp and 9 in temp:
            ans+=1
            temp.remove(6)
            temp.remove(7)

        if 4 in temp and 5 in temp and 6 in temp and 7 in temp:
            ans+=1 
        
        ans+= (n-indx) * 2
        
        
        return ans
