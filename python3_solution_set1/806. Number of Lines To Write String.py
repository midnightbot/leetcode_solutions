##ss
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 0
        prev_lines = []
        curr_width = 0
        for x in range(len(s)-1):
            thiswidth = widths[ord(s[x])-ord('a')]
            
            if curr_width + thiswidth <=100:
                curr_width+=thiswidth
                
            else:
                prev_lines.append(curr_width)
                curr_width = thiswidth
                
        thiswidth = widths[ord(s[len(s)-1]) - ord('a')]
        if curr_width+thiswidth <=100:
            curr_width+=thiswidth
            prev_lines.append(curr_width)
        else:
            prev_lines.append(curr_width)
            prev_lines.append(thiswidth)
            
        
        return [len(prev_lines),prev_lines[-1]]
        
