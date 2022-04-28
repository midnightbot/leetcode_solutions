class Solution {
public:
    unordered_map<int,int> memo;
    //unordered_map<int,int> memo2;
    //first and not last
    //last and not first
    int rob(vector<int>& nums) {
        
        //cout << nums.len();
        if (nums.size() == 1){
            return nums[0];
        }
        int ans1 = find_ans(0,nums.size()-1,nums);
        memo.clear();
        int ans2 = find_ans(1,nums.size(),nums);
        //cout << ans1 << ans2;
        if (ans1>ans2){
            return ans1;
        }
        else{
            return ans2;
        }
        
    }
    
    int find_ans(int indx, int end,vector<int>& nums){
        //cout << indx <<" " <<end << "\n";
        if(memo.find(indx)!=memo.end()){
            return memo[indx];
        }
        if (indx>=end){
            return 0;
        }
        
        else{
            int a = find_ans(indx+1,end,nums);
            int b = find_ans(indx+2,end,nums) + nums[indx];
            
            if (a>b){
                memo[indx] = a;
            }
            else{
                memo[indx] = b;
            }
            return memo[indx];
        }
    }
};
