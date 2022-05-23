class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        
        int ans = 1000000;
        
        for(int x: nums){
            if (abs(x) < abs(ans)){
                ans = x;
            }
            else if (abs(x) == abs(ans) && x > ans){
                ans = x;
            }
        }
        return ans;
        
    }
};
