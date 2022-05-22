class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int> freq;
        
        for(int x: nums){
            
            if(freq.find(x)!=freq.end()){
                freq[x]+=1;
            }
            else{
                freq.insert({x,1});
            }
        }
        
        for(auto& it: freq){
            //cout << it.first << it.second;
            if (it.second > (int) nums.size()/2){
                return it.first;
            }
        }
        return 0;
    }
};
