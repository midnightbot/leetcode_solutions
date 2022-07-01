class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        
        sort(boxTypes.begin(),boxTypes.end(),comp);
        //cout << boxTypes[0][1];
        int ans = 0;
        int i = 0;
        while (i<boxTypes.size() && truckSize > 0) {
            if (boxTypes[i][0] <= truckSize) {
                truckSize-=boxTypes[i][0];
                ans+=boxTypes[i][0] * boxTypes[i][1];
            }
            else {
                ans+=boxTypes[i][1] * truckSize;
                truckSize = 0;
            }
            i+=1;
            //cout << ans << " ";
        }
        return ans;
    }
    
    static bool comp(const vector<int>& a, const vector<int>& b) {
        return a[1] > b[1];
    }
};
