class Solution {
public:
    int minimumLines(vector<vector<int>>& sp) {
        
        sort(sp.begin(),sp.end());
        //if slope same no line added
        // else lines+=1
        if (sp.size() == 1){
            return 0;
        }
        else if(sp.size() == 2){
            return 1;
        }
        else if(sp.size() == 3){
            long double slp1 = findslope(sp[0],sp[1]);
            long double slp2 = findslope(sp[1],sp[2]);
            
            if (slp1 == slp2){
                return 1;
            }
            else{
                return 2;
            }
        }
        int lines = 1;
        long double prev_slope = findslope(sp[0],sp[1]);
        
        for(int x=2;x<sp.size();x++){
            if (findslope(sp[x-1],sp[x]) == prev_slope){
                continue;
            }
            else{
                lines+=1;
                prev_slope = findslope(sp[x-1],sp[x]);
            }
            
            cout << lines;
        }
        return lines;
    }
    
    long double findslope(vector<int> pt1, vector<int> pt2){
        if (pt2[0] - pt1[0] == 0){
            return std::numeric_limits<long double>::infinity();
            
        }
        return (pt2[1] - pt1[1]) /(long double) (pt2[0] - pt1[0]);
    }
};
