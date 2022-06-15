//ss
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        
        unordered_map <int, int> temp1;
        unordered_map <int, int> temp2;
        
        vector<int> ans;
        int count;
        for(int x: nums1){
            
            if (temp1.find(x)!=temp1.end()){
                
                temp1[x]+=1;
                    
            }else{
                temp1.insert({x,1});
            }
        }
        //
        for(int x: nums2){
            
            if (temp2.find(x)!=temp2.end()){
                
                temp2[x]+=1;
                    
            }else{
                temp2.insert({x,1});
            }
        }
        
        for(auto& it:temp1){
            if (temp2.find(it.first)!=temp2.end()){
                count = min(it.second, temp2[it.first]);
                
                for(int x= 0; x< count; x++){
                    ans.push_back(it.first);
                }
            }
        }
        
        return ans;
        
    }
};
