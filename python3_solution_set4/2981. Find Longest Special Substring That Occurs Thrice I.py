class Solution:        
    def maximumLength(self, s: str) -> int:
        count = {chr(x):[] for x in range(ord('a'), ord('a')+26)}

        prev = s[0]
        prev_count = 1

        for x in range(1, len(s)):
            if s[x] == prev:
                prev_count+=1

            else:
                count[prev].append(prev_count)
                prev = s[x]
                prev_count=1

        count[prev].append(prev_count)
        for x in count:
            count[x] = sorted(count[x], reverse=True)

        ans = -1
        # print(count)
        for x in count:
            arr = count[x]
            # print(arr, x)
            if len(arr) > 0 and arr[0] >= 3:
                ans = max(ans, arr[0]-2)
            if len(arr) >= 2:
                if arr[0] > 1:
                    ans = max(ans, min(arr[0]-1,arr[1]))
            if len(arr) > 2:
                ans = max(ans, min(arr[0],arr[1],arr[2]))

        return ans
        # print(count)


        
