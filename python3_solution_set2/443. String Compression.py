class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        
        prev = chars[0]
        cnt = 1
        for x in chars[1:]:
            if x == prev:
                cnt+=1
            else:
                if cnt == 1:
                    ans.append(prev)
                else:
                    ans.append(prev)
                    for it in str(cnt):
                        ans.append(it)

                cnt = 1
                prev = x

        if cnt!=0:
            if cnt == 1:
                ans.append(prev)
            else:
                ans.append(prev)
                for it in str(cnt):
                    ans.append(it)

        for x in range(len(chars)):
            chars.pop()

        for x in ans:
            chars.append(x)
