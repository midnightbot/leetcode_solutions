class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> ans;
        unordered_map<int,int> maps;
       
        for (int i = 0; i < nums.size();i++){
            if (maps.find(target - nums[i])!= maps.end())
            {
                ans.push_back(i);
                ans.push_back(maps[target - nums[i]]);
                    
                return ans;
            }
            
            else{
                maps[nums[i]] = i;
            }
        }
        return ans;
    }
};
