class Solution {
public:
    int maxConsecutive(int bottom, int top, vector<int>& special) {
        int ans = 0; 
        special.insert(special.begin(),bottom-1);
        special.insert(special.begin(),top+1);
        
        sort(special.begin(),special.end());
        //cout << special[0] << "\n";
        for(int x = 1; x < special.size();x++){
            //cout << special[x] << "\n";
            if (special[x] > top+1){
                break;
            }
            
            else if (special[x] >= bottom-1 and special[x-1] >= bottom-1){
                ans = max(special[x] - special[x-1] - 1, ans);
            }
        }
        
        return ans;
    }
};
