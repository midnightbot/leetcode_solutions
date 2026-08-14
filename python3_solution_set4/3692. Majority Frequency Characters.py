class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        temp = Counter(s)
        ans = {}

        for x in temp:
            if temp[x] in ans:
                ans[temp[x]].append(x)
            else:
                ans[temp[x]] = [x]
        
        result = ''
        result_freq = 0

        for x in ans:
            if len(ans[x]) > len(result):
                result_freq = x
                result = ''.join(ans[x])
            elif len(ans[x]) == len(result):
                if x > result_freq:
                    result_freq = x
                    result = ''.join(ans[x])
        return result
        
