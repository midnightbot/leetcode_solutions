class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        vector<int> ans;
        
        sort(nums.begin(),nums.end());
        for (auto x: queries) {
            int curr = 0;
            bool done = false;
            for(int y =0; y < nums.size();++y) {
                curr+=nums[y];
                // cout << curr << " ";
                if (curr > x) {
                    ans.emplace_back(y);
                    done = true;
                    break;
                }
            
            }
            if (done == false) {
                
                ans.emplace_back(nums.size());
            }
            // cout << "\n";
            
        }
        return ans;
        
    }
};
