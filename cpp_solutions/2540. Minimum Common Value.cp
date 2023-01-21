class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        set<int> comp;
        for(auto it: nums1){
            comp.insert(it);
        }

        for(auto it : nums2){
            if(comp.find(it)!=comp.end()){
                return it;
            }
        }
        return -1;
    }
};
