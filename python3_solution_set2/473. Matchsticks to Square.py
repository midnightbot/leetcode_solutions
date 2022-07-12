##ss
class Solution:
    def makesquare(self, m: List[int]) -> bool:
        
        if sum(m)%4!=0:
            return False
        m = sorted(m,reverse=True) ##MLE saver
        maxs = sum(m)//4
        @cache
        def find_ans(s1,s2,s3,s4,indx):
            if indx == len(m):
                return s1==s2==s3==s4
            
            else:
                ans = False
                if s1 + m[indx] <= maxs:
                    ans = ans or find_ans(s1+m[indx],s2,s3,s4,indx+1)
                if s2 + m[indx] <= maxs:
                    ans = ans or find_ans(s1,s2+m[indx],s3,s4,indx+1)
                    
                if s3 + m[indx] <= maxs:
                    ans = ans or find_ans(s1,s2,s3+m[indx],s4,indx+1)
                if s4 + m[indx] <= maxs:
                    ans = ans or find_ans(s1,s2,s3,s4+m[indx],indx+1)
                return ans
            
        return find_ans(0,0,0,0,0)
        
