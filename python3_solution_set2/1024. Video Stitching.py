class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:

        ans = 0
        end  = 0
        curr_pos = 0

        clips = sorted(clips, key = lambda x:x[0])

        for xleft, xright in clips:
            if xleft > time or end>=time:
                continue

            if xleft <= curr_pos:
                end = max(end, xright)
            else:
                ans+=1
                curr_pos = end
                if xleft <= curr_pos:
                    end = max(end, xright)
                
        if curr_pos!=end:
            ans+=1

        return ans if end>=time else -1
