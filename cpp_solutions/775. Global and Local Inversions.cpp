class Solution {
public:
    bool isIdealPermutation(vector<int>& nums) {
        
        for(int x=0 ; x<nums.size();++x) {
            if (abs(nums[x]-x) > 1) {return false;}
        }
        return true;
        
    }
};
