class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        ans = 0


        for x in range(len(a)):
            for y in range(len(b)):
                for z in range(len(c)):
                    temp = (a[x] ^ b[y]) ^ c[z]
                    temp = format(temp, 'b')
                    cnt = temp.count('1')
                    if cnt%2==0:
                        ans+=1
        return ans
        
