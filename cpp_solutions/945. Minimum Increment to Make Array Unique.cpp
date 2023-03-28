class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {

        int ans = 0;
        set<int> global_seen;
        int i = 1;
        for(auto it : nums){
            global_seen.insert(it);
        }
        set<int> local_seen;
        sort(nums.begin(), nums.end());
        for(auto it : nums){
            if (local_seen.find(it) == local_seen.end()){
                local_seen.insert(it);
            } else {
                while (global_seen.find(i)!=global_seen.end() || i<=it){
                    i+=1;
                }
                ans+=(i-it);
                global_seen.insert(i);
            }
        }
        return ans;
        
    }
};
