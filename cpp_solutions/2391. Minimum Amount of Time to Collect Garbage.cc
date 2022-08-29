class Solution {
public:
    bool conts(string str, char mtc) {
        
        for(int x = 0; x< str.length(); ++x){
            if (str.at(x) == mtc) {
                return true;
            }
        }
        return false;
    }
    
    int find_count(string str, char mtc) {
        int ans = 0;
        for(int x=0; x<str.length(); ++x) {
            if (str.at(x) == mtc) {
                ++ans;
            }
        }
        return ans;
    }
    
    vector<int> PreSum(vector<int> arr) {
        vector<int> ans;
        
        ans.emplace_back(0);
        int curr = 0;
        for(auto it : arr) {
            curr += it;
            ans.emplace_back(curr);
        }
        return ans;
    }
    
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int g = 0;
        int p = 0;
        int m = 0;
        
        int g_indx = -1;
        int p_indx = -1;
        int m_indx = -1;
        
        int g_count = 0;
        int p_count = 0;
        int m_count = 0;
        vector<int> pre = PreSum(travel);
        
        
        for(int x = 0; x < garbage.size(); ++x) {
            if (conts(garbage[x], 'G')) {
                g_indx = x;
                g_count+= find_count(garbage[x],'G');
            }
            if (conts(garbage[x], 'P')) {
                // cout << "inside" << x << "\n";
                p_indx = x;
                p_count+= find_count(garbage[x],'P');
            }
            if (conts(garbage[x], 'M')) {
                m_indx = x;
                m_count+= find_count(garbage[x],'M');
            }
        }
        // cout << p_indx << "**" << "\n";
        if (g_indx!=-1) {
            g+=g_count;
            g+=pre[g_indx];
        }
        if (p_indx!=-1) {
            p+=p_count;
            p+=pre[p_indx];
        }
        if (m_indx!=-1) {
            m+=m_count;
            m+=pre[m_indx];
        }
        // cout << p << "\n";
        // cout << p_indx << "\n";
        // cout << pre[3] << "\n";
        return g + p + m;
        
    }
};
