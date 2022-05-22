//ss
class Solution {
public:
    int maxNumberOfBalloons(string text) {
        
        vector<int> maps(26,0);
        
        for (char ch: text){
            maps[int(ch)-int('a')]+=1;
        }
        
        int ans = 10000;
        // b , a , l/2, o/2, n -> mins
        string temp = "balon";
        
        for (char ch: temp){
            if (ch == 'b' || ch == 'a' || ch == 'n'){
                ans = min(ans, maps[int(ch)-int('a')]);
            }
            else{
                ans = min(ans, (int)(maps[int(ch)-int('a')]/2));
            }
        }
        return ans;
        
    }
};
