class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        int ans = 0;
        sort(players.begin(), players.end());
        
        
        sort(trainers.begin(), trainers.end());
        int i = 0;
        int t = trainers.size();
        for(auto it : players) {
            
            while (i < t && it > trainers[i]) {
                ++i;
            }
            
            if (i < t && it <= trainers[i]) {
                ++i;
                ++ans;
            }
            
        }
        return ans;
    }
};
