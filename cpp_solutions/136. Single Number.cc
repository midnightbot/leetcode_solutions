class Solution {
public:
    int singleNumber(vector<int>& nums) {
        set<int> seen;
        for(auto it : nums) {
            if (seen.find(it)!=seen.end()) {
                seen.erase(it);
            } else {
                seen.insert(it);
            }
        }
        return *seen.begin();
    }
};
