class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        unordered_set <int> seen;
        
        for(int x: nums){
            
            if (seen.find(x)!=seen.end()){
                return true;
            }
            else{
                seen.insert(x);
            }
        }
        return false;
        
    }
};
