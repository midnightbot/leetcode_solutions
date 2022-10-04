class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        
        def valid(i,j,k):
            sums = i + j + k
            if sums%i==0:
                return sums%j!=0 and sums%k!=0
            elif sums%j == 0:
                return sums%k!=0
            
            else:
                return sums%k == 0
            
            
        comp = Counter(nums)
        ans = 0
        
        for x in range(1,101):
            for y in range(x,101):
                for z in range(y,101):
                    if x in comp and y in comp and z in comp and valid(x,y,z):
                        if x==y:
                            ans+= comp[x] * (comp[x]-1)//2 * comp[z]
                            
                        elif y==z:
                            ans+= comp[x] * (comp[y]) * (comp[y]-1)//2
                            
                        else:
                            ans+= comp[x] * comp[y] * comp[z]
                            
        return ans * 6 ## ans * 3!
        
                        
        
