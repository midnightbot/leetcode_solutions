class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = format(n,'b')
        ans = ans[::-1]
        even = 0
        odd = 0
        for x in range(len(ans)):
            if x%2==0 and ans[x] == '1':
                even+=1
            elif x%2!=0 and ans[x] == '1':
                odd+=1
        return [even,odd]
