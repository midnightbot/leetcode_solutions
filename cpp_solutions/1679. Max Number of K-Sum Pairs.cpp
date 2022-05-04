class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int,int> seen;
        
        
        int c = 0;
        
        for(int x=0; x<nums.size();x++){
            
            int key = k - nums[x];
            
            if (seen.find(key)!=seen.end() and seen[key]!=0){
                c+=1;
                seen[key]-=1;
                //seen.erase(key);
            }
            else{
                if(seen.find(nums[x])!=seen.end()){
                    seen[nums[x]]+=1;
                }
                else{
                    seen[nums[x]] = 1;
                }
                //seen.insert(nums[x]);
            }
        }
        return c;
        
    }
};
