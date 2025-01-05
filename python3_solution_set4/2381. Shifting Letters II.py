class Solution:
    def find_char(self, s, net):
        if net >= 0:
            i = chr(((ord(s) - ord('a')) + net)%26 + ord('a'))
        else:
            i = chr(((ord(s) - ord('a')) + net + 26)%26 + ord('a'))

        return i

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0 for x in range(n+1)] # store num of fwd shifts
        arr2 = [0 for x in range(n+1)] # store num of backward shifts

        for x,y,z in shifts:
            if z == 1:
                arr[x]+=1
                arr[y+1]-=1
            else:
                arr2[x]+=1
                arr2[y+1]-=1

        arr = list(accumulate(arr)) # prefix sum to find number of fwd shifts at each position
        arr2 = [-x for x in list(accumulate(arr2))] # prefix sum to find number of back shifts at each position
        net = [arr[x]+arr2[x] for x in range(len(arr))] # net shifts at each position
        net = net[:-1]
        ans = ""
        for x in range(n):
            ans += self.find_char(s[x], net[x])
        
        return ans




        
