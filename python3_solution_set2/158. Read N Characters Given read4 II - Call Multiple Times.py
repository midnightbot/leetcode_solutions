# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = []
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            #print(q)
            if self.q:
                buf[i] = self.q.pop(0)
                i+=1
            else:
                self.q = ['' for x in range(4)]
                m = read4(self.q)
                if m == 0:
                    break

        return i
