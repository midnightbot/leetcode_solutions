class Solution {
public:
    bool canJump(vector<int>& nums) {
        int current = nums.size() - 1;
        
        for(int x=nums.size()-2;x>=0;x--){
            if(x+nums[x] >= current){
                current = x;
            }
            //current = min(current, x- nums[x]);
        }
        
        return current ==0 ;
        
    }
};
