class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int adds) {
        
        for(int x=0;x<capacity.size();x++){
            capacity[x]-=rocks[x];
        }
        sort(capacity.begin(),capacity.end());
        
        int i = 0;
        while (adds >= 0 and i < capacity.size()){
            if (capacity[i] <= adds){
                adds-=capacity[i];
                i+=1;
            }
            else{
                break;
            }
        }
        return i;
        
    }
};
