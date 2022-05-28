class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        int sum = 0;
        int n = nums.size() ;
        for(int x:nums){
            sum+=x;
        }
        
        return n*(n+1)/2 - sum;
        
    }
};
