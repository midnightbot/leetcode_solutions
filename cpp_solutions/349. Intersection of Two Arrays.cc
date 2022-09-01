class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;
        set<int> seen;
        
        set<int> set1;
        for(auto it : nums1) {
            set1.insert(it);
        }
        
        for(auto it : nums2) {
            if (set1.find(it)!=set1.end()) {
                seen.insert(it);
            }
        }
        
        for(auto it: seen) {
            ans.emplace_back(it);
        }
        
        return ans; 
    }
};
