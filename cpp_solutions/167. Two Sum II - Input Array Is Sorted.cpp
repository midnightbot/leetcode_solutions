class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        vector<int> ans;
        int low = 0;
        int high = numbers.size() - 1;
        
        while (low < high){
            
            if (target == numbers[low] + numbers[high]){
                ans.push_back(low + 1);
                ans.push_back(high+1);
                return ans;
            }
            else if(numbers[low] + numbers[high] < target){
                low+=1;
            }
            else{
                high-=1;
            }
        }
        
        ans.push_back(-1);
        ans.push_back(-1);
        
        return ans;
        
    }
};
