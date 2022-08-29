class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g = 0
        p = 0
        m = 0
        
        pre = [0] + list(accumulate(travel))
        
        g_indx = -1
        p_indx = -1
        m_indx = -1
        g_count = 0
        p_count = 0
        m_count = 0
        for x in range(len(garbage)):
            if "G" in garbage[x]:
                g_indx = x
                g_count+=garbage[x].count("G")
            if "P" in garbage[x]:
                p_indx = x
                p_count+=garbage[x].count("P")
            if "M" in garbage[x]:
                m_indx = x
                m_count+=garbage[x].count("M")
            
        if g_indx!=-1:
            g = g_count + pre[g_indx]
        if p_indx!=-1:
            p = p_count + pre[p_indx]
        if m_indx!=-1:
            m = m_count + pre[m_indx]
        #print(g,p,m)
        return g + p + m
