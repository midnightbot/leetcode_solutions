import copy

class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        # prefix sum on char freq

        def find_char_count(i,j, arr):
            if i == 0:
                return arr[j]
            else:
                ans = [0 for x in range(26)]
                for x in range(26):
                    ans[x] = arr[j][x] - arr[i-1][x]
                return ans

        freq = []
        start = [0 for x in range(26)]
        ans = []
        for x in range(len(s)):            
            start[ord(s[x]) - ord('a')]+=1
            freq.append(copy.deepcopy(start))

        # print(freq)
        for (x,y) in queries:
            char_counts = find_char_count(x,y,freq)
            result = 0
            for i in char_counts:
                result += (i)*(i+1)//2
            ans.append(result)
            
        return ans

        
