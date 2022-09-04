class Solution {
public:
    void PrintMap(map<char,int> g) {
        for(auto it : g) {
            cout << it.first << "-" << it.second;
            cout << "\n";
        }
    }
    
    bool checkDistances(string s, vector<int>& distance) {
        map<char,int> g;
        
        for(int x=0; x<s.length(); ++x) {
            if (g.find(s.at(x))==g.end()) {
                g.insert({s.at(x),x});
            } else {
                int temp = g[s.at(x)];
                g[s.at(x)] = x - temp - 1;
            }
        }
        // PrintMap(g);
        for(auto it : g) {
            if(it.second!=distance[int(it.first)-int('a')]) {
                return false;
            }
        }
        
        return true;
    }
};
