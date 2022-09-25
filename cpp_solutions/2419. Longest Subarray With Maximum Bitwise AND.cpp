class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int ans = *max_element(nums.begin(), nums.end());
        int c = 0;
        int result = 0;
        
        for(auto it : nums) {
            if (it == ans) {++c;}
            else{c=0;}
            result = max(result, c);
        }
        return result;
        
    }
};
