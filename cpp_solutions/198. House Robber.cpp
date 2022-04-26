class Solution {
public:
    unordered_map<int,int> memo;
    int rob(vector<int>& nums) {
        
        
        return find_ans(nums,0);
        
    }
    
    int find_ans(vector<int>& nums, int indx){
        if (indx >= nums.size()){
            return 0;
        }
        else if(memo.find(indx)!=memo.end()){
            return memo[indx];
        }
        else{
            int a = nums[indx] + find_ans(nums, indx+2);
            int b = find_ans(nums, indx+1);
            
            if (a > b){
                memo[indx] = a;
                
            }
            else{
                memo[indx] = b;
            }
            return memo[indx];
        }
        
    }
};
