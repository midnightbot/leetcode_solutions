class Solution:
    def minimizedStringLength(self, s: str) -> int:
        counter = Counter(s)
        lens = len(s)
        for c in counter:
            cnt = counter[c]
            while cnt >= 3:
                cnt-=2
                lens-=2
            if cnt == 2:
                cnt-=1
                lens-=1

        return lens
